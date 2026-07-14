import sys

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

            logger.info(f"Accuracy : {accuracy:.4f}")

            return model, accuracy

        except Exception as e:
            logger.error(e)
            raise CustomException(e, sys)