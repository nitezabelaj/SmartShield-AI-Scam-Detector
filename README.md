# 🛡️ SmartShield AI – Scam & Risk Message Detector

SmartShield AI is an intelligent message analysis system that detects scam and high-risk messages using Natural Language Processing (NLP) and Machine Learning.

The system analyzes text messages, assigns a risk score (0–100), classifies them as Safe, Suspicious, or High Risk, and provides an explanation for the decision.

---

##  Features

-  NLP Text Preprocessing
-  Machine Learning Classification (Logistic Regression)
-  Risk Scoring System (0–100)
-  Smart Classification:
  - Safe
  - Suspicious
  - High Risk
-  Explainable AI (Keyword-based explanation engine)
-  FastAPI REST API
-  Interactive Swagger UI
-  Modular & Scalable Architecture

---

##  How It Works

### 1. Text Preprocessing
- Lowercasing
- Removing URLs
- Removing special characters
- Stopword removal (NLTK)

### 2. Feature Extraction
- TF-IDF Vectorization

### 3. Machine Learning Model
- Logistic Regression
- Binary classification (Scam / Not Scam)

### 4. Risk Engine
- Converts probability into:
  - Risk Score (0–100)
  - Risk Category

### 5. Explanation Engine
- Detects suspicious keywords
- Provides human-readable explanation

---



## ⚙️ Installation

###   1. Clone the repository
git clone https://github.com/nitezabelaj/SmartShield-AI-Scam-Detector.git
cd SmartShield-AI-Scam-Detector

### 2. Install dependencies
pip install -r requirements.txt

If needed:

pip install fastapi uvicorn scikit-learn pandas numpy nltk

### ▶️ Run the Application
uvicorn main:app --reload

Server will start at:

http://127.0.0.1:8000

Swagger documentation:

http://127.0.0.1:8000/docs
### Example API Request
Endpoint
POST /analyze/
Example Input
#### Win free money now click urgent link
### Example Response
From JSON:
{
  "message": "Win free money now click urgent link",
  "risk_score": 85,
  "classification": "High Risk",
  "explanation": "Suspicious keywords detected: win, free, money"
}
### Technologies Used

Python 3.13

FastAPI

Uvicorn

Scikit-learn

Pandas

NumPy

NLTK
### 📊 Risk Classification Logic 
<img width="2212" height="835" alt="Screenshot (2729)" src="https://github.com/user-attachments/assets/6d5a0960-b21b-41df-82a0-e9438844e6f2" />

###  Future Improvements:

Use real-world scam dataset

Deploy to cloud (AWS / Azure / Render)

Add Frontend UI (React)

Integrate Deep Learning (LSTM / Transformer)

Chrome Extension Integration

Real-time email scanning

SHAP Explainable AI integration

### Use Cases

SMS scam detection

Email phishing detection

Customer support filtering

Social media content monitoring

Fraud detection systems
### License

This project is licensed under the MIT License.
You are free to use, modify, and distribute this project for educational and commercial purposes.



