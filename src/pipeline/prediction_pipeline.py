import sys
import joblib
import pandas as pd

from src.exception.exception import CustomException
from src.logger.logger import logger


class PredictionPipeline:

    def __init__(self):

        try:

            logger.info("Loading model and preprocessor...")

            self.model = joblib.load("artifacts/model.pkl")
            self.preprocessor = joblib.load("artifacts/preprocessor.pkl")

            logger.info("Model and preprocessor loaded successfully.")

        except Exception as e:
            logger.error(e)
            raise CustomException(e, sys)

    def predict(self, input_data: dict):

        try:

            logger.info("Creating input dataframe...")

            df = pd.DataFrame([input_data])

            logger.info("Handling TotalCharges...")

            df["TotalCharges"] = df["TotalCharges"].replace(
                r"^\s*$",
                pd.NA,
                regex=True,
            )

            df["TotalCharges"] = pd.to_numeric(
                df["TotalCharges"],
                errors="coerce",
            )

            logger.info("Applying preprocessor...")

            transformed_data = self.preprocessor.transform(df)

            prediction = self.model.predict(transformed_data)[0]

            probability = self.model.predict_proba(
                transformed_data
            )[0][1]

            result = {
                "prediction": int(prediction),
                "probability": float(probability),
            }

            logger.info(f"Prediction Result : {result}")

            return result

        except Exception as e:
            logger.error(e)
            raise CustomException(e, sys)