import os
import sys
import joblib
import pandas as pd

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

            df["TotalCharges"] = df["TotalCharges"].replace(
                r"^\s*$",
                pd.NA,
                regex=True
            )

            df["TotalCharges"] = pd.to_numeric(
                df["TotalCharges"],
                errors="coerce"
            )

            X = df.drop(columns=["customerID", "Churn"])
            y = df["Churn"].map({"No": 0, "Yes": 1})

            categorical_features = X.select_dtypes(
                include=["object", "string", "str"]
            ).columns.tolist()

            numerical_features = X.select_dtypes(
                include=["int64", "float64"]
            ).columns.tolist()

            numerical_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler()),
                ]
            )

            categorical_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    (
                        "encoder",
                        OneHotEncoder(handle_unknown="ignore"),
                    ),
                ]
            )

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

            X_train, X_test, y_train, y_test = train_test_split(
                X,
                y,
                test_size=0.2,
                random_state=42,
                stratify=y,
            )

            X_train = preprocessor.fit_transform(X_train)
            X_test = preprocessor.transform(X_test)

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