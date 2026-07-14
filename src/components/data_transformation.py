import sys
import pandas as pd
from sklearn.preprocessing import LabelEncoder

from src.exception.exception import CustomException
from src.logger.logger import logger


class DataTransformation:

    def __init__(self):
        logger.info("DataTransformation component initialized.")

    def handle_missing_values(self, df: pd.DataFrame) -> pd.DataFrame:

        try:

            logger.info("Handling missing values...")

            df["TotalCharges"] = df["TotalCharges"].replace(
                r"^\s*$", pd.NA, regex=True
            )

            df["TotalCharges"] = pd.to_numeric(
                df["TotalCharges"],
                errors="coerce"
            )

            median_value = df["TotalCharges"].median()

            df["TotalCharges"] = df["TotalCharges"].fillna(median_value)

            logger.info("Missing values handled successfully.")

            return df

        except Exception as e:
            logger.error(e)
            raise CustomException(e, sys)

    def encode_features(self, df: pd.DataFrame) -> pd.DataFrame:

        try:

            logger.info("Encoding categorical features...")

            label_encoder = LabelEncoder()

            categorical_columns = df.select_dtypes(
                include=["object", "string", "str"]
            ).columns.tolist()

            categorical_columns.remove("customerID")
            categorical_columns.remove("Churn")

            for column in categorical_columns:
                df[column] = label_encoder.fit_transform(df[column])

            df["Churn"] = label_encoder.fit_transform(df["Churn"])

            logger.info("Categorical encoding completed.")

            return df

        except Exception as e:
            logger.error(e)
            raise CustomException(e, sys)