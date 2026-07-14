from pathlib import Path

# Project Root Directory
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Configuration
CONFIG_FILE_PATH = PROJECT_ROOT / "configs" / "config.yaml"
SCHEMA_FILE_PATH = PROJECT_ROOT / "configs" / "schema.yaml"

# Data Directories
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# Model Directory
MODEL_DIR = PROJECT_ROOT / "models"

# Report Directory
REPORT_DIR = PROJECT_ROOT / "reports"

# Log Directory
LOG_DIR = PROJECT_ROOT / "logs"

# MLflow Directory
MLFLOW_DIR = PROJECT_ROOT / "mlruns"

# Test Directory
TEST_DIR = PROJECT_ROOT / "tests"