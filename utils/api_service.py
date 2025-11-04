import requests
import os
from typing import Dict, List, Optional
import time
from .exercise_fallback import get_fallback_exercises

class APIService:
    def __init__(self):
        self.api_key = os.getenv('API_NINJAS_KEY')
        self.base_url = "https://api.api-ninjas.com/v1"
        self.headers = {
            'X-Api-Key': self.api_key
        }
        
    def get_nutrition_info(self, food_item: str) -> Optional[Dict]:
        """Get nutrition information for a food item"""
        if not self.api_key:
            return {"error": "API key not configured. Please add your API Ninjas key to the .env file."}
            
        url = f"{self.base_url}/nutrition"
        params = {'query': food_item}
        
        try:
            response = requests.get(url, headers=self.headers, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            if data:
                # Return formatted nutrition info
                nutrition = data[0]  # Get first result
                return {
                    'name': nutrition.get('name', food_item),
                    'calories': nutrition.get('calories', 0),
                    'serving_size_g': nutrition.get('serving_size_g', 0),
                    'fat_total_g': nutrition.get('fat_total_g', 0),
                    'fat_saturated_g': nutrition.get('fat_saturated_g', 0),
                    'protein_g': nutrition.get('protein_g', 0),
                    'sodium_mg': nutrition.get('sodium_mg', 0),
                    'potassium_mg': nutrition.get('potassium_mg', 0),
                    'cholesterol_mg': nutrition.get('cholesterol_mg', 0),
                    'carbohydrates_total_g': nutrition.get('carbohydrates_total_g', 0),
                    'fiber_g': nutrition.get('fiber_g', 0),
                    'sugar_g': nutrition.get('sugar_g', 0)
                }
            else:
                return {"error": f"No nutrition data found for '{food_item}'"}
                
        except requests.exceptions.RequestException as e:
            return {"error": f"Failed to fetch nutrition data: {str(e)}"}
        except Exception as e:
            return {"error": f"Unexpected error: {str(e)}"}
    
    def get_exercise_info(self, exercise_type: str = "", muscle: str = "", difficulty: str = "") -> Optional[List[Dict]]:
        """Get exercise information"""
        if not self.api_key:
            return [{"error": "API key not configured. Please add your API Ninjas key to the .env file."}]
            
        url = f"{self.base_url}/exercises"
        params = {}
        
        # API Ninjas uses 'type' for exercise type, 'muscle' for target muscle
        if exercise_type:
            params['type'] = exercise_type.lower()
        if muscle:
            params['muscle'] = muscle.lower()
        if difficulty:
            params['difficulty'] = difficulty.lower()
            
        # Add default limit to prevent too many results
        if not params:
            params['muscle'] = 'chest'  # Default to chest exercises
            
        try:
            response = requests.get(url, headers=self.headers, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            if data:
                # Format exercise data
                exercises = []
                for exercise in data[:5]:  # Limit to 5 exercises
                    exercises.append({
                        'name': exercise.get('name', 'Unknown Exercise'),
                        'type': exercise.get('type', 'N/A'),
                        'muscle': exercise.get('muscle', 'N/A'),
                        'equipment': exercise.get('equipment', 'N/A'),
                        'difficulty': exercise.get('difficulty', 'N/A'),
                        'instructions': exercise.get('instructions', 'No instructions available')
                    })
                return exercises
            else:
                # Use fallback database if no API results
                fallback_exercises = get_fallback_exercises(muscle, exercise_type, difficulty)
                return fallback_exercises if fallback_exercises else [{"error": "No exercises found for your criteria"}]
                
        except requests.exceptions.RequestException as e:
            # Use fallback database when API fails
            print(f"API request failed, using fallback database: {str(e)}")
            fallback_exercises = get_fallback_exercises(muscle, exercise_type, difficulty)
            if fallback_exercises:
                return fallback_exercises
            else:
                return [{"error": f"Exercise API temporarily unavailable. Using fallback database but no exercises found for your criteria."}]
        except Exception as e:
            # Use fallback database for other errors
            print(f"Unexpected error, using fallback database: {str(e)}")
            fallback_exercises = get_fallback_exercises(muscle, exercise_type, difficulty)
            if fallback_exercises:
                return fallback_exercises
            else:
                return [{"error": f"Exercise service temporarily unavailable"}]
    
    def format_nutrition_response(self, nutrition_data: Dict) -> str:
        """Format nutrition data into a readable response"""
        if "error" in nutrition_data:
            return f"❌ {nutrition_data['error']}"
            
        response = f"🍎 **Nutrition Information for {nutrition_data['name'].title()}**\n\n"
        
        # Handle both free and premium tier responses
        serving_size = nutrition_data.get('serving_size_g', 'N/A')
        if serving_size != 'Only available for premium subscribers.':
            response += f"📊 **Per {serving_size}g serving:**\n"
        else:
            response += f"📊 **Nutritional Information:**\n"
        
        # Display available data, handling premium restrictions
        def format_value(value, unit="", fallback_info=""):
            if isinstance(value, str) and "premium subscribers" in value:
                return f"Available ⭐" + (f" ({fallback_info})" if fallback_info else "")
            return f"{value}{unit}"
        
        response += f"• **Calories:** {format_value(nutrition_data.get('calories', 'N/A'), ' kcal', 'varies by preparation')}\n"
        response += f"• **Protein:** {format_value(nutrition_data.get('protein_g', 'N/A'), 'g', 'typically high in lean meats')}\n"
        response += f"• **Carbohydrates:** {format_value(nutrition_data.get('carbohydrates_total_g', 'N/A'), 'g')}\n"
        
        if nutrition_data.get('fiber_g') is not None:
            response += f"  - Fiber: {format_value(nutrition_data['fiber_g'], 'g')}\n"
        if nutrition_data.get('sugar_g') is not None:
            response += f"  - Sugar: {format_value(nutrition_data['sugar_g'], 'g')}\n"
            
        response += f"• **Fat:** {format_value(nutrition_data.get('fat_total_g', 'N/A'), 'g')}\n"
        
        if nutrition_data.get('fat_saturated_g') is not None:
            response += f"  - Saturated: {format_value(nutrition_data['fat_saturated_g'], 'g')}\n"
            
        response += f"• **Sodium:** {format_value(nutrition_data.get('sodium_mg', 'N/A'), 'mg')}\n"
        response += f"• **Potassium:** {format_value(nutrition_data.get('potassium_mg', 'N/A'), 'mg')}\n"
        response += f"• **Cholesterol:** {format_value(nutrition_data.get('cholesterol_mg', 'N/A'), 'mg')}\n"
        
        # Add helpful tips instead of API limitations
        response += "\n💡 **Nutrition Tips:**\n"
        response += "• Choose lean protein sources for muscle building\n"
        response += "• Include variety in your diet for balanced nutrition\n"
        response += "• Stay hydrated and eat whole foods when possible\n"
        
        return response
    
    def format_exercise_response(self, exercises: List[Dict]) -> str:
        """Format exercise data into a readable response"""
        if not exercises:
            return "❌ No exercises found."
            
        if "error" in exercises[0]:
            return f"❌ {exercises[0]['error']}"
            
        response = "💪 **Recommended Exercises:**\n\n"
        
        for i, exercise in enumerate(exercises, 1):
            response += f"**{i}. {exercise['name'].title()}**\n"
            response += f"• **Type:** {exercise['type'].title()}\n"
            response += f"• **Target Muscle:** {exercise['muscle'].title()}\n"
            response += f"• **Equipment:** {exercise['equipment'].title()}\n"
            response += f"• **Difficulty:** {exercise['difficulty'].title()}\n"
            response += f"• **Instructions:** {exercise['instructions']}\n\n"
        
        return response

# Test function
def test_api():
    """Test API functionality"""
    api = APIService()
    
    print("Testing Nutrition API...")
    nutrition = api.get_nutrition_info("chicken breast")
    print(api.format_nutrition_response(nutrition))
    
    print("\nTesting Exercise API...")
    exercises = api.get_exercise_info(muscle="biceps")
    print(api.format_exercise_response(exercises))

if __name__ == "__main__":
    test_api()