from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    raw_data_path: Path


@dataclass(frozen=True)
class DataValidationConfig:
    raw_data_path: Path
    schema_path: Path
    validation_report_path: Path


@dataclass(frozen=True)
class DataTransformationConfig:
    processed_data_path: Path


@dataclass(frozen=True)
class ModelTrainerConfig:
    trained_model_path: Path