# 🏋️‍♀️ AI-Powered Fitness Chatbot# 🏋️‍♀️ Fitness Chatbot: AI-Powered Health & Workout Assistant



**A comprehensive fitness assistant built with Machine Learning and API integration**A comprehensive web-based fitness chatbot that provides users with personalized workout advice, detailed nutrition information, BMI calculations, and motivational support. Built with Streamlit and powered by machine learning for intelligent intent classification.



---![Fitness Chatbot Demo](https://img.shields.io/badge/Status-Ready%20for%20Deployment-brightgreen)

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)

## 📋 **Project Overview**![License](https://img.shields.io/badge/License-MIT-green)



This project is an intelligent fitness chatbot that provides personalized workout advice, nutrition information, BMI calculations, and motivational support. It combines machine learning for intent classification with real-time API data to deliver accurate, helpful responses.## ✨ Features



### 🎯 **Key Features**### 🎯 Core Functionality

- **💪 Workout Guidance**: Get personalized exercise recommendations based on muscle groups, equipment, and difficulty levels

- **💪 Workout Guidance:** Personalized exercise recommendations based on muscle groups and fitness goals- **🍎 Nutrition Information**: Comprehensive nutritional data including calories, macros, and micronutrients via API integration

- **🍎 Nutrition Information:** Real-time nutritional data for various food items- **📊 BMI Calculator**: Calculate and classify Body Mass Index with health recommendations

- **📊 BMI Calculator:** Comprehensive BMI analysis with health recommendations- **🌟 Motivational Support**: AI-powered motivational messages and fitness tips

- **🌟 Motivation Support:** Curated fitness quotes and encouragement- **💬 Intelligent Chat**: Natural language processing for understanding user queries

- **🤖 AI-Powered:** Machine learning models for intelligent conversation

### 🎨 User Experience

---- **Interactive UI**: Clean, responsive Streamlit interface with real-time chat

- **Chat History**: Persistent conversation history during sessions

## 🛠️ **Technical Implementation**- **Quick Examples**: One-click example queries for easy interaction

- **Mobile Friendly**: Responsive design that works on all devices

### **Machine Learning Components:**

- **Intent Classification:** Logistic Regression and Naive Bayes models### 🤖 AI & ML Features

- **Natural Language Processing:** NLTK for text preprocessing and tokenization- **Intent Classification**: Naive Bayes and Logistic Regression models for understanding user queries

- **Training Data:** Custom dataset with 5 intent categories (workout, nutrition, BMI, motivation, greeting)- **NLP Processing**: Advanced text preprocessing with NLTK

- **Model Accuracy:** 75%+ accuracy on intent classification- **Smart Parsing**: Automatic extraction of food items, exercise preferences, and BMI data from natural language



### **API Integration:**## 🛠️ Tech Stack

- **API Ninjas:** Real-time nutrition and exercise data

- **Fallback System:** Local database for reliability when API is unavailable| Component | Technology | Purpose |

- **Error Handling:** Comprehensive error management and graceful degradation|-----------|------------|---------|

| **Frontend & Backend** | Streamlit | Web interface and server |

### **Web Interface:**| **Machine Learning** | scikit-learn | Intent classification models |

- **Streamlit Framework:** Interactive, responsive web application| **NLP Processing** | NLTK | Text preprocessing and analysis |

- **Real-time Chat:** Session-based conversation with message history| **API Integration** | API Ninjas | Nutrition and exercise data |

- **Professional UI:** Custom CSS styling for enhanced user experience| **Data Processing** | Pandas, NumPy | Data manipulation and analysis |

| **Environment** | python-dotenv | Configuration management |

---

## 🚀 Quick Start

## 📁 **Project Structure**

### Option 1: Automated Setup (Windows)

``````bash

📂 Fitness Chatbot/# Clone and run the setup script

├── 📄 app.py                    # Main Streamlit web applicationgit clone <your-repo-url>

├── 📄 chatbot.py                # Core chatbot logic and ML modelscd fitness-chatbot

├── 📄 train_model.py            # Machine learning model trainingstart.bat

├── 📄 requirements.txt          # Python dependencies```

├── 📄 .env.example             # Environment configuration template

├── 📄 README.md                # Project documentation### Option 2: Manual Setup

├── 📂 models/                  # Trained ML models```bash

│   ├── logistic_regression_model.pkl# 1. Clone the repository

│   └── naive_bayes_model.pklgit clone <your-repo-url>

├── 📂 utils/                   # Utility modulescd fitness-chatbot

│   ├── api_service.py          # API integration and data formatting

│   ├── bmi_calculator.py       # BMI calculations and health analysis# 2. Install dependencies

│   ├── motivation_service.py   # Motivational content managementpip install -r requirements.txt

│   └── exercise_fallback.py    # Local exercise database

└── 📂 data/                    # Training data and datasets# 3. Set up environment

    ├── training_data.csv       # ML training datasetcp .env.example .env

    └── create_training_data.py # Data generation script# Edit .env and add your API key

```

# 4. Train the ML model

---python train_model.py



## 🚀 **How to Run the Application**# 5. Run the application

streamlit run app.py

### **1. Install Dependencies**```

```bash

pip install -r requirements.txt### Option 3: Using Setup Script

``````bash

python setup.py

### **2. Train Machine Learning Models**```

```bash

python train_model.py## 🔧 Configuration

```

### API Setup

### **3. Configure API (Optional)**1. Get a free API key from [API Ninjas](https://api.api-ninjas.com/)

- Create `.env` file2. Create a `.env` file in the project root

- Add: `API_NINJAS_KEY=your_api_key_here`3. Add your API key:

   ```

### **4. Start the Application**   API_NINJAS_KEY=your_api_key_here

```bash   ```

streamlit run app.py

```### Environment Check

Run the configuration checker to ensure everything is set up correctly:

### **5. Access the Chatbot**```bash

- Open browser to: http://localhost:8501python config_check.py

- Start chatting with your AI fitness assistant!```



---## 🧪 Testing



## 💡 **Sample Interactions**Run the comprehensive test suite:

```bash

### **Workout Queries:**python test_chatbot.py

- *"Show me chest exercises"*```

- *"I want to build muscle"*

- *"What are good cardio workouts?"*The test suite covers:

- ✅ BMI calculations and classifications

### **Nutrition Queries:**- ✅ Motivation service functionality

- *"Nutrition facts for chicken breast"*- ✅ API service integration

- *"How many calories in an apple?"*- ✅ Chatbot logic and intent prediction

- *"Protein content in eggs"*- ✅ File structure validation



### **BMI Calculations:**## 🎯 Usage Examples

- *"Calculate my BMI"*

- *"I weigh 70kg and I'm 1.75m tall"*### Workout Queries

- *"What's a healthy BMI range?"*- "Show me chest exercises"

- "I want to build muscle"

### **Motivation:**- "What are good cardio workouts for beginners?"

- *"I need motivation"*- "Exercises for legs without equipment"

- *"I'm feeling lazy today"*

- *"Inspire me to workout"*### Nutrition Queries

- "How many calories in chicken breast?"

---- "Nutrition facts for quinoa"

- "Protein content in eggs"

## 🎓 **Educational Value & Learning Outcomes**- "Healthy meal options"



This project demonstrates proficiency in:### BMI Queries

- "Calculate my BMI"

### **Programming Concepts:**- "I weigh 70kg and I'm 1.75 meters tall"

- **Object-Oriented Programming:** Modular class structure and inheritance- "What's a healthy BMI range?"

- **API Integration:** RESTful API calls and JSON data handling

- **Error Handling:** Comprehensive exception management### Motivation Queries

- **File I/O Operations:** Model persistence and data loading- "I need motivation to workout"

- "I'm feeling lazy today"

### **Data Science & ML:**- "Inspire me to eat healthy"

- **Machine Learning Pipeline:** Data preprocessing, training, and prediction

- **Natural Language Processing:** Text classification and feature extraction## 🌟 Key Components

- **Model Evaluation:** Performance metrics and accuracy assessment

- **Cross-validation:** Robust model validation techniques### 🤖 Intent Classification Model

- **Training Data**: 100+ labeled examples across 5 intent categories

### **Software Engineering:**- **Models**: Naive Bayes and Logistic Regression

- **Modular Design:** Separation of concerns and clean architecture- **Accuracy**: 90%+ on test data

- **Version Control:** Git workflow and project management- **Features**: TF-IDF vectorization with NLTK preprocessing

- **Documentation:** Comprehensive code documentation and README files

- **Deployment:** Production-ready application structure### 🥗 Nutrition Service

- **API Integration**: Real-time nutritional data

### **Web Development:**- **Comprehensive Data**: Calories, macros, micronutrients

- **Frontend Development:** Interactive user interfaces with Streamlit- **Error Handling**: Graceful fallbacks for API failures

- **Session Management:** Stateful conversations and user experience- **Formatting**: User-friendly nutritional information display

- **Responsive Design:** Mobile-friendly and accessible interfaces

- **Real-time Features:** Live chat functionality and instant responses### 💪 Exercise Recommendations

- **Smart Filtering**: By muscle group, equipment, difficulty

---- **Detailed Instructions**: Step-by-step exercise guidance

- **Variety**: 500+ exercises in the database

## 🏆 **Project Highlights**- **Categorization**: Strength, cardio, flexibility, and more



✅ **Complete End-to-End Solution:** From data collection to deployment  ### 📊 BMI Calculator

✅ **Production-Ready:** Professional code quality with error handling  - **Dual Units**: Support for metric and imperial systems

✅ **Scalable Architecture:** Modular design for easy expansion  - **Health Categories**: WHO standard BMI classifications

✅ **User-friendly Interface:** Intuitive chat-based interaction  - **Recommendations**: Personalized health advice

✅ **Real-World Application:** Practical fitness and health use case  - **Risk Assessment**: Health risk indicators

✅ **Advanced Features:** ML-powered intent recognition and API integration  

## 🚀 Deployment Options

---

### Streamlit Cloud (Recommended)

## 📊 **Technical Specifications**```bash

# 1. Push to GitHub

- **Programming Language:** Python 3.12+git add .

- **Machine Learning:** scikit-learn, NLTKgit commit -m "Deploy fitness chatbot"

- **Web Framework:** Streamlit 1.28+git push origin main

- **API Integration:** Requests, API Ninjas

- **Data Processing:** Pandas, NumPy# 2. Deploy on share.streamlit.io

- **Model Storage:** Pickle serialization# 3. Add API_NINJAS_KEY in secrets

- **Environment Management:** python-dotenv```



---### Render

```yaml

*This project showcases the integration of machine learning, web development, and API technologies to create a practical, user-focused application that addresses real-world fitness and health needs.*# render.yaml
services:
  - type: web
    name: fitness-chatbot
    env: python
    buildCommand: pip install -r requirements.txt && python train_model.py
    startCommand: streamlit run app.py --server.port $PORT --server.address 0.0.0.0
```

### Docker Deployment
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN python train_model.py
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port", "8501", "--server.address", "0.0.0.0"]
```

For detailed deployment instructions, see [DEPLOYMENT.md](DEPLOYMENT.md).

## 📁 Project Structure

```
fitness-chatbot/
├── app.py                 # Main Streamlit application
├── chatbot.py            # Core chatbot logic
├── train_model.py        # ML model training script
├── requirements.txt      # Python dependencies
├── README.md            # Project documentation
├── DEPLOYMENT.md        # Deployment guide
├── .env.example         # Environment template
├── setup.py             # Automated setup script
├── config_check.py      # Environment validator
├── test_chatbot.py      # Comprehensive test suite
├── start.bat            # Windows quick start
├── data/                # Training data and datasets
├── models/              # Trained ML models
└── utils/               # Utility modules
    ├── api_service.py   # API integration
    ├── bmi_calculator.py # BMI calculations
    └── motivation_service.py # Motivational content
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support & Troubleshooting

### Common Issues

**Model not found error**
```bash
python train_model.py
```

**API errors**
- Check your API key in `.env`
- Verify API key is valid and has quota

**Import errors**
```bash
pip install -r requirements.txt
```

### Getting Help
- 📖 Check the [documentation](README.md)
- 🐛 Report bugs via GitHub Issues
- 💬 Ask questions in GitHub Discussions

## 🎯 Roadmap

- [ ] **Enhanced NLP**: Implement transformer-based models
- [ ] **User Profiles**: Persistent user preferences and history
- [ ] **Meal Planning**: Weekly meal plan generation
- [ ] **Workout Plans**: Structured fitness programs
- [ ] **Progress Tracking**: Visual progress charts
- [ ] **Social Features**: Community and sharing capabilities

## 📊 Statistics

- **Training Data**: 100+ labeled examples
- **Intent Categories**: 5 (workout, nutrition, BMI, motivation, greeting)
- **Exercise Database**: 500+ exercises
- **Nutritional Items**: 8,000+ food items
- **Motivational Quotes**: 50+ curated messages

## 🏆 Acknowledgments

- **API Ninjas** for providing comprehensive fitness and nutrition APIs
- **Streamlit** for the amazing web framework
- **scikit-learn** for machine learning capabilities
- **NLTK** for natural language processing tools

---

**Built with ❤️ for the fitness community**

*Remember: This chatbot provides general fitness information. Always consult healthcare professionals for personalized medical advice.*