# 🚀 Customer Churn Prediction System

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Production-green)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)
![MLflow](https://img.shields.io/badge/MLflow-Experiment%20Tracking-blue)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED)
![GitHub Actions](https://img.shields.io/badge/CI-GitHub%20Actions-success)

---

# 📌 Overview

Customer churn is one of the biggest challenges for subscription-based businesses. Acquiring a new customer costs significantly more than retaining an existing one. This project predicts whether a customer is likely to leave a telecom service using Machine Learning while demonstrating how to build a production-ready ML system rather than just a prediction model.

Unlike notebook-based ML projects, this repository implements a complete machine learning pipeline including data validation, preprocessing, model training, experiment tracking, REST API deployment, Docker containerization, and CI/CD automation.

---

# 🎯 Objectives

- Predict customer churn using Machine Learning.
- Build an end-to-end production ML pipeline.
- Track experiments using MLflow.
- Deploy prediction service using FastAPI.
- Containerize the application using Docker.
- Automate testing using GitHub Actions.

---

# ✨ Features

- End-to-End ML Pipeline
- Data Validation
- Data Transformation
- Feature Engineering
- Random Forest Classification
- Experiment Tracking (MLflow)
- REST API using FastAPI
- Swagger Documentation
- Docker Support
- Docker Compose
- GitHub Actions CI
- Structured Logging
- Custom Exception Handling
- Modular Project Structure

---

# 🛠 Tech Stack

| Category | Technologies |
|-----------|--------------|
| Language | Python 3.12 |
| Machine Learning | Scikit-Learn |
| Data Processing | Pandas, NumPy |
| API | FastAPI |
| Experiment Tracking | MLflow |
| Containerization | Docker |
| CI/CD | GitHub Actions |
| Model Serialization | Joblib |
| Version Control | Git + GitHub |

---

# 📂 Project Structure

```text
customer_churn_ml_system/

│
├── configs/
├── data/
│   ├── raw/
│   ├── interim/
│   └── processed/
│
├── artifacts/
├── models/
├── reports/
├── notebooks/
├── tests/
│
├── src/
│   ├── api/
│   ├── components/
│   ├── config/
│   ├── constants/
│   ├── entity/
│   ├── exception/
│   ├── logger/
│   ├── monitoring/
│   ├── pipeline/
│   └── utils/
│
├── Dockerfile
├── requirements.txt
├── main.py
└── README.md
```

---

# 🏗 System Architecture

```text
                Dataset
                   │
                   ▼
         Data Validation
                   │
                   ▼
      Data Transformation
                   │
                   ▼
        Feature Engineering
                   │
                   ▼
      Random Forest Training
                   │
         ┌─────────┴─────────┐
         ▼                   ▼
   MLflow Logging      Saved Model
                               │
                               ▼
                     Prediction Pipeline
                               │
                               ▼
                           FastAPI
                               │
                               ▼
                        Docker Container
                               │
                               ▼
                     GitHub Actions CI
```

---

# ⚙️ Machine Learning Workflow

1. Load Dataset
2. Validate Dataset
3. Handle Missing Values
4. Encode Categorical Features
5. Scale Numerical Features
6. Train Random Forest Model
7. Evaluate Model
8. Log Experiment using MLflow
9. Save Model
10. Serve Predictions using FastAPI
11. Containerize using Docker
12. Automate using GitHub Actions
---

# 🚀 Installation

## Clone the Repository

```bash
git clone https://github.com/<your-github-username>/customer_churn_ml_system.git

cd customer_churn_ml_system
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Train the Model

```bash
python main.py
```

This command will:

- Validate the dataset
- Transform the data
- Train the Random Forest model
- Evaluate performance
- Save the trained model
- Save the preprocessing pipeline
- Log the experiment using MLflow

---

# 📊 MLflow Experiment Tracking

Launch MLflow UI:

```bash
mlflow ui
```

Open:

```
http://127.0.0.1:5000
```

You can inspect:

- Experiment history
- Model parameters
- Performance metrics
- Model artifacts

---

# 🌐 Run FastAPI Server

```bash
uvicorn src.api.app:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

Swagger UI provides interactive API documentation for testing the prediction endpoint.

---

# 🐳 Docker

## Build Docker Image

```bash
docker build -t customer-churn-api .
```

---

## Run Docker Container

```bash
docker run -p 8000:8000 customer-churn-api
```

Open:

```
http://localhost:8000/docs
```

---

# 🐳 Docker Compose

Run the complete application:

```bash
docker compose up -d
```

Stop the application:

```bash
docker compose down
```

---

# 📡 API Endpoint

## POST `/predict`

Example Request

```json
{
  "gender": "Female",
  "SeniorCitizen": 0,
  "Partner": "Yes",
  "Dependents": "No",
  "tenure": 12,
  "PhoneService": "Yes",
  "MultipleLines": "No",
  "InternetService": "Fiber optic",
  "OnlineSecurity": "No",
  "OnlineBackup": "Yes",
  "DeviceProtection": "No",
  "TechSupport": "No",
  "StreamingTV": "Yes",
  "StreamingMovies": "No",
  "Contract": "Month-to-month",
  "PaperlessBilling": "Yes",
  "PaymentMethod": "Electronic check",
  "MonthlyCharges": 79.85,
  "TotalCharges": 958.20
}
```

Example Response

```json
{
  "prediction": 1,
  "probability": 0.87
}
```

Where:

- `prediction = 1` → Customer likely to churn
- `prediction = 0` → Customer likely to stay

---

# 📈 Continuous Integration

Every push or pull request automatically:

- Installs dependencies
- Verifies project imports
- Runs the training pipeline
- Builds the Docker image

This ensures the repository remains functional after every code change.

---

# 📸 Screenshots

Add screenshots here after running the project.

Suggested images:

- MLflow Dashboard
- Swagger UI
- GitHub Actions
- Docker Desktop
- API Prediction Response

---

# 🚀 Future Improvements

- Hyperparameter tuning
- Model versioning
- Cloud deployment (AWS/Azure/GCP)
- Automated monitoring and drift detection
- Batch prediction pipeline
- Authentication for API
- Database integration

---

# 💼 Skills Demonstrated

- Machine Learning
- Feature Engineering
- Data Validation
- Model Evaluation
- Experiment Tracking
- REST API Development
- FastAPI
- Docker
- Docker Compose
- GitHub Actions
- MLOps Fundamentals
- Software Engineering Best Practices

---

# 📄 License

This project is licensed under the MIT License.

---

# 🙋 Author

**Akash**

Machine Learning & AI Engineering Portfolio Project

Built as a production-style end-to-end ML system for demonstrating applied machine learning, MLOps fundamentals, and backend deployment skills.3

## Architecture Diagram

For the complete architecture, see:

```text
assets/architecture.md
```
