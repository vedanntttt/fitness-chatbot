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
        // Call backend API
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
        addMessage('bot', 'Sorry, I\'m having trouble connecting right now. Please check your internet connection and try again.');
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

// Fallback for when backend is not available
async function getFallbackResponse(message) {
    const lowerMessage = message.toLowerCase();
    
    // Simple keyword-based responses
    if (lowerMessage.includes('exercise') || lowerMessage.includes('workout')) {
        return "Here are some great exercises you can try:\n\n1. **Push-ups** - Great for chest and arms\n2. **Squats** - Perfect for legs and glutes\n3. **Planks** - Excellent for core strength\n4. **Burpees** - Full body cardio workout\n\nRemember to start slowly and maintain proper form!";
    }
    
    if (lowerMessage.includes('nutrition') || lowerMessage.includes('diet')) {
        return "Here's some general nutrition advice:\n\n• **Eat plenty of vegetables** - Aim for colorful variety\n• **Choose lean proteins** - Chicken, fish, beans, tofu\n• **Include whole grains** - Brown rice, quinoa, oats\n• **Stay hydrated** - Drink at least 8 glasses of water daily\n• **Limit processed foods** - Focus on whole, natural foods\n\nRemember: A balanced diet is key to good health!";
    }
    
    if (lowerMessage.includes('bmi') || lowerMessage.includes('weight')) {
        return "To calculate your BMI, I need your height and weight. \n\nBMI Formula: BMI = weight (kg) / height (m)²\n\n**BMI Categories:**\n• Underweight: Below 18.5\n• Normal weight: 18.5-24.9\n• Overweight: 25-29.9\n• Obese: 30 and above\n\nPlease provide your measurements like: 'I am 170 cm tall and weigh 70 kg'";
    }
    
    if (lowerMessage.includes('motivation') || lowerMessage.includes('inspire')) {
        const quotes = [
            "💪 The only bad workout is the one that didn't happen!",
            "🌟 Your body can do it. It's your mind you need to convince.",
            "🔥 Don't stop when you're tired. Stop when you're done!",
            "⚡ Strength doesn't come from what you can do. It comes from overcoming what you once thought you couldn't.",
            "🏆 Success isn't given. It's earned in the gym!"
        ];
        return quotes[Math.floor(Math.random() * quotes.length)];
    }
    
    return "I'm here to help with fitness, nutrition, and health questions! Try asking me about:\n\n• Exercise recommendations\n• Nutrition advice\n• BMI calculations\n• Motivational quotes\n• General health tips\n\nWhat would you like to know?";
}