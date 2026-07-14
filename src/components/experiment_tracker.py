import sys
import mlflow
import mlflow.sklearn

from src.exception.exception import CustomException
from src.logger.logger import logger


class ExperimentTracker:

    def __init__(self):
        logger.info("ExperimentTracker initialized.")
        mlflow.set_experiment("Customer_Churn_Prediction")

    def log_experiment(
        self,
        model,
        metrics,
        params,
    ):

        try:

            with mlflow.start_run():

                logger.info("Logging experiment...")

                mlflow.log_params(params)

                mlflow.log_metrics(metrics)

                # Log model only
                mlflow.sklearn.log_model(
                    sk_model=model,
                    name="model",
                    serialization_format="cloudpickle",
                )

                logger.info("Experiment logged successfully.")

        except Exception as e:
            logger.error(e)
            raise CustomException(e, sys)