import pandas as pd
import xgboost as xgb
import mlflow
import mlflow.xgboost
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, f1_score, precision_score, recall_score

# Load the data
df = pd.read_csv("data/processed/train_dataset.csv")

X = df.drop(columns=["failure_within_24h", "datetime","machineID"])
y = df["failure_within_24h"]

# Convert categorical variable
X = pd.get_dummies(X, columns=["model"])

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Set up MLflow
mlflow.set_experiment("PredictiveMaintenance")

with mlflow.start_run(run_name="prueba_1"):

    # Compute class balance for weighting
    scale_pos_weight = (y_train == 0).sum() / (y_train == 1).sum()

    # 🔹 4. Define the model
    model = xgb.XGBClassifier(
        objective="binary:logistic",
        eval_metric="auc",
        use_label_encoder=False,
        scale_pos_weight=scale_pos_weight,
        random_state=42
    )

    # Train the model
    model.fit(X_train, y_train)

    # Evaluation metrics
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1]

    auc = roc_auc_score(y_test, y_proba)
    f1 = f1_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)

    # Log parameters and metrics to MLflow
    mlflow.log_param("scale_pos_weight", scale_pos_weight)
    mlflow.log_metric("AUC", auc)
    mlflow.log_metric("F1", f1)
    mlflow.log_metric("Precision", precision)
    mlflow.log_metric("Recall", recall)
    mlflow.set_tag("dataset", "train_dataset.csv")
    mlflow.set_tag("dataset", "train_dataset.csv")

    # Save the model into mlruns/
    mlflow.xgboost.log_model(model, artifact_path="model")

    print("Training completed and model saved to MLflow.")
