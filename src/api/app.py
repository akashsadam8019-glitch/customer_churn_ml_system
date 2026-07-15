from fastapi import FastAPI
from fastapi.responses import JSONResponse

from src.entity.prediction_entity import CustomerData
from src.pipeline.prediction_pipeline import PredictionPipeline


app = FastAPI(
    title="Customer Churn Prediction API",
    version="1.0.0",
    description="Production Grade ML API",
)


@app.get("/")
def home():

    return {
        "message": "Customer Churn Prediction API is Running"
    }


@app.post("/predict")
def predict(data: CustomerData):

    pipeline = PredictionPipeline()

    result = pipeline.predict(data.model_dump())

    return JSONResponse(content=result)