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

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        return DataIngestionConfig(
            raw_data_path=Path(self.config["data"]["raw_data_path"])
        )

    def get_data_validation_config(self) -> DataValidationConfig:
        return DataValidationConfig(
            raw_data_path=Path(self.config["data"]["raw_data_path"]),
            schema_path=SCHEMA_FILE_PATH,
            validation_report_path=Path(
                self.config["reports"]["validation_report_path"]
            ),
        )