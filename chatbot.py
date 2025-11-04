import pickle
import re
import os
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
        self.model = None
        self.load_model()
        
        # Conversation state
        self.conversation_state = {}
        self.awaiting_bmi_data = False
        self.bmi_data = {}
        
    def load_model(self):
        """Load the trained ML model"""
        try:
            model_path = 'models/logistic_regression_model.pkl'
            if os.path.exists(model_path):
                with open(model_path, 'rb') as f:
                    self.model = pickle.load(f)
                print("Model loaded successfully!")
            else:
                print("Model not found. Please train the model first by running train_model.py")
        except Exception as e:
            print(f"Error loading model: {e}")
    
    def preprocess_text(self, text: str) -> str:
        """Basic text preprocessing"""
        # Convert to lowercase and remove extra spaces
        text = text.lower().strip()
        # Remove special characters except spaces
        text = re.sub(r'[^\w\s]', '', text)
        return text
    
    def predict_intent(self, text: str) -> Tuple[str, float]:
        """Predict the intent of user input with keyword fallback"""
        if not self.model:
            return self.keyword_based_intent(text), 0.5
        
        try:
            processed_text = self.preprocess_text(text)
            prediction = self.model.predict([processed_text])[0]
            confidence = max(self.model.predict_proba([processed_text])[0])
            
            # If confidence is low, use keyword-based detection
            if confidence < 0.4:
                keyword_intent = self.keyword_based_intent(text)
                if keyword_intent != "unknown":
                    return keyword_intent, 0.6
            
            return prediction, confidence
        except Exception as e:
            print(f"Error predicting intent: {e}")
            return self.keyword_based_intent(text), 0.5
    
    def keyword_based_intent(self, text: str) -> str:
        """Fallback intent detection using keywords"""
        text_lower = text.lower()
        
        # Greeting keywords
        greeting_words = ['hello', 'hi', 'hey', 'good morning', 'good evening', 'howdy', 'greetings']
        if any(word in text_lower for word in greeting_words):
            return "greeting"
        
        # BMI keywords  
        bmi_words = ['bmi', 'body mass index', 'weigh', 'weight', 'height', 'tall', 'kg', 'lbs', 'pounds', 'meters', 'feet', 'inches']
        weight_height_pattern = r'(weigh|weight).*?\d+.*?(tall|height).*?\d+'
        if any(word in text_lower for word in bmi_words) or re.search(weight_height_pattern, text_lower):
            return "bmi"
        
        # Nutrition keywords
        nutrition_words = ['calories', 'nutrition', 'protein', 'carbs', 'fat', 'nutrients', 'vitamin']
        if any(word in text_lower for word in nutrition_words):
            return "nutrition"
        
        # Workout keywords
        workout_words = ['exercise', 'workout', 'training', 'fitness', 'muscle', 'strength', 'cardio', 'gym']
        if any(word in text_lower for word in workout_words):
            return "workout"
        
        # Motivation keywords
        motivation_words = ['motivation', 'inspire', 'encourage', 'lazy', 'tired', 'give up', 'help me']
        if any(word in text_lower for word in motivation_words):
            return "motivation"
        
        return "unknown"
    
    def extract_food_item(self, text: str) -> str:
        """Extract food item from nutrition query"""
        # Remove common nutrition-related words
        nutrition_words = ['calories', 'nutrition', 'nutrients', 'protein', 'carbs', 'fat', 'in', 'for', 'of', 'how', 'much', 'many', 'what', 'about']
        words = text.lower().split()
        food_words = [word for word in words if word not in nutrition_words and len(word) > 2]
        return ' '.join(food_words) if food_words else text
    
    def extract_exercise_keywords(self, text: str) -> Dict[str, str]:
        """Extract exercise-related keywords from workout query"""
        text_lower = text.lower()
        
        # Muscle groups
        muscle_map = {
            'chest': 'chest', 'pecs': 'chest',
            'biceps': 'biceps', 'bicep': 'biceps', 'arms': 'biceps',
            'triceps': 'triceps', 'tricep': 'triceps',
            'shoulders': 'shoulders', 'shoulder': 'shoulders',
            'back': 'lats', 'lats': 'lats',
            'legs': 'quadriceps', 'quads': 'quadriceps', 'thighs': 'quadriceps',
            'glutes': 'glutes', 'butt': 'glutes',
            'calves': 'calves', 'calf': 'calves',
            'abs': 'abdominals', 'core': 'abdominals', 'abdominals': 'abdominals'
        }
        
        # Exercise types
        type_map = {
            'cardio': 'cardio', 'running': 'cardio', 'cycling': 'cardio',
            'strength': 'strength', 'weights': 'strength', 'lifting': 'strength',
            'stretching': 'stretching', 'flexibility': 'stretching',
            'plyometrics': 'plyometrics', 'hiit': 'plyometrics'
        }
        
        muscle = None
        exercise_type = None
        
        for keyword, muscle_group in muscle_map.items():
            if keyword in text_lower:
                muscle = muscle_group
                break
        
        for keyword, ex_type in type_map.items():
            if keyword in text_lower:
                exercise_type = ex_type
                break
        
        return {'muscle': muscle, 'type': exercise_type}
    
    def extract_bmi_data(self, text: str) -> Optional[Dict]:
        """Extract BMI data from user input"""
        # Look for weight and height patterns
        weight_pattern = r'(?:weight|weigh)\s*(\d+(?:\.\d+)?)\s*(?:kg|kilograms?|lbs?|pounds?)|(\d+(?:\.\d+)?)\s*(?:kg|kilograms?|lbs?|pounds?)'
        height_pattern = r'(?:height|tall|i\'?m)\s*(\d+\.?\d*)\s*(?:m|meters?|cm|centimeters?|ft|feet|in|inches?|\'|\")?|(\d+\.?\d*)\s*(?:m|meters?|cm|centimeters?|ft|feet)'
        
        weight_match = re.search(weight_pattern, text.lower())
        height_match = re.search(height_pattern, text.lower())
        
        if weight_match and height_match:
            # Extract weight (could be in group 1 or 2)
            weight = float(weight_match.group(1) if weight_match.group(1) else weight_match.group(2))
            # Extract height (could be in group 1 or 2)  
            height = float(height_match.group(1) if height_match.group(1) else height_match.group(2))
            
            # Determine units based on context
            unit_system = "metric"
            if "lbs" in text.lower() or "pounds" in text.lower():
                unit_system = "imperial"
            elif "feet" in text.lower() or "ft" in text.lower() or "inches" in text.lower() or "in" in text.lower():
                unit_system = "imperial"
            
            # Convert height if needed
            if unit_system == "metric" and height > 10:  # Assume cm if > 10
                height = height / 100  # Convert cm to m
            elif unit_system == "imperial" and height < 10:  # Assume feet
                height = height * 12  # Convert feet to inches
            elif unit_system == "metric" and height < 3:  # Already in meters
                height = height  # Keep as is
            
            return {
                'weight': weight,
                'height': height,
                'unit_system': unit_system
            }
        
        return None
    
    def handle_bmi_intent(self, text: str) -> str:
        """Handle BMI-related queries"""
        # Try to extract BMI data from the text
        bmi_data = self.extract_bmi_data(text)
        
        if bmi_data:
            # Calculate BMI directly
            return self.bmi_calculator.format_bmi_response(
                bmi_data['weight'], 
                bmi_data['height'], 
                bmi_data['unit_system']
            )
        else:
            # Ask for BMI data
            self.awaiting_bmi_data = True
            return ("📊 **BMI Calculator**\n\n"
                   "I'd be happy to calculate your BMI! Please provide your:\n"
                   "• Weight (in kg or lbs)\n"
                   "• Height (in meters, cm, feet, or inches)\n\n"
                   "Example: \"I weigh 70 kg and I'm 1.75 meters tall\"\n"
                   "or \"I weigh 154 lbs and I'm 5 feet 9 inches tall\"")
    
    def handle_nutrition_intent(self, text: str) -> str:
        """Handle nutrition-related queries"""
        food_item = self.extract_food_item(text)
        if not food_item:
            return ("🍎 **Nutrition Information**\n\n"
                   "Please specify a food item you'd like to know about!\n"
                   "Example: \"nutrition facts for chicken breast\" or \"calories in apple\"")
        
        nutrition_data = self.api_service.get_nutrition_info(food_item)
        return self.api_service.format_nutrition_response(nutrition_data)
    
    def handle_workout_intent(self, text: str) -> str:
        """Handle workout-related queries"""
        keywords = self.extract_exercise_keywords(text)
        exercises = self.api_service.get_exercise_info(
            exercise_type=keywords.get('type', ''),
            muscle=keywords.get('muscle', '')
        )
        return self.api_service.format_exercise_response(exercises)
    
    def handle_motivation_intent(self, text: str) -> str:
        """Handle motivation-related queries"""
        return self.motivation_service.format_motivation_response(text)
    
    def handle_greeting_intent(self, text: str) -> str:
        """Handle greeting queries"""
        return ("👋 **Hello! Welcome to your AI Fitness Assistant!** 🏋️‍♀️\n\n"
               "I'm here to help you with:\n"
               "• 💪 **Workout advice** - Get exercise recommendations\n"
               "• 🍎 **Nutrition info** - Learn about food calories and nutrients\n"
               "• 📊 **BMI calculation** - Check your body mass index\n"
               "• 🌟 **Motivation** - Get inspiring fitness quotes and tips\n\n"
               "What would you like to know about today? Just ask me anything fitness-related!")
    
    def handle_unknown_intent(self, text: str) -> str:
        """Handle unknown or unclear queries"""
        return ("🤔 **I'm not sure how to help with that.**\n\n"
               "I can assist you with:\n"
               "• **Workouts**: \"Show me chest exercises\" or \"I want to build muscle\"\n"
               "• **Nutrition**: \"Calories in chicken breast\" or \"nutrition facts for apple\"\n"
               "• **BMI**: \"Calculate my BMI\" or \"I weigh 70kg and I'm 1.75m tall\"\n"
               "• **Motivation**: \"I need motivation\" or \"inspire me\"\n\n"
               "Please try rephrasing your question, and I'll do my best to help! 💪")
    
    def process_message(self, user_input: str) -> str:
        """Process user input and generate response"""
        if not user_input.strip():
            return "Please enter a message!"
        
        # Check if we're waiting for BMI data
        if self.awaiting_bmi_data:
            bmi_data = self.extract_bmi_data(user_input)
            if bmi_data:
                self.awaiting_bmi_data = False
                return self.bmi_calculator.format_bmi_response(
                    bmi_data['weight'], 
                    bmi_data['height'], 
                    bmi_data['unit_system']
                )
            else:
                return ("❌ I couldn't understand your weight and height. Please try again with a format like:\n"
                       "\"I weigh 70 kg and I'm 1.75 meters tall\" or\n"
                       "\"I weigh 154 lbs and I'm 5 feet 9 inches tall\"")
        
        # Predict intent
        intent, confidence = self.predict_intent(user_input)
        
        # Handle based on intent
        if intent == "workout":
            return self.handle_workout_intent(user_input)
        elif intent == "nutrition":
            return self.handle_nutrition_intent(user_input)
        elif intent == "bmi":
            return self.handle_bmi_intent(user_input)
        elif intent == "motivation":
            return self.handle_motivation_intent(user_input)
        elif intent == "greeting":
            return self.handle_greeting_intent(user_input)
        else:
            return self.handle_unknown_intent(user_input)

# Test function
def test_chatbot():
    """Test chatbot functionality"""
    chatbot = FitnessChatbot()
    
    test_messages = [
        "Hello",
        "I want to do chest exercises",
        "Calories in chicken breast",
        "Calculate my BMI",
        "I need motivation",
        "I weigh 70 kg and I'm 1.75 meters tall",
    ]
    
    for message in test_messages:
        print(f"User: {message}")
        response = chatbot.process_message(message)
        print(f"Bot: {response}")
        print("-" * 50)

if __name__ == "__main__":
    test_chatbot()