import sys
import pandas as pd

from src.exception.exception import CustomException
from src.logger.logger import logger


class DataTransformation:

    def __init__(self):
        logger.info("DataTransformation component initialized.")

    def handle_missing_values(self, df: pd.DataFrame) -> pd.DataFrame:

        try:

            logger.info("Handling missing values...")

            # Replace blank strings with NaN
            df["TotalCharges"] = df["TotalCharges"].replace(r"^\s*$", pd.NA, regex=True)

            # Convert to numeric
            df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

            # Fill missing values using median
            median_value = df["TotalCharges"].median()

            df["TotalCharges"] = df["TotalCharges"].fillna(median_value)

            logger.info("Missing values handled successfully.")

            return df

        except Exception as e:
            logger.error(e)
            raise CustomException(e, sys)