import sys

from src.config.configuration import ConfigurationManager
from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.exception.exception import CustomException
from src.logger.logger import logger


class TrainingPipeline:
    """
    Orchestrates the complete ML training workflow.
    """

    def __init__(self):
        pass

    def run_pipeline(self):
        try:

            logger.info("=" * 60)
            logger.info("Training Pipeline Started")
            logger.info("=" * 60)

            # Configuration
            config = ConfigurationManager()

            # Data Ingestion
            ingestion_config = config.get_data_ingestion_config()
            ingestion = DataIngestion(ingestion_config)

            df = ingestion.load_data()

            # Data Validation
            validation_config = config.get_data_validation_config()
            schema = config.get_schema()
            validation = DataValidation(validation_config,schema)

            validated_df = validation.validate_dataframe(df)

            logger.info(
                f"Validation Completed. Dataset Shape: {validated_df.shape}"
            )

            logger.info("=" * 60)
            logger.info("Training Pipeline Completed Successfully")
            logger.info("=" * 60)

        except Exception as e:
            logger.error(e)
            raise CustomException(e, sys)