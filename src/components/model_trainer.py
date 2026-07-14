import os
import sys
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

from src.exception.exception import CustomException
from src.logger.logger import logger


class ModelTrainer:

    def __init__(self):
        logger.info("ModelTrainer initialized.")

    def train(self, X_train, X_test, y_train, y_test):

        try:

            logger.info("Training Random Forest model...")

            model = RandomForestClassifier(
                n_estimators=200,
                random_state=42
            )

            model.fit(X_train, y_train)

            predictions = model.predict(X_test)

            accuracy = accuracy_score(y_test, predictions)

            logger.info(f"Accuracy: {accuracy:.4f}")

            return model, accuracy

        except Exception as e:
            logger.error(e)
            raise CustomException(e, sys)

    def save_model(self, model):

        try:

            logger.info("Saving trained model...")

            os.makedirs("models", exist_ok=True)

            model_path = os.path.join(
                "models",
                "customer_churn_model.pkl"
            )

            joblib.dump(model, model_path)

            logger.info(f"Model saved at: {model_path}")

            return model_path

        except Exception as e:
            logger.error(e)
            raise CustomException(e, sys)