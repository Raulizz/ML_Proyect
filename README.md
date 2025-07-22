# Predictive Maintenance ML API

A full MLOps pipeline for predicting machine failures based on sensor telemetry data. This repository includes data preprocessing, model training and tracking with MLflow, inference with FastAPI, and containerization with Docker.

---

## 🚀 ¡IMPORTANT! For a quick test of the model, go directly to the README.md file in the "ready to use" folder. There you will find instructions on how to run the model quickly.

![1753173605063](image/README/1753173605063.png)

---

## 📂 How to Navigate the Repo

| Folder/File           | Purpose                                                                                                                            |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `api/`              | FastAPI app with `/predict` endpoint                                                                                             |
| `data/`             | Contains raw and processed data                                                                                                    |
| `image/`            | contains images used in thr README file                                                                                            |
| `mlruns/`           | Local MLflow tracking directory                                                                                                    |
| `notebooks/`        | Exploratory data analysis (EDA)                                                                                                    |
| `ready_to_use`      | folder with model + docker                                                                                                         |
| `src/`              | Contains preprocessing and training scripts                                                                                        |
| `venv`              | virtual environment                                                                                                                |
| `.gitignore`        | Prevents local files (e.g. venv/) from being copied                                                                                |
| `README.md`         | usage guide                                                                                                                        |
| `requirements.txt`  | file containing dependencies                                                                                                       |
| `tech_report.md`    | Results obtained, key decisions, trade-offs, lessons learned, and next steps.                                                      |
| `technical_design/` | Describes the architecture, data flow, components, diagrams, and decisions for the implementation of the machine learning project. |



## Proof of Work 

- Integration with GIT + Repository GitHub

[Raulizz/ML_Proyect: It´s a repository for MLOps](https://github.com/Raulizz/ML_Proyect)

![1753177633266](image/README/1753177633266.png)

![1753177657754](image/README/1753177657754.png)

- Models in MLflow + ui

  ![1753177857940](image/README/1753177857940.png)

![1753177940560](image/README/1753177940560.png)

*Model 2 is better than model 1

- API working perfectly

![1753178052330](image/README/1753178052330.png)

- Docker + API

![1753178110063](image/README/1753178110063.png)
