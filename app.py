import streamlit as st
import os
from datetime import datetime
from dotenv import load_dotenv
from chatbot import FitnessChatbot

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Fitness Chatbot - AI Health Assistant",
    page_icon="💪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #FF6B6B;
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .sub-header {
        text-align: center;
        color: #4ECDC4;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .user-message {
        background-color: #E3F2FD;
        border-left: 4px solid #2196F3;
    }
    .bot-message {
        background-color: #F3E5F5;
        border-left: 4px solid #9C27B0;
    }
    .feature-box {
        background-color: #F8F9FA;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #28A745;
        margin: 0.5rem 0;
    }
    .warning-box {
        background-color: #FFF3CD;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #FFC107;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

def initialize_session_state():
    """Initialize session state variables"""
    if 'chatbot' not in st.session_state:
        st.session_state.chatbot = FitnessChatbot()
    
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    
    if 'api_key_configured' not in st.session_state:
        st.session_state.api_key_configured = bool(os.getenv('API_NINJAS_KEY'))

def display_header():
    """Display the main header"""
    st.markdown('<h1 class="main-header">🏋️‍♀️ Fitness Chatbot</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Your AI-Powered Health & Workout Assistant</p>', unsafe_allow_html=True)

def display_sidebar():
    """Display the sidebar with features and settings"""
    with st.sidebar:
        st.header("🚀 Features")
        
        features = [
            ("💪", "Workout Guidance", "Get personalized exercise recommendations"),
            ("🍎", "Nutrition Info", "Learn about calories and nutrients"),
            ("📊", "BMI Calculator", "Calculate and analyze your BMI"),
            ("🌟", "Motivation", "Receive inspiring fitness quotes")
        ]
        
        for icon, title, description in features:
            st.markdown(f"""
            <div class="feature-box">
                <h4>{icon} {title}</h4>
                <p>{description}</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.header("⚙️ Settings")
        
        # API Key status
        if st.session_state.api_key_configured:
            st.success("✅ API Key Configured")
        else:
            st.error("❌ API Key Not Configured")
            st.markdown("""
            <div class="warning-box">
                <strong>⚠️ API Setup Required</strong><br>
                To use nutrition and exercise features, please:
                <ol>
                    <li>Get a free API key from <a href="https://api.api-ninjas.com/" target="_blank">API Ninjas</a></li>
                    <li>Create a <code>.env</code> file in your project directory</li>
                    <li>Add: <code>API_NINJAS_KEY=your_api_key_here</code></li>
                </ol>
            </div>
            """, unsafe_allow_html=True)
        
        # Clear chat history
        if st.button("🗑️ Clear Chat History"):
            st.session_state.chat_history = []
            st.rerun()
        
        # Model status
        st.header("🤖 Model Status")
        if st.session_state.chatbot.model:
            st.success("✅ ML Model Loaded")
        else:
            st.error("❌ ML Model Not Found")
            st.info("Run `python train_model.py` to train the model first.")
        
        # Usage tips
        st.header("💡 Usage Tips")
        st.markdown("""
        **Try asking:**
        - "Show me chest exercises"
        - "Calories in chicken breast"
        - "Calculate my BMI - I weigh 70kg and I'm 1.75m tall"
        - "I need motivation"
        - "What are good cardio workouts?"
        """)

def display_chat_history():
    """Display the chat history"""
    if not st.session_state.chat_history:
        st.info("👋 Welcome! Ask me anything about fitness, nutrition, BMI, or get some motivation!")
        return
    
    for i, (user_msg, bot_msg, timestamp) in enumerate(st.session_state.chat_history):
        # User message
        st.markdown(f'<div class="chat-message user-message"><strong>🧑 You ({timestamp}):</strong></div>', unsafe_allow_html=True)
        st.markdown(user_msg)
        
        # Bot message  
        st.markdown(f'<div class="chat-message bot-message"><strong>🤖 Fitness Bot:</strong></div>', unsafe_allow_html=True)
        st.markdown(bot_msg)

def handle_user_input():
    """Handle user input and generate bot response"""
    user_input = st.session_state.user_input
    
    if user_input:
        # Get current timestamp
        timestamp = datetime.now().strftime("%H:%M")
        
        # Process the message
        bot_response = st.session_state.chatbot.process_message(user_input)
        
        # Add to chat history
        st.session_state.chat_history.append((user_input, bot_response, timestamp))

def process_example_input(example_text):
    """Process example input from buttons"""
    # Get current timestamp
    timestamp = datetime.now().strftime("%H:%M")
    
    # Process the message
    bot_response = st.session_state.chatbot.process_message(example_text)
    
    # Add to chat history
    st.session_state.chat_history.append((example_text, bot_response, timestamp))

def display_examples():
    """Display example queries"""
    st.header("🎯 Try These Examples")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("💪 Workout Queries")
        workout_examples = [
            "Show me chest exercises",
            "I want to build muscle",
            "What are good cardio workouts?",
            "Exercises for beginners"
        ]
        for example in workout_examples:
            if st.button(f"💪 {example}", key=f"workout_{example}"):
                process_example_input(example)
                st.rerun()
        
        st.subheader("📊 BMI Queries")
        bmi_examples = [
            "Calculate my BMI",
            "I weigh 70kg and I'm 1.75m tall",
            "What is a healthy BMI range?"
        ]
        for example in bmi_examples:
            if st.button(f"📊 {example}", key=f"bmi_{example}"):
                process_example_input(example)
                st.rerun()
    
    with col2:
        st.subheader("🍎 Nutrition Queries")
        nutrition_examples = [
            "Calories in chicken breast",
            "Nutrition facts for apple",
            "Protein content in eggs"
        ]
        for example in nutrition_examples:
            if st.button(f"🍎 {example}", key=f"nutrition_{example}"):
                process_example_input(example)
                st.rerun()
        
        st.subheader("🌟 Motivation Queries")
        motivation_examples = [
            "I need motivation",
            "I'm feeling lazy today",
            "Inspire me to workout"
        ]
        for example in motivation_examples:
            if st.button(f"🌟 {example}", key=f"motivation_{example}"):
                process_example_input(example)
                st.rerun()

def main():
    """Main application function"""
    # Initialize session state
    initialize_session_state()
    
    # Display header
    display_header()
    
    # Display sidebar
    display_sidebar()
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("💬 Chat")
        
        # Chat input
        st.text_input(
            "Ask me anything about fitness, nutrition, BMI, or motivation:",
            key="user_input",
            on_change=handle_user_input,
            placeholder="Type your message here... (e.g., 'Show me chest exercises')"
        )
        
        # Display chat history
        display_chat_history()
    
    with col2:
        # Display examples
        display_examples()
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; padding: 1rem;">
        <p>🏋️‍♀️ <strong>Fitness Chatbot</strong> - Built with Streamlit, scikit-learn, and API Ninjas</p>
        <p>💡 <em>Remember: This chatbot provides general fitness information. Always consult healthcare professionals for personalized advice.</em></p>
    </div>
    """, unsafe_allow_html=True)

# For Vercel deployment
def handler(request):
    main()

if __name__ == "__main__":
    main()