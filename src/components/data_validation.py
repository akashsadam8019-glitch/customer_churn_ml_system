import sys

import pandas as pd

from src.exception.exception import CustomException
from src.logger.logger import logger


class DataValidation:
    """
    Responsible for validating the ingested dataset.
    """

    def __init__(self, config, schema):
        self.config = config
        self.schema = schema
        logger.info("DataValidation component initialized.")

    def validate_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Validate the ingested dataframe.
        """

        try:
            logger.info("Starting data validation...")

            # Check if dataset is empty
            if df.empty:
                raise ValueError("Dataset is empty.")

            # Check required columns
            expected_columns = list(self.schema["columns"].keys())
            actual_columns = list(df.columns)

            missing_columns = [
                col for col in expected_columns if col not in actual_columns
            ]

            if missing_columns:
                raise ValueError(
                    f"Missing columns: {missing_columns}"
                )

            logger.info("All required columns are present.")

            logger.info(
                f"Dataset contains {df.shape[0]} rows and {df.shape[1]} columns."
            )

            return df

        except Exception as e:
            logger.error(e)
            raise CustomException(e, sys)