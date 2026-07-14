import sys

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    classification_report,
)

from src.exception.exception import CustomException
from src.logger.logger import logger


class ModelEvaluation:

    def __init__(self):
        logger.info("ModelEvaluation initialized.")

    def evaluate(self, model, X_test, y_test):

        try:

            logger.info("Evaluating model...")

            predictions = model.predict(X_test)

            probabilities = model.predict_proba(X_test)[:, 1]

            metrics = {
                "accuracy": accuracy_score(y_test, predictions),
                "precision": precision_score(y_test, predictions),
                "recall": recall_score(y_test, predictions),
                "f1_score": f1_score(y_test, predictions),
                "roc_auc": roc_auc_score(y_test, probabilities),
            }

            confusion = confusion_matrix(y_test, predictions)

            report = classification_report(
                y_test,
                predictions,
                output_dict=False,
            )

            logger.info(f"Accuracy : {metrics['accuracy']:.4f}")
            logger.info(f"Precision: {metrics['precision']:.4f}")
            logger.info(f"Recall   : {metrics['recall']:.4f}")
            logger.info(f"F1 Score : {metrics['f1_score']:.4f}")
            logger.info(f"ROC AUC  : {metrics['roc_auc']:.4f}")

            logger.info(f"\nConfusion Matrix\n{confusion}")

            logger.info(f"\nClassification Report\n{report}")

            return metrics, confusion, report

        except Exception as e:
            logger.error(e)
            raise CustomException(e, sys)