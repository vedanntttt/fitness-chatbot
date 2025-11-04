import re
import random
from typing import Dict, Tuple, Optional
from dotenv import load_dotenv
from utils.api_service import APIService
from utils.bmi_calculator import BMICalculator
from utils.motivation_service import MotivationService

# Load environment variables
load_dotenv()

class FitnessChatbot:
    def __init__(self):
        self.api_service = APIService()
        self.bmi_calculator = BMICalculator()
        self.motivation_service = MotivationService()
        
        # Conversation state
        self.conversation_state = {}
        self.awaiting_bmi_data = False
        self.bmi_data = {}
        
        # Intent keywords mapping (lightweight alternative to ML)
        self.intent_keywords = {
            'exercise_recommendation': [
                'exercise', 'workout', 'training', 'fitness', 'gym', 'cardio', 
                'strength', 'muscle', 'routine', 'plan', 'recommendation'
            ],
            'nutrition_advice': [
                'nutrition', 'diet', 'food', 'calories', 'protein', 'carbs', 
                'fat', 'meal', 'eating', 'nutrients', 'vitamins'
            ],
            'bmi_calculation': [
                'bmi', 'body mass index', 'weight', 'height', 'calculate', 
                'body fat', 'overweight', 'underweight'
            ],
            'motivation': [
                'motivation', 'inspire', 'quote', 'encourage', 'support', 
                'help', 'boost', 'confidence', 'success'
            ],
            'general_health': [
                'health', 'wellness', 'tips', 'advice', 'healthy', 'lifestyle', 
                'habits', 'wellbeing', 'medical'
            ]
        }
        
    def preprocess_text(self, text: str) -> str:
        """Basic text preprocessing"""
        text = text.lower().strip()
        text = re.sub(r'[^\w\s]', '', text)
        return text
    
    def predict_intent(self, text: str) -> Tuple[str, float]:
        """Predict intent using keyword matching (lightweight alternative)"""
        preprocessed_text = self.preprocess_text(text)
        words = preprocessed_text.split()
        
        intent_scores = {}
        
        # Calculate scores based on keyword matches
        for intent, keywords in self.intent_keywords.items():
            score = 0
            for word in words:
                for keyword in keywords:
                    if keyword in word or word in keyword:
                        score += 1
            
            if score > 0:
                intent_scores[intent] = score / len(words)
        
        if intent_scores:
            best_intent = max(intent_scores, key=intent_scores.get)
            confidence = intent_scores[best_intent]
            return best_intent, confidence
        else:
            return 'general_health', 0.3
    
    def generate_response(self, user_input: str) -> str:
        """Generate response based on predicted intent"""
        try:
            intent, confidence = self.predict_intent(user_input)
            
            # Handle BMI calculation flow
            if self.awaiting_bmi_data:
                return self.handle_bmi_input(user_input)
            
            if intent == 'exercise_recommendation':
                return self.get_exercise_recommendation(user_input)
            elif intent == 'nutrition_advice':
                return self.get_nutrition_advice(user_input)
            elif intent == 'bmi_calculation':
                return self.initiate_bmi_calculation()
            elif intent == 'motivation':
                return self.motivation_service.get_motivational_quote()
            else:
                return self.get_general_health_advice()
                
        except Exception as e:
            return f"I'm sorry, I encountered an error. Please try asking your question differently. Error: {str(e)}"
    
    def get_exercise_recommendation(self, user_input: str) -> str:
        """Get exercise recommendations"""
        try:
            # Extract muscle group or exercise type from input
            muscle_groups = ['chest', 'back', 'shoulders', 'arms', 'legs', 'abs', 'cardio']
            detected_muscle = None
            
            for muscle in muscle_groups:
                if muscle in user_input.lower():
                    detected_muscle = muscle
                    break
            
            if not detected_muscle:
                detected_muscle = 'chest'  # default
            
            exercises = self.api_service.get_exercises_by_muscle(detected_muscle)
            if exercises:
                response = f"Here are some great {detected_muscle} exercises for you:\n\n"
                for i, exercise in enumerate(exercises[:3], 1):
                    response += f"{i}. **{exercise.get('name', 'Unknown')}**\n"
                    response += f"   Equipment: {exercise.get('equipment', 'None')}\n"
                    response += f"   Instructions: {exercise.get('instructions', 'Follow proper form')}\n\n"
                return response
            else:
                return self.get_fallback_exercises(detected_muscle)
                
        except Exception as e:
            return f"I couldn't fetch exercises right now. Here's a basic {detected_muscle or 'general'} exercise: Push-ups are great for building upper body strength!"
    
    def get_nutrition_advice(self, user_input: str) -> str:
        """Get nutrition advice"""
        try:
            # Extract food item from input
            words = user_input.lower().split()
            food_items = ['apple', 'banana', 'chicken', 'rice', 'bread', 'egg', 'milk', 'salmon']
            
            detected_food = None
            for word in words:
                for food in food_items:
                    if food in word or word in food:
                        detected_food = food
                        break
                if detected_food:
                    break
            
            if detected_food:
                nutrition = self.api_service.get_nutrition_info(detected_food)
                if nutrition:
                    response = f"Nutrition information for {detected_food}:\n\n"
                    for item in nutrition[:3]:
                        response += f"**{item.get('name', detected_food)}** (per 100g):\n"
                        response += f"• Calories: {item.get('calories', 'N/A')}\n"
                        response += f"• Protein: {item.get('protein_g', 'N/A')}g\n"
                        response += f"• Carbs: {item.get('carbohydrates_total_g', 'N/A')}g\n"
                        response += f"• Fat: {item.get('fat_total_g', 'N/A')}g\n\n"
                    return response
            
            return self.get_general_nutrition_advice()
            
        except Exception as e:
            return "Here's some general nutrition advice: Focus on a balanced diet with plenty of vegetables, lean proteins, whole grains, and adequate hydration!"
    
    def initiate_bmi_calculation(self) -> str:
        """Start BMI calculation process"""
        self.awaiting_bmi_data = True
        self.bmi_data = {}
        return "I'd be happy to help you calculate your BMI! Please provide your height and weight. For example: 'I am 170 cm tall and weigh 70 kg' or 'I am 5'8\" and weigh 150 lbs'"
    
    def handle_bmi_input(self, user_input: str) -> str:
        """Handle BMI calculation input"""
        try:
            height, weight, height_unit, weight_unit = self.bmi_calculator.parse_measurements(user_input)
            
            if height and weight:
                bmi, category = self.bmi_calculator.calculate_bmi(height, weight, height_unit, weight_unit)
                self.awaiting_bmi_data = False
                
                response = f"**BMI Calculation Results:**\n\n"
                response += f"• Your BMI: **{bmi:.1f}**\n"
                response += f"• Category: **{category}**\n\n"
                response += self.bmi_calculator.get_bmi_advice(category)
                
                return response
            else:
                return "I couldn't understand your measurements. Please try again with format like: 'I am 170 cm and 70 kg' or '5 feet 8 inches, 150 pounds'"
                
        except Exception as e:
            self.awaiting_bmi_data = False
            return "Sorry, I couldn't calculate your BMI. Please try again with your height and weight."
    
    def get_general_health_advice(self) -> str:
        """Provide general health advice"""
        tips = [
            "Stay hydrated by drinking at least 8 glasses of water daily! 💧",
            "Aim for 7-9 hours of quality sleep each night for optimal recovery! 😴",
            "Include at least 30 minutes of physical activity in your daily routine! 🏃‍♂️",
            "Eat a variety of colorful fruits and vegetables for essential nutrients! 🥗",
            "Practice stress management through meditation or deep breathing! 🧘‍♀️",
            "Take regular breaks from sitting and stretch throughout the day! 🧘‍♂️"
        ]
        return random.choice(tips)
    
    def get_fallback_exercises(self, muscle_group: str) -> str:
        """Provide fallback exercises when API fails"""
        exercises = {
            'chest': ['Push-ups', 'Chest dips', 'Wall push-ups'],
            'back': ['Pull-ups', 'Rows', 'Superman exercise'],
            'shoulders': ['Shoulder press', 'Lateral raises', 'Front raises'],
            'arms': ['Bicep curls', 'Tricep dips', 'Arm circles'],
            'legs': ['Squats', 'Lunges', 'Calf raises'],
            'abs': ['Planks', 'Crunches', 'Mountain climbers'],
            'cardio': ['Jumping jacks', 'High knees', 'Burpees']
        }
        
        exercise_list = exercises.get(muscle_group, exercises['chest'])
        response = f"Here are some {muscle_group} exercises you can try:\n\n"
        for i, exercise in enumerate(exercise_list, 1):
            response += f"{i}. {exercise}\n"
        
        return response
    
    def get_general_nutrition_advice(self) -> str:
        """Provide general nutrition advice"""
        advice = [
            "Focus on whole, unprocessed foods for better nutrition! 🥬",
            "Include lean proteins in every meal for muscle maintenance! 🍗",
            "Choose complex carbohydrates over simple sugars for sustained energy! 🍠",
            "Don't forget healthy fats like avocados, nuts, and olive oil! 🥑",
            "Eat the rainbow - colorful foods provide diverse nutrients! 🌈",
            "Practice portion control and mindful eating! 🍽️"
        ]
        return random.choice(advice)