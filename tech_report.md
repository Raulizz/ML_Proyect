# Technical Report

## Project Summary

This project demonstrates a full MLOps workflow applied to predictive maintenance. The goal is to detect whether a machine will fail in the next 24 hours based on time series telemetry and metadata.

tools and focus: feature engineering, model training with MLflow tracking, API deployment using FastAPI, and containerization with Docker.

---


## Key Decisions

- **Model**: XGBoost chosen for its performance with tabular data and ability to handle imbalance.
- **Tracking**: MLflow used to compare multiple training runs with metrics and parameters.
- **Deployment**: FastAPI selected for its speed and built-in documentation.
- **Portability**: Docker ensures the system runs anywhere without manual setup.

---

## Trade-offs

| Choice                          | Trade-off                            |
| ------------------------------- | ------------------------------------ |
| MLflow local tracking           | Easy to use, but not remote-sharable |
| Training without `errors.csv` | Faster, but less feature-rich        |
| Static API model load           | Simple, but not auto-updatable       |

---

## Lessons Learned

- A good project encompasses everything an ML engineer should know. I really enjoyed it and learned a lot. From a general perspective, it explains how the process of creating an MLops from scratch is carried out.

---

## Next Steps

- Deploy the container to a cloud service (GCP, AZURE, AWS)
- Automate training + deployment via GitHub Actions or similar
