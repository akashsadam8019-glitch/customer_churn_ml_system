from pathlib import Path
import yaml

from src.constants.constants import CONFIG_FILE_PATH, SCHEMA_FILE_PATH
from src.entity.config_entity import (
    DataIngestionConfig,
    DataValidationConfig,
)


class ConfigurationManager:
    """
    Loads project configuration and provides configuration
    objects for different pipeline components.
    """

    def __init__(
        self,
        config_filepath=CONFIG_FILE_PATH,
        schema_filepath=SCHEMA_FILE_PATH,
    ):

        with open(config_filepath, "r") as file:
            self.config = yaml.safe_load(file)

        with open(schema_filepath, "r") as file:
            self.schema = yaml.safe_load(file)

    # =====================================================
    # Data Ingestion
    # =====================================================

    def get_data_ingestion_config(self) -> DataIngestionConfig:

        return DataIngestionConfig(
            raw_data_path=Path(
                self.config["data"]["raw_data_path"]
            )
        )

    # =====================================================
    # Data Validation
    # =====================================================

    def get_data_validation_config(self) -> DataValidationConfig:

        return DataValidationConfig(
            raw_data_path=Path(
                self.config["data"]["raw_data_path"]
            ),
            schema_path=SCHEMA_FILE_PATH,
            validation_report_path=Path(
                self.config["reports"]["validation_report_path"]
            ),
        )

    # =====================================================
    # Schema
    # =====================================================

    def get_schema(self):

        return self.schema

    # =====================================================
    # Artifact Paths
    # =====================================================

    def get_model_path(self):

        return self.config["artifacts"]["model_path"]

    def get_preprocessor_path(self):

        return self.config["artifacts"]["preprocessor_path"]

    def get_artifact_dir(self):

        return self.config["artifacts"]["artifact_dir"]

    # =====================================================
    # MLflow
    # =====================================================

    def get_experiment_name(self):

        return self.config["mlflow"]["experiment_name"]

    # =====================================================
    # API
    # =====================================================

    def get_api_host(self):

        return self.config["api"]["host"]

    def get_api_port(self):

        return self.config["api"]["port"]