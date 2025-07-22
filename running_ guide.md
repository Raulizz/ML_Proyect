# How to Run the Predictive Maintenance ML API

This guide explains step-by-step how to set up, train, and test the machine learning pipeline locally using Visual Studio Code and Docker.

---

## 1- Clone the Repository from GitHub or unzip the .zip file

In Visual Studio Code:

- Open a terminal
- Run:

```bash
git clone https://github.com/Raulizz/ML_Proyect.git
cd ML_Proyect
```

---

## 2- Create and Activate a Virtual Environment

In your terminal:

```bash
python -m venv venv
```

Then activate it:

- On **Windows**:

```bash
venv\Scripts\activate
```

- On **Mac/Linux**:

```bash
source venv/bin/activate
```

Then install requirements:

```bash
pip install -r requirements.txt
```

---

## 3- Generate the Training Dataset

Run the following script to generate a unified training dataset:

```bash
python src/preprocessing/generate_dataset.py
```

This will create a single unified archive of the raw files:

```
data/processed/train_dataset.csv
```

---

## 4- Explore the Data (EDA)

Open:

```
notebooks/eda.ipynb
```

To understand how the data is distributed, feature correlations, and failure patterns.

---

## 5- Train and Compare ML Models with MLflow

Launch the MLflow UI in one terminal:

```bash
mlflow ui
```

This will start a web server at:

```
http://localhost:5000
```

Then, run the two training scripts in another terminal:

```bash
python src/train/train_mlflow_1.py
python src/train/train_mlflow_2.py
```

Each run will log parameters, metrics, and a model artifact.

### Important: Set the model you want to serve

Open `api/main.py` and find this line:

```python
RUN_ID = "07b4fa3c054940339a543c5bc56205d8"
```

Replace it with the `run_id` of the model you want to test.

You can find it in the MLflow UI:

```
mlruns/0/<RUN_ID>/artifacts/model/
```

Copy that `<RUN_ID>` from MLflow into your `main.py`.

---

## 6- Run the FastAPI Service Locally

Activate your virtual environment if needed, then run:

```bash
uvicorn api.main:app --reload
```

Access the Swagger UI:

```
http://localhost:8000/docs
```

There you can test the `/predict` endpoint with sample input.

---

## 7- Quick Test with Pre-trained Docker Image

If you don't want to retrain anything:

1. Go into the `ready_to_use/` folder
2. Run this from terminal:

```bash
docker build -t predictive-api .
docker run -p 8000:8000 predictive-api
```

3. Open your browser at:

```
http://localhost:8000/docs
```

This will load a pre-trained model and allow predictions directly from the API.
