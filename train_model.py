import pandas as pd
import numpy as np
import pickle
import nltk
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.pipeline import Pipeline
import os

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab')

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet')

try:
    nltk.data.find('corpora/omw-1.4')
except LookupError:
    nltk.download('omw-1.4')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

class IntentClassifier:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
        self.vectorizer = TfidfVectorizer(max_features=1000, lowercase=True, stop_words='english')
        self.naive_bayes_model = MultinomialNB()
        self.logistic_model = LogisticRegression(random_state=42, max_iter=1000)
        self.nb_pipeline = None
        self.lr_pipeline = None
        
    def preprocess_text(self, text):
        """Preprocess text by tokenizing, removing stopwords, and lemmatizing"""
        # Convert to lowercase
        text = text.lower()
        
        # Tokenize
        tokens = word_tokenize(text)
        
        # Remove stopwords and lemmatize
        tokens = [self.lemmatizer.lemmatize(token) for token in tokens 
                 if token.isalnum() and token not in self.stop_words]
        
        return ' '.join(tokens)
    
    def create_training_data(self):
        """Create and save training data"""
        # Training data for intent classification
        training_data = [
            # Workout/Exercise intents
            ("show me chest exercises", "workout"),
            ("what are good arm workouts", "workout"),
            ("I want to build muscle", "workout"),
            ("exercises for legs", "workout"),
            ("how to lose weight", "workout"),
            ("cardio workouts", "workout"),
            ("strength training", "workout"),
            ("yoga poses", "workout"),
            ("abs workout", "workout"),
            ("back exercises", "workout"),
            ("bicep workouts", "workout"),
            ("tricep exercises", "workout"),
            ("shoulder workout", "workout"),
            ("glute exercises", "workout"),
            ("calf workouts", "workout"),
            ("full body workout", "workout"),
            ("home workouts", "workout"),
            ("gym exercises", "workout"),
            ("push ups", "workout"),
            ("squats", "workout"),
            ("deadlifts", "workout"),
            ("bench press", "workout"),
            ("running exercises", "workout"),
            ("swimming workout", "workout"),
            ("cycling training", "workout"),
            ("HIIT workout", "workout"),
            ("beginner exercises", "workout"),
            ("advanced workouts", "workout"),
            ("morning workout", "workout"),
            ("evening exercises", "workout"),
            
            # Nutrition intents
            ("calories in apple", "nutrition"),
            ("nutrition facts for chicken", "nutrition"),
            ("how much protein in eggs", "nutrition"),
            ("carbs in rice", "nutrition"),
            ("healthy food options", "nutrition"),
            ("diet plan", "nutrition"),
            ("nutrition information", "nutrition"),
            ("calories in banana", "nutrition"),
            ("protein content", "nutrition"),
            ("fat content in avocado", "nutrition"),
            ("sugar in fruits", "nutrition"),
            ("vitamins in vegetables", "nutrition"),
            ("meal calories", "nutrition"),
            ("food nutrition", "nutrition"),
            ("healthy eating", "nutrition"),
            ("calorie count", "nutrition"),
            ("nutritional value", "nutrition"),
            ("macro nutrients", "nutrition"),
            ("micro nutrients", "nutrition"),
            ("daily calorie intake", "nutrition"),
            ("protein requirements", "nutrition"),
            ("carbohydrate needs", "nutrition"),
            ("fat intake", "nutrition"),
            ("fiber content", "nutrition"),
            ("calcium in milk", "nutrition"),
            ("iron in spinach", "nutrition"),
            ("sodium content", "nutrition"),
            ("cholesterol levels", "nutrition"),
            ("antioxidants in berries", "nutrition"),
            ("omega 3 fatty acids", "nutrition"),
            
            # BMI intents
            ("calculate my BMI", "bmi"),
            ("what is BMI", "bmi"),
            ("body mass index", "bmi"),
            ("am I overweight", "bmi"),
            ("healthy weight", "bmi"),
            ("BMI calculator", "bmi"),
            ("check my weight status", "bmi"),
            ("ideal weight", "bmi"),
            ("weight category", "bmi"),
            ("underweight or overweight", "bmi"),
            ("body weight analysis", "bmi"),
            ("weight assessment", "bmi"),
            ("height weight ratio", "bmi"),
            ("weight classification", "bmi"),
            ("obesity check", "bmi"),
            ("normal weight range", "bmi"),
            ("weight evaluation", "bmi"),
            ("health weight status", "bmi"),
            ("BMI range", "bmi"),
            ("weight index", "bmi"),
            
            # Motivation intents
            ("I need motivation", "motivation"),
            ("encourage me", "motivation"),
            ("fitness motivation", "motivation"),
            ("I'm feeling lazy", "motivation"),
            ("inspire me", "motivation"),
            ("motivational quote", "motivation"),
            ("keep me going", "motivation"),
            ("I want to give up", "motivation"),
            ("boost my confidence", "motivation"),
            ("positive message", "motivation"),
            ("cheer me up", "motivation"),
            ("I'm tired", "motivation"),
            ("struggling with fitness", "motivation"),
            ("need encouragement", "motivation"),
            ("feeling demotivated", "motivation"),
            ("help me stay focused", "motivation"),
            ("losing motivation", "motivation"),
            ("fitness inspiration", "motivation"),
            ("workout motivation", "motivation"),
            ("diet motivation", "motivation"),
            ("health inspiration", "motivation"),
            ("success stories", "motivation"),
            ("fitness goals", "motivation"),
            ("stay committed", "motivation"),
            ("overcome laziness", "motivation"),
            ("push through", "motivation"),
            ("don't quit", "motivation"),
            ("believe in yourself", "motivation"),
            ("you can do it", "motivation"),
            ("never give up", "motivation"),
            
            # Greeting intents
            ("hello", "greeting"),
            ("hi", "greeting"),
            ("hey", "greeting"),
            ("good morning", "greeting"),
            ("good evening", "greeting"),
            ("howdy", "greeting"),
            ("what's up", "greeting"),
            ("how are you", "greeting"),
            ("greetings", "greeting"),
            ("nice to meet you", "greeting"),
        ]
        
        # Create DataFrame
        df = pd.DataFrame(training_data, columns=['text', 'intent'])
        
        # Save to CSV
        df.to_csv('data/training_data.csv', index=False)
        
        return df
    
    def train_models(self, df):
        """Train both Naive Bayes and Logistic Regression models"""
        # Preprocess text data
        df['processed_text'] = df['text'].apply(self.preprocess_text)
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            df['processed_text'], df['intent'], test_size=0.2, random_state=42, stratify=df['intent']
        )
        
        # Create pipelines
        self.nb_pipeline = Pipeline([
            ('tfidf', TfidfVectorizer(max_features=1000, lowercase=True, stop_words='english')),
            ('nb', MultinomialNB())
        ])
        
        self.lr_pipeline = Pipeline([
            ('tfidf', TfidfVectorizer(max_features=1000, lowercase=True, stop_words='english')),
            ('lr', LogisticRegression(random_state=42, max_iter=1000))
        ])
        
        # Train models
        print("Training Naive Bayes model...")
        self.nb_pipeline.fit(X_train, y_train)
        
        print("Training Logistic Regression model...")
        self.lr_pipeline.fit(X_train, y_train)
        
        # Evaluate models
        nb_pred = self.nb_pipeline.predict(X_test)
        lr_pred = self.lr_pipeline.predict(X_test)
        
        print(f"\nNaive Bayes Accuracy: {accuracy_score(y_test, nb_pred):.3f}")
        print(f"Logistic Regression Accuracy: {accuracy_score(y_test, lr_pred):.3f}")
        
        print("\nNaive Bayes Classification Report:")
        print(classification_report(y_test, nb_pred))
        
        print("\nLogistic Regression Classification Report:")
        print(classification_report(y_test, lr_pred))
        
        return X_test, y_test
    
    def save_models(self):
        """Save trained models"""
        os.makedirs('models', exist_ok=True)
        
        with open('models/naive_bayes_model.pkl', 'wb') as f:
            pickle.dump(self.nb_pipeline, f)
            
        with open('models/logistic_regression_model.pkl', 'wb') as f:
            pickle.dump(self.lr_pipeline, f)
            
        print("Models saved successfully!")
    
    def load_models(self):
        """Load trained models"""
        try:
            with open('models/naive_bayes_model.pkl', 'rb') as f:
                self.nb_pipeline = pickle.load(f)
                
            with open('models/logistic_regression_model.pkl', 'rb') as f:
                self.lr_pipeline = pickle.load(f)
                
            print("Models loaded successfully!")
            return True
        except FileNotFoundError:
            print("Model files not found. Please train the models first.")
            return False
    
    def predict_intent(self, text, model_type='logistic'):
        """Predict intent for given text"""
        processed_text = self.preprocess_text(text)
        
        if model_type == 'naive_bayes' and self.nb_pipeline:
            prediction = self.nb_pipeline.predict([processed_text])[0]
            confidence = max(self.nb_pipeline.predict_proba([processed_text])[0])
        elif model_type == 'logistic' and self.lr_pipeline:
            prediction = self.lr_pipeline.predict([processed_text])[0]
            confidence = max(self.lr_pipeline.predict_proba([processed_text])[0])
        else:
            return "unknown", 0.0
            
        return prediction, confidence

def main():
    classifier = IntentClassifier()
    
    # Create training data
    print("Creating training data...")
    df = classifier.create_training_data()
    print(f"Training data created with {len(df)} samples")
    print("Intent distribution:")
    print(df['intent'].value_counts())
    
    # Train models
    print("\nTraining models...")
    X_test, y_test = classifier.train_models(df)
    
    # Save models
    classifier.save_models()
    
    # Test predictions
    print("\nTesting predictions:")
    test_texts = [
        "I want to do push ups",
        "How many calories in chicken breast",
        "Calculate my body mass index",
        "I need some motivation",
        "Hello there"
    ]
    
    for text in test_texts:
        intent_nb, conf_nb = classifier.predict_intent(text, 'naive_bayes')
        intent_lr, conf_lr = classifier.predict_intent(text, 'logistic')
        print(f"Text: '{text}'")
        print(f"  Naive Bayes: {intent_nb} (confidence: {conf_nb:.3f})")
        print(f"  Logistic Regression: {intent_lr} (confidence: {conf_lr:.3f})")
        print()

if __name__ == "__main__":
    main()