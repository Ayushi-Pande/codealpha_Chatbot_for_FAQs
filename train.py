import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer

print("Loading FAQ Dataset...")

df = pd.read_csv("data/faq.csv")

questions = df["question"].tolist()

answers = df["answer"].tolist()

print("Training TF-IDF Model...")

vectorizer = TfidfVectorizer(
    stop_words="english",
    lowercase=True
)

vectors = vectorizer.fit_transform(
    questions
)

joblib.dump(
    vectorizer,
    "models/vectorizer.pkl"
)

joblib.dump(
    vectors,
    "models/question_vectors.pkl"
)

joblib.dump(
    questions,
    "models/questions.pkl"
)

joblib.dump(
    answers,
    "models/answers.pkl"
)

print("=" * 50)
print("PinguaAI Model Trained Successfully")
print("=" * 50)