import os
import sys
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
)

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

            params = {
                "n_estimators": 200,
                "max_depth": 10,
                "min_samples_split": 5,
                "min_samples_leaf": 2,
                "random_state": 42,
                "n_jobs": -1,

            }   

            metrics = {
                "accuracy": accuracy_score(y_test, predictions),
                "precision": precision_score(y_test, predictions),
                "recall": recall_score(y_test, predictions),
                "f1_score": f1_score(y_test, predictions),
            }

            logger.info(metrics)

            return model, metrics, params

        except Exception as e:
            logger.error(e)
            raise CustomException(e, sys)

    def save_model(self, model):

        try:

            os.makedirs("artifacts", exist_ok=True)

            model_path = "artifacts/model.pkl"

            joblib.dump(model, model_path)

            logger.info(f"Model saved at {model_path}")

            return model_path

        except Exception as e:
            logger.error(e)
            raise CustomException(e, sys)