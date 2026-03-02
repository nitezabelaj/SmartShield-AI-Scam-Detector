import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from preprocessing import clean_text

vectorizer = TfidfVectorizer()
model = LogisticRegression()

def train_model():
    data = {
        "text": [
            "Win money now",
            "Click this link urgent",
            "Hello how are you",
            "Meeting tomorrow at 10"
        ],
        "label": [1, 1, 0, 0]
    }

    df = pd.DataFrame(data)
    df["text"] = df["text"].apply(clean_text)

    X = vectorizer.fit_transform(df["text"])
    y = df["label"]

    model.fit(X, y)

def predict(message):
    cleaned = clean_text(message)
    X = vectorizer.transform([cleaned])
    prob = model.predict_proba(X)[0][1]
    return prob