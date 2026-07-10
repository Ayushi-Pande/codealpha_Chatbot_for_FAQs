from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify

from chatbot import PinguaAIChatbot
from analytics import AnalyticsManager

from datetime import datetime

import pandas as pd
import os

# ======================================================
# FLASK APP
# ======================================================

app = Flask(__name__)

# ======================================================
# INITIALIZE SERVICES
# ======================================================

chatbot = PinguaAIChatbot()

analytics = AnalyticsManager()

# ======================================================
# FILE PATHS
# ======================================================

UNKNOWN_QUESTIONS_FILE = (
    "data/unknown_questions.csv"
)

CHAT_HISTORY_FILE = (
    "data/chat_history.csv"
)

# ======================================================
# CREATE DATA FILES IF MISSING
# ======================================================

def ensure_data_files():

    os.makedirs(
        "data",
        exist_ok=True
    )

    if not os.path.exists(
        UNKNOWN_QUESTIONS_FILE
    ):

        pd.DataFrame(
            columns=[
                "timestamp",
                "question"
            ]
        ).to_csv(
            UNKNOWN_QUESTIONS_FILE,
            index=False
        )

    if not os.path.exists(
        CHAT_HISTORY_FILE
    ):

        pd.DataFrame(
            columns=[
                "timestamp",
                "user_message",
                "bot_response",
                "confidence",
                "sentiment"
            ]
        ).to_csv(
            CHAT_HISTORY_FILE,
            index=False
        )

ensure_data_files()

# ======================================================
# STORE UNKNOWN QUESTIONS
# ======================================================

def save_unknown_question(
    question
):

    try:

        new_entry = pd.DataFrame([
            {
                "timestamp":
                datetime.now(),

                "question":
                question
            }
        ])

        new_entry.to_csv(
            UNKNOWN_QUESTIONS_FILE,
            mode="a",
            header=False,
            index=False
        )

    except Exception as e:

        print(
            "Unknown Question Error:",
            e
        )

# ======================================================
# HOME PAGE
# ======================================================

@app.route("/")

def home():

    return render_template(
        "index.html"
    )

# ======================================================
# CHAT API
# ======================================================

@app.route(
    "/chat",
    methods=["POST"]
)

def chat():

    try:

        data = request.get_json()

        if not data:

            return jsonify({

                "answer":
                "Invalid request.",

                "confidence":
                0,

                "sentiment":
                "Neutral"

            }), 400

        user_message = (
            data.get(
                "message",
                ""
            ).strip()
        )

        if not user_message:

            return jsonify({

                "answer":
                "Please enter a question.",

                "confidence":
                0,

                "sentiment":
                "Neutral"

            })

        result = (
            chatbot.get_response(
                user_message
            )
        )

        answer = (
            result["answer"]
        )

        confidence = (
            result["confidence"]
        )

        sentiment = (
            result["sentiment"]
        )

        analytics.save_chat(

            user_message=
            user_message,

            bot_response=
            answer,

            confidence=
            confidence,

            sentiment=
            sentiment
        )

        if confidence < 35:

            save_unknown_question(
                user_message
            )

        return jsonify({

            "answer":
            answer,

            "confidence":
            confidence,

            "sentiment":
            sentiment

        })

    except Exception as e:

        print(
            "Chat API Error:",
            e
        )

        return jsonify({

            "answer":
            "Internal server error.",

            "confidence":
            0,

            "sentiment":
            "Neutral"

        }), 500

# ======================================================
# ANALYTICS API
# ======================================================

@app.route(
    "/analytics",
    methods=["GET"]
)

def analytics_dashboard():

    try:

        dashboard_data = (
            analytics.dashboard_summary()
        )

        return jsonify(
            dashboard_data
        )

    except Exception as e:

        print(
            "Analytics Error:",
            e
        )

        return jsonify({

            "total_conversations":
            0,

            "average_confidence":
            0,

            "sentiment_stats": {

                "Positive": 0,
                "Neutral": 0,
                "Negative": 0
            },

            "most_asked_questions":
            {}

        })

# ======================================================
# UNKNOWN QUESTIONS API
# ======================================================

@app.route(
    "/unknown-questions",
    methods=["GET"]
)

def unknown_questions():

    try:

        if not os.path.exists(
            UNKNOWN_QUESTIONS_FILE
        ):

            return jsonify([])

        df = pd.read_csv(
            UNKNOWN_QUESTIONS_FILE
        )

        questions = (
            df.tail(20)
            .to_dict(
                orient="records"
            )
        )

        return jsonify(
            questions
        )

    except Exception as e:

        print(
            "Unknown Questions Error:",
            e
        )

        return jsonify([])

# ======================================================
# HEALTH CHECK
# ======================================================

@app.route(
    "/health",
    methods=["GET"]
)

def health():

    return jsonify({

        "status":
        "running",

        "application":
        "PinguaAI InsightBot"

    })

# ======================================================
# ERROR HANDLERS
# ======================================================

@app.errorhandler(404)

def not_found(error):

    return jsonify({

        "error":
        "Page not found"

    }), 404

@app.errorhandler(500)

def server_error(error):

    return jsonify({

        "error":
        "Internal server error"

    }), 500

# ======================================================
# MAIN
# ======================================================

if __name__ == "__main__":

    app.run(

        host="0.0.0.0",

        port=5000,

        debug=True
    )
    