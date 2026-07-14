import sys

import pandas as pd

from src.exception.exception import CustomException
from src.logger.logger import logger


class DataValidation:
    """
    Responsible for validating the raw dataset before
    it enters the preprocessing pipeline.
    """

    def __init__(self, config):
        self.config = config
        logger.info("DataValidation component initialized.")

    def load_dataset(self):
        """
        Load dataset for validation.
        """

        try:
            logger.info(f"Loading dataset from: {self.config.raw_data_path}")

            df = pd.read_csv(self.config.raw_data_path)

            logger.info(f"Dataset loaded successfully. Shape: {df.shape}")

            return df

        except Exception as e:
            logger.error(e)
            raise CustomException(e, sys)