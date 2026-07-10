import joblib

from textblob import TextBlob

from sklearn.metrics.pairwise import cosine_similarity


class PinguaAIChatbot:

    def __init__(self):

        self.vectorizer = joblib.load(
            "models/vectorizer.pkl"
        )

        self.question_vectors = joblib.load(
            "models/question_vectors.pkl"
        )

        self.questions = joblib.load(
            "models/questions.pkl"
        )

        self.answers = joblib.load(
            "models/answers.pkl"
        )

    def analyze_sentiment(
        self,
        text
    ):

        polarity = TextBlob(
            text
        ).sentiment.polarity

        if polarity > 0:
            return "Positive"

        elif polarity < 0:
            return "Negative"

        return "Neutral"

    def get_response(
        self,
        user_input
    ):

        user_vector = self.vectorizer.transform(
            [user_input]
        )

        similarities = cosine_similarity(
            user_vector,
            self.question_vectors
        )

        best_match_index = similarities.argmax()

        confidence = similarities[
            0
        ][
            best_match_index
        ]

        sentiment = self.analyze_sentiment(
            user_input
        )

        if confidence < 0.25:

            return {

                "answer":
                "Sorry, I couldn't find a suitable answer.",

                "confidence":
                round(
                    confidence * 100,
                    2
                ),

                "sentiment":
                sentiment,

                "unknown":
                True
            }

        return {

            "answer":
            self.answers[
                best_match_index
            ],

            "confidence":
            round(
                confidence * 100,
                2
            ),

            "sentiment":
            sentiment,

            "unknown":
            False
        }