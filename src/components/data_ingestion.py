import sys

import pandas as pd

from src.exception.exception import CustomException
from src.logger.logger import logger


class DataIngestion:
    """
    Responsible for loading the raw dataset.
    """

    def __init__(self, config):
        self.config = config
        logger.info("DataIngestion component initialized.")

    def load_data(self):
        """
        Load the raw dataset from the configured path.
        """

        try:
            logger.info(f"Reading dataset from: {self.config.raw_data_path}")

            df = pd.read_csv(self.config.raw_data_path)

            logger.info(f"Dataset loaded successfully. Shape: {df.shape}")

            return df

        except Exception as e:
            logger.error(f"Error while loading dataset: {e}")
            raise CustomException(e, sys)