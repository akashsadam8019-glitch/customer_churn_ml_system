import os
import sys
import joblib
import pandas as pd

from pandas.api.types import (
    is_numeric_dtype,
    is_string_dtype,
    is_object_dtype,
)

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.exception.exception import CustomException
from src.logger.logger import logger


class DataTransformation:

    def __init__(self):
        logger.info("DataTransformation initialized.")

    def prepare_data(self, df: pd.DataFrame):

        try:

            logger.info("Preparing dataset...")

            # =====================================================
            # Handle TotalCharges
            # =====================================================

            df["TotalCharges"] = df["TotalCharges"].replace(
                r"^\s*$",
                pd.NA,
                regex=True,
            )

            df["TotalCharges"] = pd.to_numeric(
                df["TotalCharges"],
                errors="coerce",
            )

            # =====================================================
            # Features & Target
            # =====================================================

            X = df.drop(columns=["customerID", "Churn"])
            y = df["Churn"].map({"No": 0, "Yes": 1})

            # =====================================================
            # Detect Feature Types
            # =====================================================

            categorical_features = [
                col
                for col in X.columns
                if is_string_dtype(X[col]) or is_object_dtype(X[col])
            ]

            numerical_features = [
                col
                for col in X.columns
                if is_numeric_dtype(X[col])
            ]

            logger.info(f"Categorical Features: {categorical_features}")
            logger.info(f"Numerical Features: {numerical_features}")

            # =====================================================
            # Numerical Pipeline
            # =====================================================

            numerical_pipeline = Pipeline(
                steps=[
                    (
                        "imputer",
                        SimpleImputer(strategy="median"),
                    ),
                    (
                        "scaler",
                        StandardScaler(),
                    ),
                ]
            )

            # =====================================================
            # Categorical Pipeline
            # =====================================================

            categorical_pipeline = Pipeline(
                steps=[
                    (
                        "imputer",
                        SimpleImputer(strategy="most_frequent"),
                    ),
                    (
                        "encoder",
                        OneHotEncoder(
                            handle_unknown="ignore",
                            sparse_output=False,
                        ),
                    ),
                ]
            )

            # =====================================================
            # Column Transformer
            # =====================================================

            preprocessor = ColumnTransformer(
                transformers=[
                    (
                        "num",
                        numerical_pipeline,
                        numerical_features,
                    ),
                    (
                        "cat",
                        categorical_pipeline,
                        categorical_features,
                    ),
                ]
            )

            # =====================================================
            # Train Test Split
            # =====================================================

            X_train, X_test, y_train, y_test = train_test_split(
                X,
                y,
                test_size=0.2,
                random_state=42,
                stratify=y,
            )

            # =====================================================
            # Apply Preprocessing
            # =====================================================

            X_train = preprocessor.fit_transform(X_train)
            X_test = preprocessor.transform(X_test)

            logger.info("Data Transformation Completed Successfully.")

            return (
                X_train,
                X_test,
                y_train,
                y_test,
                preprocessor,
            )

        except Exception as e:
            logger.error(e)
            raise CustomException(e, sys)

    def save_preprocessor(self, preprocessor):

        try:

            os.makedirs("artifacts", exist_ok=True)

            path = "artifacts/preprocessor.pkl"

            joblib.dump(preprocessor, path)

            logger.info(f"Preprocessor saved at {path}")

            return path

        except Exception as e:
            logger.error(e)
            raise CustomException(e, sys)