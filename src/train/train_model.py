import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, f1_score, precision_score, recall_score
import pickle
import os

# Cargar dataset
df = pd.read_csv("data/processed/train_dataset.csv")

# Separar features y target
X = df.drop(columns=["failure_within_24h", "datetime"])
y = df["failure_within_24h"]

# Convertir 'model' a variables dummies
X = pd.get_dummies(X, columns=["model"])

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Calcular proporción para scale_pos_weight
scale_pos_weight = (y_train == 0).sum() / (y_train == 1).sum()

# Modelo XGBoost
model = xgb.XGBClassifier(
    objective="binary:logistic",
    eval_metric="auc",
    use_label_encoder=False,
    scale_pos_weight=scale_pos_weight,
    random_state=42
)

model.fit(X_train, y_train)

# Predicciones
y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)[:, 1]

# Métricas
print("AUC:", roc_auc_score(y_test, y_proba))
print("F1:", f1_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))


# Guardar modelo
os.makedirs("models", exist_ok=True)
with open("models/xgb_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Modelo guardado en models/xgb_model.pkl")
