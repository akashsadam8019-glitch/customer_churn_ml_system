import sys
import pandas as pd

from src.exception.exception import CustomException
from src.logger.logger import logger


class DataValidation:
    """
    Responsible for validating the ingested dataset.
    """

    def __init__(self, config, schema):
        self.config = config
        self.schema = schema
        logger.info("DataValidation component initialized.")

    def validate_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Validate the ingested dataframe.

        Validation Checks:
        1. Dataset is not empty
        2. Required columns exist
        3. Semantic data type validation
        4. Missing value analysis
        5. Duplicate row analysis
        """

        try:

            logger.info("=" * 60)
            logger.info("Starting Data Validation")
            logger.info("=" * 60)

            # =====================================================
            # 1. Empty Dataset Validation
            # =====================================================
            if df.empty:
                raise ValueError("Dataset is empty.")

            logger.info("Dataset is not empty.")

            # =====================================================
            # 2. Required Column Validation
            # =====================================================
            expected_columns = list(self.schema["columns"].keys())
            actual_columns = list(df.columns)

            missing_columns = [
                column
                for column in expected_columns
                if column not in actual_columns
            ]

            if missing_columns:
                raise ValueError(
                    f"Missing columns: {missing_columns}"
                )

            logger.info("All required columns are present.")

            # =====================================================
            # 3. Semantic Data Type Validation
            # =====================================================
            expected_schema = self.schema["columns"]

            for column, expected_type in expected_schema.items():

                series = df[column]

                if expected_type == "numeric":

                    if not pd.api.types.is_numeric_dtype(series):
                        raise ValueError(
                            f"Column '{column}' should be numeric."
                        )

                elif expected_type == "integer":

                    if not pd.api.types.is_integer_dtype(series):
                        raise ValueError(
                            f"Column '{column}' should be integer."
                        )

                elif expected_type == "string":

                    if not (
                        pd.api.types.is_object_dtype(series)
                        or pd.api.types.is_string_dtype(series)
                    ):
                        raise ValueError(
                            f"Column '{column}' should be string."
                        )

                elif expected_type == "categorical":

                    if not (
                        pd.api.types.is_object_dtype(series)
                        or pd.api.types.is_string_dtype(series)
                        or pd.api.types.is_categorical_dtype(series)
                    ):
                        raise ValueError(
                            f"Column '{column}' should be categorical."
                        )

            logger.info("Semantic data types validated successfully.")

            # =====================================================
            # 4. Missing Value Analysis
            # =====================================================
            missing_values = df.isnull().sum()

            missing_columns = missing_values[
                missing_values > 0
            ]

            if not missing_columns.empty:

                logger.warning("Missing values detected:")

                for column, count in missing_columns.items():
                    logger.warning(f"{column}: {count}")

            else:
                logger.info("No missing values found.")

            # =====================================================
            # 5. Duplicate Row Analysis
            # =====================================================
            duplicate_rows = df.duplicated().sum()

            if duplicate_rows > 0:
                logger.warning(
                    f"Duplicate rows found: {duplicate_rows}"
                )
            else:
                logger.info("No duplicate rows found.")

            # =====================================================
            # Validation Summary
            # =====================================================
            logger.info("=" * 60)
            logger.info("Data Validation Completed Successfully")
            logger.info(f"Rows    : {df.shape[0]}")
            logger.info(f"Columns : {df.shape[1]}")
            logger.info("=" * 60)

            return df

        except Exception as e:
            logger.error(e)
            raise CustomException(e, sys)