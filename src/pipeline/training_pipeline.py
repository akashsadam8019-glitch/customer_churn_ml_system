import sys

from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.components.model_evaluation import ModelEvaluation
from src.components.experiment_tracker import ExperimentTracker

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

            # =====================================================
            # Configuration
            # =====================================================

            configuration = ConfigurationManager()

            ingestion_config = configuration.get_data_ingestion_config()
            validation_config = configuration.get_data_validation_config()
            schema = configuration.get_schema()

            # =====================================================
            # Data Ingestion
            # =====================================================

            ingestion = DataIngestion(ingestion_config)

            df = ingestion.load_data()

            # =====================================================
            # Data Validation
            # =====================================================

            validation = DataValidation(
                validation_config,
                schema
            )

            df = validation.validate_dataframe(df)

            # =====================================================
            # Data Transformation
            # =====================================================

            transformation = DataTransformation()

            (
                X_train,
                X_test,
                y_train,
                y_test,
                preprocessor,
            ) = transformation.prepare_data(df)

            transformation.save_preprocessor(preprocessor)

            # =====================================================
            # Model Training
            # =====================================================

            trainer = ModelTrainer()

            model, metrics, params = trainer.train(
                X_train,
                X_test,
                y_train,
                y_test,
            )

            # =====================================================
            # Model Evaluation
            # =====================================================

            evaluator = ModelEvaluation()

            metrics, confusion, report = evaluator.evaluate(
                model,
                X_test,
                y_test,
            )

            # =====================================================
            # MLflow
            # =====================================================

            tracker = ExperimentTracker()

            tracker.log_experiment(
                model=model,
                metrics=metrics,
                params=params,
            )

            # =====================================================
            # Save Model
            # =====================================================

            trainer.save_model(model)

            logger.info("=" * 80)
            logger.info("TRAINING PIPELINE COMPLETED SUCCESSFULLY")
            logger.info("=" * 80)

        except Exception as e:
            logger.error(e)
            raise CustomException(e, sys)