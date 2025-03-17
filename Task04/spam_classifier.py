import pandas as pd
import numpy as np
import nltk
import string
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Download stopwords
nltk.download("stopwords")

# Load the dataset
df = pd.read_csv("SMSSpamCollection.csv", encoding="latin-1", sep="\t", header=None, names=["Label", "Text"])

# Convert labels to binary (Spam = 1, Ham (Not Spam) = 0)
df["Label"] = df["Label"].map({"spam": 1, "ham": 0})

# Function to clean text
def clean_text(text):
    text = text.lower()  # Convert to lowercase
    text = "".join([char for char in text if char not in string.punctuation])  # Remove punctuation
    text = " ".join([word for word in text.split() if word not in stopwords.words("english")])  # Remove stopwords
    return text

# Apply cleaning function
df["Cleaned_Text"] = df["Text"].apply(clean_text)

# Convert text to numerical data using TF-IDF Vectorizer
vectorizer = TfidfVectorizer(max_features=1000, ngram_range=(1,2), stop_words="english")
X = vectorizer.fit_transform(df["Cleaned_Text"])
y = df["Label"]

# Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Train Naïve Bayes model
model = MultinomialNB()
model.fit(X_train, y_train)

# Predict on test data
y_pred = model.predict(X_test)

# Print accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Improved Model Accuracy: {accuracy * 100:.2f}%")

# Test with a custom message
def predict_spam(message):
    message = clean_text(message)  # Preprocess input
    message_vector = vectorizer.transform([message])
    prediction = model.predict(message_vector)
    return "Spam" if prediction[0] == 1 else "Not Spam"

# Try a sample message
print(f"Test Message Prediction: {predict_spam('Win a free vacation!')}")
