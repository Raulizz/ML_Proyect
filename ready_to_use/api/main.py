from fastapi import FastAPI
from pydantic import BaseModel
import mlflow.pyfunc
import pandas as pd

# Run FastAPI
app = FastAPI(title="Predictive Maintenance API")

# Load the model from MLflow
model = mlflow.xgboost.load_model("prod_model/model")

# Define the input schema
class InputData(BaseModel):
    volt_mean: float
    volt_std: float
    rotate_mean: float
    rotate_std: float
    pressure_mean: float
    pressure_std: float
    vibration_mean: float
    vibration_std: float
    age: int
    model_model1: int
    model_model2: int
    model_model3: int
    model_model4: int

# The endpoint is created (/predict)
import logging
logging.basicConfig(level=logging.INFO)

@app.post("/predict")
def predict(data: InputData):
    try:
        input_df = pd.DataFrame([data.model_dump()])
        prediction = model.predict(input_df)
        return {"failure_prediction": int(prediction[0])}
    except Exception as e:
        logging.error(f"Prediction error: {e}")
        return {"error": str(e)}
