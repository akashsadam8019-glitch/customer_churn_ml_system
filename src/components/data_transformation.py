import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

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

            df["TotalCharges"] = df["TotalCharges"].fillna(
                df["TotalCharges"].median()
            )

            logger.info("Missing values handled successfully.")

            return df

        except Exception as e:
            logger.error(e)
            raise CustomException(e, sys)

    def encode_features(self, df: pd.DataFrame) -> pd.DataFrame:

        try:
            logger.info("Encoding categorical features...")

            encoder = LabelEncoder()

            categorical_columns = df.select_dtypes(
                include=["object", "string", "str"]
            ).columns.tolist()

            if "customerID" in categorical_columns:
                categorical_columns.remove("customerID")

            if "Churn" in categorical_columns:
                categorical_columns.remove("Churn")

            for column in categorical_columns:
                df[column] = encoder.fit_transform(df[column])

            df["Churn"] = encoder.fit_transform(df["Churn"])

            logger.info("Encoding completed.")

            return df

        except Exception as e:
            logger.error(e)
            raise CustomException(e, sys)

    def split_features_target(self, df: pd.DataFrame):

        try:
            logger.info("Splitting features and target...")

            X = df.drop(columns=["customerID", "Churn"])
            y = df["Churn"]

            return X, y

        except Exception as e:
            logger.error(e)
            raise CustomException(e, sys)

    def split_train_test(self, X, y):

        try:
            logger.info("Splitting train and test datasets...")

            X_train, X_test, y_train, y_test = train_test_split(
                X,
                y,
                test_size=0.2,
                random_state=42,
                stratify=y,
            )

            logger.info(f"X_train : {X_train.shape}")
            logger.info(f"X_test  : {X_test.shape}")
            logger.info(f"y_train : {y_train.shape}")
            logger.info(f"y_test  : {y_test.shape}")

            return X_train, X_test, y_train, y_test

        except Exception as e:
            logger.error(e)
            raise CustomException(e, sys)

    def scale_features(self, X_train, X_test):

        try:
            logger.info("Scaling numerical features...")

            scaler = StandardScaler()

            numeric_columns = [
                "tenure",
                "MonthlyCharges",
                "TotalCharges",
            ]

            X_train = X_train.copy()
            X_test = X_test.copy()

            X_train[numeric_columns] = scaler.fit_transform(
                X_train[numeric_columns]
            )

            X_test[numeric_columns] = scaler.transform(
                X_test[numeric_columns]
            )

            logger.info("Feature scaling completed.")

            return X_train, X_test

        except Exception as e:
            logger.error(e)
            raise CustomException(e, sys)