// Chat functionality
let messages = [];

// API Configuration
const API_BASE_URL = '/api/chat'; // This will be our Python backend endpoint

// Initialize chat
document.addEventListener('DOMContentLoaded', function() {
    // Add event listener for Enter key
    document.getElementById('userInput').addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });
});

// Send message function
async function sendMessage() {
    const userInput = document.getElementById('userInput');
    const message = userInput.value.trim();
    
    if (!message) return;
    
    // Add user message to chat
    addMessage('user', message);
    userInput.value = '';
    
    // Show loading
    showLoading(true);
    
    try {
        // For local development, use fallback responses
        if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
            // Use fallback response for local testing
            const response = await getFallbackResponse(message);
            addMessage('bot', response);
            return;
        }
        
        // Call backend API (for production)
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                message: message,
                conversation_history: messages.slice(-10) // Send last 10 messages for context
            })
        });
        
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        
        const data = await response.json();
        
        // Add bot response to chat
        addMessage('bot', data.response || 'Sorry, I encountered an error. Please try again.');
        
    } catch (error) {
        console.error('Error:', error);
        // Fallback to local responses
        const fallbackResponse = await getFallbackResponse(message);
        addMessage('bot', fallbackResponse);
    } finally {
        showLoading(false);
    }
}

// Add message to chat
function addMessage(role, content) {
    const chatMessages = document.getElementById('chatMessages');
    const messageDiv = document.createElement('div');
    messageDiv.className = role === 'user' ? 'user-message' : 'bot-message';
    
    const messageContent = document.createElement('div');
    messageContent.className = 'message-content';
    
    if (role === 'user') {
        messageContent.innerHTML = `<strong>You:</strong> ${escapeHtml(content)}`;
    } else {
        messageContent.innerHTML = `<strong>🤖 Fitness Coach:</strong> ${formatBotResponse(content)}`;
    }
    
    messageDiv.appendChild(messageContent);
    chatMessages.appendChild(messageDiv);
    
    // Store message in history
    messages.push({ role, content });
    
    // Scroll to bottom
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Format bot response with proper line breaks and formatting
function formatBotResponse(content) {
    return escapeHtml(content)
        .replace(/\n\n/g, '<br><br>')
        .replace(/\n/g, '<br>')
        .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
        .replace(/• /g, '• ');
}

// Escape HTML to prevent XSS
function escapeHtml(text) {
    const map = {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#039;'
    };
    return text.replace(/[&<>"']/g, function(m) { return map[m]; });
}

// Show/hide loading indicator
function showLoading(show) {
    const loading = document.getElementById('loading');
    const sendButton = document.getElementById('sendButton');
    const userInput = document.getElementById('userInput');
    
    loading.style.display = show ? 'flex' : 'none';
    sendButton.disabled = show;
    userInput.disabled = show;
    
    if (show) {
        sendButton.textContent = 'Sending...';
    } else {
        sendButton.textContent = 'Send';
    }
}

// Quick action function
function quickAction(message) {
    document.getElementById('userInput').value = message;
    sendMessage();
}

// Clear chat function
function clearChat() {
    const chatMessages = document.getElementById('chatMessages');
    // Keep only the initial bot message
    chatMessages.innerHTML = `
        <div class="bot-message">
            <div class="message-content">
                <strong>🤖 Fitness Coach:</strong> 
                Hello! I'm your AI fitness coach. I can help you with exercise recommendations, nutrition advice, BMI calculations, and motivation. What would you like to know?
            </div>
        </div>
    `;
    messages = [];
}

// Enhanced fallback for when backend is not available
async function getFallbackResponse(message) {
    const lowerMessage = message.toLowerCase();
    
    // BMI calculation logic
    if (lowerMessage.includes('bmi') || (lowerMessage.includes('cm') && lowerMessage.includes('kg')) || 
        (lowerMessage.includes('feet') && lowerMessage.includes('pounds'))) {
        
        // Try to extract height and weight
        const bmiResult = calculateBMIFromText(message);
        if (bmiResult) {
            return bmiResult;
        }
        
        return "To calculate your BMI, please provide your height and weight like:\n\n• 'I am 170 cm tall and weigh 70 kg'\n• '5 feet 8 inches, 150 pounds'\n\n**BMI Categories:**\n• Underweight: Below 18.5\n• Normal weight: 18.5-24.9\n• Overweight: 25-29.9\n• Obese: 30 and above";
    }
    
    // Exercise recommendations with specific muscle groups
    if (lowerMessage.includes('exercise') || lowerMessage.includes('workout')) {
        const muscleGroups = {
            'chest': ['Push-ups', 'Chest dips', 'Wall push-ups', 'Incline push-ups'],
            'back': ['Pull-ups', 'Rows', 'Superman exercise', 'Reverse flies'],
            'shoulders': ['Shoulder press', 'Lateral raises', 'Front raises', 'Arm circles'],
            'arms': ['Bicep curls', 'Tricep dips', 'Arm circles', 'Diamond push-ups'],
            'legs': ['Squats', 'Lunges', 'Calf raises', 'Wall sits'],
            'abs': ['Planks', 'Crunches', 'Mountain climbers', 'Bicycle crunches'],
            'cardio': ['Jumping jacks', 'High knees', 'Burpees', 'Running in place']
        };
        
        // Check for specific muscle group
        for (const [muscle, exercises] of Object.entries(muscleGroups)) {
            if (lowerMessage.includes(muscle)) {
                return `Great ${muscle} exercises for you:\n\n${exercises.map((ex, i) => `${i + 1}. **${ex}**`).join('\n')}\n\n💡 **Tips:**\n• Start with 3 sets of 10-15 reps\n• Focus on proper form over speed\n• Rest 30-60 seconds between sets\n• Stay hydrated!`;
            }
        }
        
        return "Here are some excellent full-body exercises:\n\n1. **Push-ups** - Upper body strength\n2. **Squats** - Lower body power\n3. **Planks** - Core stability\n4. **Burpees** - Full body cardio\n5. **Lunges** - Leg strength & balance\n\n💪 **Beginner tip:** Start with 2-3 sets of 8-12 reps each!";
    }
    
    // Nutrition advice with specific foods
    if (lowerMessage.includes('nutrition') || lowerMessage.includes('diet') || lowerMessage.includes('food')) {
        const foods = ['chicken', 'rice', 'banana', 'apple', 'egg', 'salmon', 'broccoli', 'oats'];
        const mentionedFood = foods.find(food => lowerMessage.includes(food));
        
        if (mentionedFood) {
            const nutritionInfo = {
                'chicken': '**Chicken (100g):**\n• Calories: 165\n• Protein: 31g\n• Fat: 3.6g\n• Carbs: 0g\n\n🍗 Excellent lean protein source!',
                'rice': '**Brown Rice (100g cooked):**\n• Calories: 111\n• Protein: 3g\n• Fat: 0.9g\n• Carbs: 23g\n\n🍚 Great source of complex carbs!',
                'banana': '**Banana (medium):**\n• Calories: 105\n• Protein: 1.3g\n• Fat: 0.4g\n• Carbs: 27g\n\n🍌 Perfect pre/post workout snack!',
                'apple': '**Apple (medium):**\n• Calories: 95\n• Protein: 0.5g\n• Fat: 0.3g\n• Carbs: 25g\n\n🍎 High in fiber and antioxidants!',
                'egg': '**Egg (large):**\n• Calories: 70\n• Protein: 6g\n• Fat: 5g\n• Carbs: 0.6g\n\n🥚 Complete protein with all amino acids!',
                'salmon': '**Salmon (100g):**\n• Calories: 208\n• Protein: 25g\n• Fat: 12g\n• Carbs: 0g\n\n🐟 Rich in omega-3 fatty acids!',
                'broccoli': '**Broccoli (100g):**\n• Calories: 34\n• Protein: 2.8g\n• Fat: 0.4g\n• Carbs: 7g\n\n🥦 Packed with vitamins and minerals!',
                'oats': '**Oats (100g dry):**\n• Calories: 389\n• Protein: 17g\n• Fat: 7g\n• Carbs: 66g\n\n🥣 Great for sustained energy!'
            };
            
            return nutritionInfo[mentionedFood] || getGeneralNutritionAdvice();
        }
        
        return getGeneralNutritionAdvice();
    }
    
    // Motivation quotes
    if (lowerMessage.includes('motivation') || lowerMessage.includes('inspire') || lowerMessage.includes('quote')) {
        const quotes = [
            "💪 The only bad workout is the one that didn't happen!",
            "🌟 Your body can do it. It's your mind you need to convince.",
            "🔥 Don't stop when you're tired. Stop when you're done!",
            "⚡ Strength doesn't come from what you can do. It comes from overcoming what you once thought you couldn't.",
            "🏆 Success isn't given. It's earned in the gym!",
            "💯 Push yourself because no one else is going to do it for you.",
            "🎯 Champions train, losers complain.",
            "🚀 Believe in yourself and all that you are!",
            "💝 Take care of your body. It's the only place you have to live.",
            "🌱 Progress, not perfection!"
        ];
        return quotes[Math.floor(Math.random() * quotes.length)];
    }
    
    // Health tips
    if (lowerMessage.includes('health') || lowerMessage.includes('tips') || lowerMessage.includes('advice')) {
        const healthTips = [
            "💧 **Hydration:** Drink at least 8 glasses of water daily for optimal body function!",
            "😴 **Sleep:** Aim for 7-9 hours of quality sleep each night for recovery and energy!",
            "🥗 **Nutrition:** Eat a rainbow of fruits and vegetables for diverse nutrients!",
            "🧘‍♀️ **Stress Management:** Practice deep breathing or meditation for mental wellness!",
            "🚶‍♂️ **Movement:** Take regular breaks from sitting - your body will thank you!",
            "☀️ **Vitamin D:** Get some sunlight daily for bone health and mood!"
        ];
        return healthTips[Math.floor(Math.random() * healthTips.length)];
    }
    
    return "Hello! I'm your AI fitness coach. I can help you with:\n\n🏋️‍♀️ **Exercise recommendations** (try: 'chest exercises')\n🥗 **Nutrition information** (try: 'chicken nutrition')\n📊 **BMI calculations** (try: 'I am 170cm and 70kg')\n💪 **Motivational support** (try: 'motivate me')\n🏥 **Health tips** (try: 'health advice')\n\nWhat would you like to know?";
}

// Helper function for general nutrition advice
function getGeneralNutritionAdvice() {
    return "🥗 **General Nutrition Guidelines:**\n\n• **Protein:** 0.8-1g per kg body weight\n• **Vegetables:** 5-9 servings daily\n• **Water:** 8+ glasses per day\n• **Whole grains:** Choose over refined\n• **Healthy fats:** Nuts, avocado, olive oil\n• **Limit:** Processed foods and added sugars\n\n💡 **Remember:** Balance and variety are key!";
}

// Helper function to calculate BMI from text
function calculateBMIFromText(text) {
    const lowerText = text.toLowerCase();
    
    // Regex patterns for different formats
    const cmKgPattern = /(\d+\.?\d*)\s*cm.*?(\d+\.?\d*)\s*kg/;
    const heightWeightPattern = /(\d+\.?\d*)\s*(cm|centimeters).*?(\d+\.?\d*)\s*(kg|kilograms)/;
    const feetPoundsPattern = /(\d+)\s*feet?\s*(\d+)?\s*inches?.*?(\d+\.?\d*)\s*(pounds?|lbs)/;
    
    let height, weight, bmi, unit = 'metric';
    
    // Try cm/kg pattern
    let match = text.match(cmKgPattern) || text.match(heightWeightPattern);
    if (match) {
        height = parseFloat(match[1]) / 100; // convert cm to m
        weight = parseFloat(match[2]);
    } else {
        // Try feet/inches and pounds
        match = text.match(feetPoundsPattern);
        if (match) {
            const feet = parseInt(match[1]);
            const inches = match[2] ? parseInt(match[2]) : 0;
            height = (feet * 12 + inches) * 0.0254; // convert to meters
            weight = parseFloat(match[3]) * 0.453592; // convert lbs to kg
            unit = 'imperial';
        }
    }
    
    if (height && weight && height > 0 && weight > 0) {
        bmi = weight / (height * height);
        
        let category;
        if (bmi < 18.5) category = "Underweight";
        else if (bmi < 25) category = "Normal weight";
        else if (bmi < 30) category = "Overweight";
        else category = "Obese";
        
        return `**BMI Calculation Results:**\n\n📊 **Your BMI:** ${bmi.toFixed(1)}\n🎯 **Category:** ${category}\n\n**Health Advice:**\n${getBMIAdvice(category)}`;
    }
    
    return null;
}

// Helper function for BMI advice
function getBMIAdvice(category) {
    const advice = {
        "Underweight": "• Focus on nutrient-dense, calorie-rich foods\n• Include healthy fats and proteins\n• Consider consulting a nutritionist",
        "Normal weight": "• Maintain your current healthy lifestyle!\n• Continue balanced diet and regular exercise\n• Monitor changes over time",
        "Overweight": "• Focus on gradual, sustainable weight loss\n• Increase physical activity\n• Choose whole foods over processed",
        "Obese": "• Consider consulting healthcare professionals\n• Start with gentle, low-impact exercises\n• Focus on sustainable lifestyle changes"
    };
    
    return advice[category] || "Consult with healthcare professionals for personalized advice.";
}