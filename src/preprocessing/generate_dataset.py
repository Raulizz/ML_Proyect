import pandas as pd
from datetime import timedelta

# Cargar archivos
telemetry = pd.read_csv("data/raw/PdM_telemetry.csv", parse_dates=["datetime"])
failures = pd.read_csv("data/raw/PdM_failures.csv", parse_dates=["datetime"])
machines = pd.read_csv("data/raw/PdM_machines.csv")

# 1. Agregar features estadísticas (rolling window = 3h)
telemetry.sort_values(by=["machineID", "datetime"], inplace=True)
rolling = telemetry.groupby("machineID").rolling("3h", on="datetime").agg({
    "volt": ["mean", "std"],
    "rotate": ["mean", "std"],
    "pressure": ["mean", "std"],
    "vibration": ["mean", "std"]
}).reset_index()

rolling.columns = ["machineID", "datetime",
                   "volt_mean", "volt_std",
                   "rotate_mean", "rotate_std",
                   "pressure_mean", "pressure_std",
                   "vibration_mean", "vibration_std"]

# 2. Crear target: ¿falla en las próximas 24h?
failures["failure_within_24h"] = 1
df = pd.merge_asof(rolling.sort_values("datetime"),
                   failures[["datetime", "machineID", "failure_within_24h"]]
                   .sort_values("datetime"),
                   by="machineID",
                   on="datetime",
                   direction="forward",
                   tolerance=pd.Timedelta("24h"))

df["failure_within_24h"] = df["failure_within_24h"].fillna(0).astype(int)

# 3. Añadir info de máquina
df = df.merge(machines, on="machineID", how="left")

# 4. Guardar dataset listo
df.to_csv("data/processed/train_dataset.csv", index=False)
print("✅ Dataset procesado y guardado en 'data/processed/train_dataset.csv'")