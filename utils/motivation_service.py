import random
from typing import List

class MotivationService:
    def __init__(self):
        self.motivational_quotes = [
            # Fitness and Exercise Motivation
            "💪 The only bad workout is the one that didn't happen!",
            "🏃‍♀️ Your body can do it. It's your mind you need to convince.",
            "⚡ Strength doesn't come from what you can do. It comes from overcoming the things you once thought you couldn't.",
            "🔥 Don't stop when you're tired. Stop when you're done!",
            "🌟 The pain you feel today will be the strength you feel tomorrow.",
            "🎯 Success isn't given. It's earned in the gym, on the field, and in every training session.",
            "💥 Push yourself because no one else is going to do it for you.",
            "🏆 Champions train, losers complain.",
            "✨ The only person you are destined to become is the person you decide to be.",
            "🚀 Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.",
            
            # Health and Wellness Motivation
            "🌱 Take care of your body. It's the only place you have to live.",
            "💚 Health is not about the weight you lose, but about the life you gain.",
            "🧘‍♀️ A healthy outside starts from the inside.",
            "🌈 You don't have to be perfect, you just have to be better than you were yesterday.",
            "🦋 Progress, not perfection.",
            "🌸 Your health is an investment, not an expense.",
            "💎 You are stronger than you think and more capable than you imagine.",
            "🌟 Small changes can make a big difference.",
            "🌊 Consistency is key to achieving your health goals.",
            "🌞 Every day is a new opportunity to improve your health.",
            
            # Diet and Nutrition Motivation
            "🥗 You are what you eat, so don't be fast, cheap, easy or fake.",
            "🍎 Eat clean, train hard, stay healthy.",
            "🥑 Fuel your body with the right foods and watch it transform.",
            "🌾 Good nutrition is the foundation of a healthy lifestyle.",
            "🥕 Every meal is a chance to nourish your body.",
            "🍓 Eat the rainbow - colorful foods are full of nutrients!",
            "🥪 A balanced diet is a cookie in each hand... just kidding! Balance is key.",
            "🥤 Hydrate, nourish, and energize your body.",
            "🍌 Food is fuel, not therapy.",
            "🥒 Make healthy choices today for a healthier tomorrow.",
            
            # Mental Strength and Mindset
            "🧠 Your mind is your most powerful tool. Use it wisely.",
            "💭 Positive thoughts lead to positive actions.",
            "🎯 Focus on progress, not perfection.",
            "🔄 Fall seven times, stand up eight.",
            "🌅 Every morning is a fresh start to become the best version of yourself.",
            "🎪 Life begins at the end of your comfort zone.",
            "🔋 You have the power to change your life one healthy choice at a time.",
            "🎭 Be yourself, everyone else is taken.",
            "🌠 Dream big, work hard, stay focused.",
            "⭐ You are capable of amazing things!",
            
            # Goal Achievement
            "🎯 Goals are dreams with deadlines.",
            "📈 Success is the sum of small efforts repeated day in and day out.",
            "🏅 Winners never quit, and quitters never win.",
            "🎖️ The difference between ordinary and extraordinary is that little extra.",
            "🚧 Obstacles are those frightful things you see when you take your eyes off your goals.",
            "📊 Track your progress, celebrate your wins, learn from your setbacks.",
            "🔥 Discipline is choosing between what you want now and what you want most.",
            "⏰ The best time to plant a tree was 20 years ago. The second best time is now.",
            "🎨 Create the life you want, one healthy choice at a time.",
            "🏃‍♂️ It's not about being perfect, it's about being consistent.",
            
            # Self-Love and Confidence
            "💖 Love yourself enough to live a healthy lifestyle.",
            "👑 You are worth the effort it takes to be healthy.",
            "🌟 Believe in yourself, even when others don't.",
            "💝 Self-care is not selfish, it's essential.",
            "🦸‍♀️ You are your own superhero.",
            "💪 Strong is beautiful, healthy is beautiful, you are beautiful.",
            "🌈 Embrace your journey, celebrate your progress.",
            "✨ You are enough, just as you are, and you deserve to be healthy and happy.",
            "🦋 Transform yourself from the inside out.",
            "🎯 You have everything within you to succeed."
        ]
        
        self.encouragement_messages = [
            "🌟 You've got this! Every step forward is progress.",
            "💪 Keep going! Your future self will thank you.",
            "🔥 Don't give up now! You're closer than you think.",
            "⚡ Stay strong! Champions are made in moments of doubt.",
            "🚀 Push through! Great things never come from comfort zones.",
            "🏆 Keep fighting! Your dedication will pay off.",
            "💎 Stay focused! Diamonds are formed under pressure.",
            "🌅 New day, new opportunities! You can do this.",
            "🎯 Stay on track! Every healthy choice matters.",
            "💥 Power through! You're stronger than your excuses."
        ]
        
        self.success_tips = [
            "🎯 Set small, achievable goals and celebrate each victory!",
            "📅 Create a routine and stick to it - consistency is key!",
            "📝 Track your progress - what gets measured gets managed!",
            "🤝 Find a workout buddy for accountability and motivation!",
            "🎵 Create an energizing playlist to pump you up!",
            "📚 Educate yourself about fitness and nutrition!",
            "🧘‍♀️ Practice mindfulness and listen to your body!",
            "💤 Prioritize sleep - recovery is part of the process!",
            "🥗 Meal prep to set yourself up for success!",
            "🏅 Reward yourself for reaching milestones (non-food rewards)!"
        ]
    
    def get_random_quote(self) -> str:
        """Get a random motivational quote"""
        return random.choice(self.motivational_quotes)
    
    def get_encouragement(self) -> str:
        """Get an encouraging message"""
        return random.choice(self.encouragement_messages)
    
    def get_success_tip(self) -> str:
        """Get a success tip"""
        return random.choice(self.success_tips)
    
    def get_personalized_motivation(self, user_context: str = "") -> str:
        """Get personalized motivation based on context"""
        base_message = self.get_random_quote()
        
        if "tired" in user_context.lower() or "exhausted" in user_context.lower():
            return f"{base_message}\n\n🌙 Remember: Rest is part of the journey. Listen to your body and take care of yourself!"
        elif "lazy" in user_context.lower() or "unmotivated" in user_context.lower():
            return f"{base_message}\n\n⚡ Start small today! Even 5 minutes of movement is better than none. You've got this!"
        elif "give up" in user_context.lower() or "quit" in user_context.lower():
            return f"{base_message}\n\n🔥 Don't quit! Remember why you started. Every champion was once a beginner who refused to give up!"
        elif "discouraged" in user_context.lower() or "sad" in user_context.lower():
            return f"{base_message}\n\n💖 Be patient with yourself. Progress isn't always linear, but every step counts!"
        else:
            return f"{base_message}\n\n{self.get_success_tip()}"
    
    def format_motivation_response(self, context: str = "") -> str:
        """Format a complete motivational response"""
        if context:
            main_message = self.get_personalized_motivation(context)
        else:
            main_message = self.get_random_quote()
        
        encouragement = self.get_encouragement()
        tip = self.get_success_tip()
        
        response = f"🌟 **Motivation Boost** 🌟\n\n"
        response += f"{main_message}\n\n"
        response += f"**Quick Encouragement:**\n{encouragement}\n\n"
        response += f"**Success Tip:**\n{tip}\n\n"
        response += f"💪 **You're doing great! Keep up the amazing work!** 💪"
        
        return response

# Test function
def test_motivation_service():
    """Test motivation service functionality"""
    motivation = MotivationService()
    
    print("Random Quote:")
    print(motivation.get_random_quote())
    
    print("\nEncouragement:")
    print(motivation.get_encouragement())
    
    print("\nSuccess Tip:")
    print(motivation.get_success_tip())
    
    print("\nPersonalized Motivation (tired):")
    print(motivation.get_personalized_motivation("I'm feeling tired"))
    
    print("\nFormatted Response:")
    print(motivation.format_motivation_response("I need motivation"))

if __name__ == "__main__":
    test_motivation_service()