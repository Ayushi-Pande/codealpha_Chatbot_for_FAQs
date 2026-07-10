import pandas as pd
from datetime import datetime
import os


CHAT_HISTORY_FILE = "data/chat_history.csv"


class AnalyticsManager:

    def __init__(self):
        self.ensure_files_exist()

    def ensure_files_exist(self):

        if not os.path.exists(CHAT_HISTORY_FILE):

            df = pd.DataFrame(
                columns=[
                    "timestamp",
                    "user_message",
                    "bot_response",
                    "confidence",
                    "sentiment"
                ]
            )

            df.to_csv(
                CHAT_HISTORY_FILE,
                index=False
            )

    def save_chat(
        self,
        user_message,
        bot_response,
        confidence,
        sentiment
    ):

        new_data = pd.DataFrame(
            [{
                "timestamp": datetime.now(),
                "user_message": user_message,
                "bot_response": bot_response,
                "confidence": confidence,
                "sentiment": sentiment
            }]
        )

        new_data.to_csv(
            CHAT_HISTORY_FILE,
            mode="a",
            header=False,
            index=False
        )

    def total_conversations(self):

        try:

            df = pd.read_csv(
                CHAT_HISTORY_FILE
            )

            return len(df)

        except:

            return 0

    def average_confidence(self):

        try:

            df = pd.read_csv(
                CHAT_HISTORY_FILE
            )

            if len(df) == 0:
                return 0

            return round(
                df["confidence"].mean(),
                2
            )

        except:

            return 0

    def sentiment_statistics(self):

        try:

            df = pd.read_csv(
                CHAT_HISTORY_FILE
            )

            if len(df) == 0:

                return {
                    "Positive": 0,
                    "Neutral": 0,
                    "Negative": 0
                }

            result = (
                df["sentiment"]
                .value_counts()
                .to_dict()
            )

            return {
                "Positive": result.get(
                    "Positive",
                    0
                ),
                "Neutral": result.get(
                    "Neutral",
                    0
                ),
                "Negative": result.get(
                    "Negative",
                    0
                )
            }

        except:

            return {
                "Positive": 0,
                "Neutral": 0,
                "Negative": 0
            }

    def most_asked_questions(
        self,
        limit=5
    ):

        try:

            df = pd.read_csv(
                CHAT_HISTORY_FILE
            )

            top_questions = (
                df["user_message"]
                .value_counts()
                .head(limit)
                .to_dict()
            )

            return top_questions

        except:

            return {}

    def dashboard_summary(self):

        return {

            "total_conversations":
                self.total_conversations(),

            "average_confidence":
                self.average_confidence(),

            "sentiment_stats":
                self.sentiment_statistics(),

            "most_asked_questions":
                self.most_asked_questions()
        }