import streamlit as st
import os
from datetime import datetime
from dotenv import load_dotenv
from chatbot_vercel import FitnessChatbot

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
        margin: 0.5rem 0;
        border-left: 4px solid #28A745;
    }
    .stButton > button {
        background-color: #FF6B6B;
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.5rem 1rem;
        font-weight: bold;
        transition: all 0.3s;
    }
    .stButton > button:hover {
        background-color: #FF5252;
        transform: translateY(-2px);
    }
</style>
""", unsafe_allow_html=True)

def initialize_chatbot():
    """Initialize the chatbot"""
    if 'chatbot' not in st.session_state:
        st.session_state.chatbot = FitnessChatbot()
    return st.session_state.chatbot

def initialize_session_state():
    """Initialize session state variables"""
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    if 'user_profile' not in st.session_state:
        st.session_state.user_profile = {}

def display_chat_history():
    """Display the chat history"""
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f"""
            <div class="chat-message user-message">
                <strong>You:</strong> {message["content"]}
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="chat-message bot-message">
                <strong>🤖 Fitness Coach:</strong> {message["content"]}
            </div>
            """, unsafe_allow_html=True)

def display_examples():
    """Display example queries"""
    st.markdown("""
    <div class="feature-box">
        <h4>💡 Try asking me about:</h4>
        <ul>
            <li>🏋️‍♀️ "Show me chest exercises"</li>
            <li>🥗 "What's the nutrition of chicken?"</li>
            <li>📊 "Calculate my BMI - I'm 170cm and 70kg"</li>
            <li>💪 "Give me motivation"</li>
            <li>🏃‍♂️ "I need a cardio workout"</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

def display_features():
    """Display chatbot features"""
    st.markdown("""
    <div class="feature-box">
        <h4>🚀 Features:</h4>
        <ul>
            <li>🎯 Exercise Recommendations</li>
            <li>🍎 Nutrition Information</li>
            <li>📏 BMI Calculator</li>
            <li>💝 Motivational Support</li>
            <li>🏥 General Health Tips</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

def sidebar_content():
    """Display sidebar content"""
    with st.sidebar:
        st.markdown("### 🎯 Quick Actions")
        
        # Quick action buttons
        if st.button("💪 Get Exercise Tips", use_container_width=True):
            return "Give me some exercise recommendations"
        
        if st.button("🥗 Nutrition Advice", use_container_width=True):
            return "Give me nutrition advice"
        
        if st.button("📊 Calculate BMI", use_container_width=True):
            return "I want to calculate my BMI"
        
        if st.button("🌟 Get Motivated", use_container_width=True):
            return "Give me some motivation"
        
        if st.button("🔄 Clear Chat", use_container_width=True):
            st.session_state.messages = []
            st.experimental_rerun()
        
        st.markdown("---")
        display_features()
        
    return None

def main():
    """Main application function"""
    # Initialize session state and chatbot
    initialize_session_state()
    chatbot = initialize_chatbot()
    
    # Header
    st.markdown('<h1 class="main-header">🏋️‍♀️ AI Fitness Coach</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Your Personal Health & Fitness Assistant</p>', unsafe_allow_html=True)
    
    # Sidebar
    sidebar_action = sidebar_content()
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 💬 Chat with Your Fitness Coach")
        
        # Handle sidebar actions
        if sidebar_action:
            # Add user message
            st.session_state.messages.append({"role": "user", "content": sidebar_action})
            
            # Generate bot response
            with st.spinner("🤔 Thinking..."):
                response = chatbot.generate_response(sidebar_action)
            
            # Add bot response
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.experimental_rerun()
        
        # Chat input
        user_input = st.chat_input("Ask me anything about fitness, nutrition, or health!")
        
        if user_input:
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": user_input})
            
            # Generate response
            with st.spinner("🤔 Thinking..."):
                response = chatbot.generate_response(user_input)
            
            # Add bot response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response})
            
            # Rerun to update the display
            st.experimental_rerun()
        
        # Display chat history
        display_chat_history()
    
    with col2:
        # Display examples
        display_examples()
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; padding: 1rem;">
        <p>🏋️‍♀️ <strong>Fitness Chatbot</strong> - Built with Streamlit and API Ninjas</p>
        <p>💡 <em>Remember: This chatbot provides general fitness information. Always consult healthcare professionals for personalized advice.</em></p>
    </div>
    """, unsafe_allow_html=True)

# For Vercel deployment
def handler(request):
    main()

if __name__ == "__main__":
    main()