# 🤖 PinguaAI InsightBot

> An AI-powered intelligent FAQ chatbot that uses Natural Language Processing, Semantic Search, Sentiment Analysis, and Machine Learning to provide context-aware answers and continuously improve through adaptive learning.

![Python](https://img.shields.io/badge/Python-3.12%2B-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-green)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-NLP-orange)
![Status](https://img.shields.io/badge/Status-Production%20Ready-success)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

# 📌 Overview

PinguaAI InsightBot is an intelligent FAQ assistant developed as part of the CodeAlpha Artificial Intelligence Internship Program.

Unlike traditional keyword-based chatbots, PinguaAI uses semantic understanding to identify user intent and provide relevant responses. The system also performs sentiment analysis, tracks analytics, supports voice interaction, and stores unanswered questions for future learning.

---

# ✨ Features

## 🧠 Artificial Intelligence Features

* Semantic FAQ Search
* Sentence Transformer Embeddings
* Cosine Similarity Matching
* Intent Understanding
* Confidence Score Prediction
* Sentiment Analysis
* Unknown Question Detection
* Adaptive Learning System

---

## 🌐 Frontend Features

* Professional Dashboard UI
* Responsive Design
* Dark and Light Theme
* Real-Time Chat Interface
* Suggested Questions
* Typing Indicator
* Voice Input
* Text-to-Speech Responses
* Export Chat Feature
* Mobile-Friendly Layout

---

## 📊 Analytics Features

* Total Conversations Tracking
* Average Confidence Monitoring
* Sentiment Statistics
* Most Asked Questions
* Chat History Logging
* Dashboard Insights

---

# 🏗️ Project Architecture

User Question

↓

Text Preprocessing

↓

Sentence Embedding Generation

↓

Cosine Similarity Search

↓

Best Match Selection

↓

Confidence Calculation

↓

Sentiment Analysis

↓

Response Generation

↓

Analytics Logging

↓

Adaptive Learning

---

# 📁 Project Structure

CodeAlpha_PinguaAI_InsightBot/

├── app.py

├── chatbot.py

├── train.py

├── analytics.py

├── requirements.txt

├── README.md

│

├── data/

│ ├── faq.csv

│ ├── chat_history.csv

│ └── unknown_questions.csv

│

├── models/

│ ├── faq_embeddings.pkl

│ ├── questions.pkl

│ └── answers.pkl

│

├── templates/

│ └── index.html

│

└── static/

├── css/

│ └── style.css

│

└── js/

└── app.js

---

# ⚙️ Installation

## Clone Repository

```bash
git clone <repository-url>
cd codealpha_Chatbot_for_FAQs
```

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🚀 Train the AI Model

Generate semantic embeddings:

```bash
python train.py
```

Generated files:

models/

├── faq_embeddings.pkl

├── questions.pkl

└── answers.pkl

---

# ▶️ Run the Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

# 🎙️ Voice Features

## Voice Input

Users can ask questions through speech recognition.

## Text-to-Speech

PinguaAI can read responses aloud using browser speech synthesis.

---

# 🧠 Adaptive Learning System

When the chatbot cannot confidently answer a question:

* The question is automatically stored.
* Administrators can review unanswered queries.
* The FAQ dataset can be updated.
* The model can be retrained to improve performance.

This enables continuous improvement of the chatbot.

---

# 📊 Analytics Dashboard

The dashboard provides:

* Total Conversations
* Average Confidence Score
* Positive Sentiments
* Neutral Sentiments
* Negative Sentiments
* Most Frequently Asked Questions

---

# 🛠️ Technologies Used

## Programming Languages

* Python
* JavaScript
* HTML5
* CSS3

## Backend

* Flask

## Artificial Intelligence & NLP

* Sentence Transformers
* Transformers
* Scikit-Learn
* NLTK
* TextBlob

## Data Processing

* Pandas
* NumPy
* Joblib

## Frontend

* HTML5
* CSS3
* JavaScript
* Font Awesome

---

# 🔮 Future Enhancements

* Multilingual Translation Support
* Database Integration
* User Authentication
* Admin Dashboard
* Real-Time Learning Pipeline
* Cloud Deployment
* AI Intent Classification
* REST API Integration
* Advanced Knowledge Management

---

# 🎯 Learning Outcomes

This project demonstrates:

* Natural Language Processing
* Semantic Search
* Machine Learning Workflows
* Data Analytics
* Flask API Development
* Frontend-Backend Integration
* Software Engineering Best Practices
* Production-Level Project Structure

---

# 🏆 CodeAlpha Artificial Intelligence Internship

Task Completed:

**Task 2 – Chatbot for FAQs**

Objective:

Build an intelligent FAQ chatbot capable of understanding user queries and returning the most relevant responses using Natural Language Processing and Machine Learning techniques.

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

Name: Ayushi Pandey

GitHub: https://github.com/Ayushi-Pande

LinkedIn: _______________________

Email: ayushipande222161@gmail.com

---

⭐ If you found this project useful, consider giving the repository a star.
