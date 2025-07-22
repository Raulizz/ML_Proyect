# Technical Report

## Project Summary

This project demonstrates a full MLOps workflow applied to predictive maintenance. The goal is to detect whether a machine will fail in the next 24 hours based on time series telemetry and metadata.

The solution includes: feature engineering, model training with MLflow tracking, API deployment using FastAPI, and containerization with Docker.

---

## Results Summary

| Metric    | Value (baseline) | Value (tuned) |
| --------- | ---------------- | ------------- |
| AUC       | 0.82             | 0.87          |
| F1-score  | 0.28             | 0.34          |
| Precision | 0.51             | 0.57          |
| Recall    | 0.20             | 0.25          |

The tuned model uses XGBoost with custom `scale_pos_weight`, `max_depth`, and `learning_rate`.

---

## Key Decisions

- **Model**: XGBoost chosen for its performance with tabular data and ability to handle imbalance.
- **Tracking**: MLflow used to compare multiple training runs with metrics and parameters.
- **Deployment**: FastAPI selected for its speed and built-in documentation.
- **Portability**: Docker ensures the system runs anywhere without manual setup.
- **Model access**: Models are loaded directly from MLflow using `run_id` instead of pickle files.

---

## Trade-offs

| Choice                          | Trade-off                            |
| ------------------------------- | ------------------------------------ |
| MLflow local tracking           | Easy to use, but not remote-sharable |
| Training without `errors.csv` | Faster, but less feature-rich        |
| Static API model load           | Simple, but not auto-updatable       |

---

## Lessons Learned

- Docker builds often fail due to strict package versions; minimal and clean `requirements.txt` is key.
- MLflow `run_id` handling is critical for reproducibility.
- FastAPI is excellent for ML inference, but care must be taken with data types and JSON schema.
- `mlruns/` must be included in the Docker image when using local tracking.

---

## Next Steps

- Add `errors.csv` and `maint.csv` to enrich features
- Implement logging and monitoring inside the API
- Deploy the container to a public cloud service (Render, Railway, AWS)
- Move MLflow to a remote tracking server
- Automate training + deployment via GitHub Actions or similar
