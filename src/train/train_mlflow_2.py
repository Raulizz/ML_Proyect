import pandas as pd
import xgboost as xgb
import mlflow
import mlflow.xgboost
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, f1_score, precision_score, recall_score

# 🔹 1. Load data
df = pd.read_csv("data/processed/train_dataset.csv")
X = df.drop(columns=["failure_within_24h", "datetime","machineID"])
y = df["failure_within_24h"]

# Encode categorical variable
X = pd.get_dummies(X, columns=["model"])

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 🔹 3. MLflow experiment
mlflow.set_experiment("PredictiveMaintenance")

with mlflow.start_run(run_name="prueba_2"):
    # Tuned hyperparameters
    max_depth = 4
    learning_rate = 0.1
    n_estimators = 100

    # Weight for imbalanced classes
    scale_pos_weight = (y_train == 0).sum() / (y_train == 1).sum()

    # XGBoost Model
    model = xgb.XGBClassifier(
        objective="binary:logistic",
        eval_metric="auc",
        use_label_encoder=False,
        scale_pos_weight=scale_pos_weight,
        max_depth=max_depth,
        learning_rate=learning_rate,
        n_estimators=n_estimators,
        random_state=42
    )

    # Train
    model.fit(X_train, y_train)

    # Metrics
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1]

    auc = roc_auc_score(y_test, y_proba)
    f1 = f1_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)

    # Log to MLflow
    mlflow.log_params({
        "scale_pos_weight": scale_pos_weight,
        "max_depth": max_depth,
        "learning_rate": learning_rate,
        "n_estimators": n_estimators
    })
    mlflow.log_metrics({
        "AUC": auc,
        "F1": f1,
        "Precision": precision,
        "Recall": recall
    })
    mlflow.set_tag("dataset", "train_dataset.csv")
    
    # Save model to MLflow
    mlflow.xgboost.log_model(model, artifact_path="model")

    print("Model logged. Check the MLflow UI.")
