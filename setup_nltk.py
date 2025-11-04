import nltk
import os

def setup_nltk():
    """Download required NLTK data"""
    try:
        # Create nltk_data directory if it doesn't exist
        nltk_data_path = '/tmp/nltk_data'
        if not os.path.exists(nltk_data_path):
            os.makedirs(nltk_data_path)
        
        # Set NLTK data path
        nltk.data.path.append(nltk_data_path)
        
        # Download required NLTK data
        downloads = [
            'punkt',
            'stopwords',
            'wordnet',
            'averaged_perceptron_tagger',
            'omw-1.4'
        ]
        
        for item in downloads:
            try:
                nltk.download(item, download_dir=nltk_data_path, quiet=True)
            except Exception as e:
                print(f"Warning: Could not download {item}: {e}")
                
        return True
    except Exception as e:
        print(f"Error setting up NLTK: {e}")
        return False

if __name__ == "__main__":
    setup_nltk()