import sys
import pandas as pd

from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

from src.config.configuration import ConfigurationManager
from src.exception.exception import CustomException
from src.logger.logger import logger


class TrainingPipeline:

    def __init__(self):
        logger.info("Training Pipeline Initialized")

    def run_pipeline(self):

        try:

            logger.info("=" * 80)
            logger.info("TRAINING PIPELINE STARTED")
            logger.info("=" * 80)

            # Configuration
            configuration = ConfigurationManager()

            ingestion_config = configuration.get_data_ingestion_config()
            validation_config = configuration.get_data_validation_config()
            schema = configuration.get_schema()

            # ----------------------------
            # Data Ingestion
            # ----------------------------
            ingestion = DataIngestion(ingestion_config)

            df = ingestion.load_data()

            # ----------------------------
            # Data Validation
            # ----------------------------
            validation = DataValidation(
                validation_config,
                schema
            )

            df = validation.validate_dataframe(df)

            # ----------------------------
            # Data Transformation
            # ----------------------------
            transformation = DataTransformation()

            df = transformation.handle_missing_values(df)

            df = transformation.encode_features(df)

            X, y = transformation.split_features_target(df)

            X_train, X_test, y_train, y_test = (
                transformation.split_train_test(X, y)
            )

            X_train, X_test = transformation.scale_features(
                X_train,
                X_test
            )

            # ----------------------------
            # Model Training
            # ----------------------------
            trainer = ModelTrainer()

            model, accuracy = trainer.train(
                X_train,
                X_test,
                y_train,
                y_test
            )

            model_path = trainer.save_model(model)

            logger.info(f"Training Accuracy : {accuracy:.4f}")

            logger.info(f"Model Saved At : {model_path}")

            logger.info("=" * 80)
            logger.info("TRAINING PIPELINE COMPLETED")
            logger.info("=" * 80)

        except Exception as e:
            logger.error(e)
            raise CustomException(e, sys)