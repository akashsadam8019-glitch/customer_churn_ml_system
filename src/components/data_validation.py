import sys

import pandas as pd

from src.exception.exception import CustomException
from src.logger.logger import logger


class DataValidation:
    """
    Responsible for validating the ingested dataset.
    """

    def __init__(self, config):
        self.config = config
        logger.info("DataValidation component initialized.")

    def validate_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Validate the ingested dataframe.
        """

        try:
            logger.info("Starting data validation...")

            if df.empty:
                raise ValueError("Dataset is empty.")

            logger.info(f"Dataset contains {df.shape[0]} rows and {df.shape[1]} columns.")

            return df

        except Exception as e:
            logger.error(e)
            raise CustomException(e, sys)