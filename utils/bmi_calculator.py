from typing import Tuple

class BMICalculator:
    def __init__(self):
        self.bmi_categories = {
            "underweight": (0, 18.5),
            "normal": (18.5, 25),
            "overweight": (25, 30),
            "obese": (30, float('inf'))
        }
    
    def calculate_bmi(self, weight_kg: float, height_m: float) -> float:
        """Calculate BMI given weight in kg and height in meters"""
        if height_m <= 0 or weight_kg <= 0:
            raise ValueError("Weight and height must be positive numbers")
        
        bmi = weight_kg / (height_m ** 2)
        return round(bmi, 2)
    
    def calculate_bmi_imperial(self, weight_lbs: float, height_inches: float) -> float:
        """Calculate BMI given weight in pounds and height in inches"""
        if height_inches <= 0 or weight_lbs <= 0:
            raise ValueError("Weight and height must be positive numbers")
        
        # Convert to metric
        weight_kg = weight_lbs * 0.453592
        height_m = height_inches * 0.0254
        
        return self.calculate_bmi(weight_kg, height_m)
    
    def classify_bmi(self, bmi: float) -> str:
        """Classify BMI into categories"""
        for category, (min_bmi, max_bmi) in self.bmi_categories.items():
            if min_bmi <= bmi < max_bmi:
                return category
        return "unknown"
    
    def get_bmi_info(self, bmi: float) -> dict:
        """Get comprehensive BMI information"""
        category = self.classify_bmi(bmi)
        
        info = {
            "bmi": bmi,
            "category": category,
            "description": self._get_category_description(category),
            "health_risks": self._get_health_risks(category),
            "recommendations": self._get_recommendations(category)
        }
        
        return info
    
    def _get_category_description(self, category: str) -> str:
        """Get description for BMI category"""
        descriptions = {
            "underweight": "Below normal weight",
            "normal": "Normal weight range",
            "overweight": "Above normal weight",
            "obese": "Significantly above normal weight"
        }
        return descriptions.get(category, "Unknown category")
    
    def _get_health_risks(self, category: str) -> str:
        """Get health risks for BMI category"""
        risks = {
            "underweight": "May indicate malnutrition, eating disorders, or other health issues",
            "normal": "Lowest risk of weight-related health problems",
            "overweight": "Increased risk of heart disease, diabetes, and high blood pressure",
            "obese": "High risk of heart disease, diabetes, stroke, and other health issues"
        }
        return risks.get(category, "Unknown risks")
    
    def _get_recommendations(self, category: str) -> str:
        """Get recommendations for BMI category"""
        recommendations = {
            "underweight": "Consider consulting a healthcare provider. Focus on healthy weight gain through balanced nutrition and strength training.",
            "normal": "Maintain your current weight through regular exercise and balanced nutrition.",
            "overweight": "Consider gradual weight loss through increased physical activity and calorie reduction.",
            "obese": "Consult a healthcare provider. Focus on sustainable weight loss through diet and exercise."
        }
        return recommendations.get(category, "Consult a healthcare provider")
    
    def format_bmi_response(self, weight: float, height: float, unit_system: str = "metric") -> str:
        """Format BMI calculation response"""
        try:
            if unit_system.lower() == "metric":
                bmi = self.calculate_bmi(weight, height)
                weight_unit = "kg"
                height_unit = "m"
            else:
                bmi = self.calculate_bmi_imperial(weight, height)
                weight_unit = "lbs"
                height_unit = "inches"
            
            info = self.get_bmi_info(bmi)
            
            response = f"📊 **BMI Calculation Results**\n\n"
            response += f"• **Weight:** {weight} {weight_unit}\n"
            response += f"• **Height:** {height} {height_unit}\n"
            response += f"• **BMI:** {info['bmi']}\n"
            response += f"• **Category:** {info['category'].title()}\n"
            response += f"• **Description:** {info['description']}\n\n"
            response += f"**Health Information:**\n"
            response += f"• **Risks:** {info['health_risks']}\n\n"
            response += f"**Recommendations:**\n"
            response += f"• {info['recommendations']}\n\n"
            response += f"*Note: BMI is a general indicator and may not account for muscle mass, bone density, and other factors. Consult a healthcare provider for personalized advice.*"
            
            return response
            
        except ValueError as e:
            return f"❌ Error calculating BMI: {str(e)}"
        except Exception as e:
            return f"❌ Unexpected error: {str(e)}"

# Test function
def test_bmi_calculator():
    """Test BMI calculator functionality"""
    calculator = BMICalculator()
    
    # Test metric system
    print("Testing Metric System:")
    print(calculator.format_bmi_response(70, 1.75, "metric"))
    
    print("\n" + "="*50 + "\n")
    
    # Test imperial system
    print("Testing Imperial System:")
    print(calculator.format_bmi_response(154, 69, "imperial"))

if __name__ == "__main__":
    test_bmi_calculator()