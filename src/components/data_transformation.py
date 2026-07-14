import sys
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

            # Handle TotalCharges
            df["TotalCharges"] = df["TotalCharges"].replace(
                r"^\s*$",
                pd.NA,
                regex=True,
            )

            df["TotalCharges"] = pd.to_numeric(
                df["TotalCharges"],
                errors="coerce",
            )

            # Split Features and Target
            X = df.drop(columns=["customerID", "Churn"])
            y = df["Churn"].map({"No": 0, "Yes": 1})

            # Feature Lists
            categorical_features = X.select_dtypes(
                include=["object", "string", "str"]
            ).columns.tolist()

            numerical_features = X.select_dtypes(
                include=["int64", "float64"]
            ).columns.tolist()

            logger.info(f"Categorical Features: {categorical_features}")
            logger.info(f"Numerical Features: {numerical_features}")

            # Numerical Pipeline
            numerical_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler()),
                ]
            )

            # Categorical Pipeline
            categorical_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    (
                        "encoder",
                        OneHotEncoder(
                            handle_unknown="ignore"
                        ),
                    ),
                ]
            )

            # Combine Pipelines
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

            # Train/Test Split
            X_train, X_test, y_train, y_test = train_test_split(
                X,
                y,
                test_size=0.2,
                random_state=42,
                stratify=y,
            )

            # Apply Preprocessing
            X_train = preprocessor.fit_transform(X_train)
            X_test = preprocessor.transform(X_test)

            logger.info("Data transformation completed successfully.")

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