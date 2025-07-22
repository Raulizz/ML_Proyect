# Technical Design Document

## Project Overview

This project is a predictive maintenance system for industrial machines. The goal is to predict whether a machine is likely to fail within the next 24 hours based on telemetry data and metadata. The model is deployed as a RESTful API using FastAPI and is fully containerized using Docker.

---

## System Architecture

```text
                    +--------------------+
                    | Raw CSV Data       |
                    | (telemetry, ... )  |
                    +--------------------+
                             |
                             v
                    +--------------------+
                    | Preprocessing      |
                    | generate_dataset.py|
                    +--------------------+
                             |
                             v
                    +--------------------+
                    | Model Training     |
                    | (train_mlflow_*.py)|
                    | XGBoost + MLflow   |
                    +--------------------+
                             |
                             v
                 +-----------------------------+
                 | MLflow Tracking & Artifacts |
                 | (params, metrics, model)    |
                 +-----------------------------+
                             |
                             v
                    +--------------------+
                    | FastAPI Inference  |
                    |  /predict endpoint |
                    +--------------------+
                             |
                             v
                    +--------------------+
                    | Dockerized Service |
                    +--------------------+
```

---

## Components

### 1. **Data Preprocessing**

- Script: `src/preprocessing/generate_dataset.py`
- Features: 3h rolling stats, encoding of categorical vars
- Target: Binary label if failure will happen within 24h

### 2. **Model Training**

- Models: XGBoost with class imbalance correction
- Tools: `scikit-learn`, `xgboost`, `mlflow`
- Tracking: `train_mlflow_1.py` (baseline), `train_mlflow_2.py` (tuned)

### 3. **Model Versioning**

- Managed using MLflow with unique `run_id`
- Model loaded dynamically in API via `mlflow.pyfunc`

### 4. **Deployment**

- API created with FastAPI (`api/main.py`)
- Exposes `/predict` endpoint
- Input schema validated using Pydantic
- Swagger UI auto-documented

### 5. **Dockerization**

- Custom `Dockerfile` using Python 3.10-slim
- System dependencies installed for model compilation
- `.dockerignore` prevents unnecessary bloat
- `mlruns/` copied into image to support local model tracking

---

## Design Decisions

- **XGBoost**: chosen for its robustness with tabular data and imbalance handling
- **MLflow**: lightweight, easy-to-use tracking and model registry
- **FastAPI**: simple, fast, self-documented API layer
- **Docker**: ensures portability and reproducibility
- **No use of pickle files**: Models are loaded directly from MLflow, promoting clean versioning

---

## Future Improvements

- Feature engineering using `errors.csv` and `maint.csv`
- Integration with MLflow Registry server (remote)
- Add monitoring/logging in API
- CI/CD pipeline to automate retraining and deployment
