import pandas as pd
from datetime import timedelta

# Upload files
telemetry = pd.read_csv("data/raw/PdM_telemetry.csv", parse_dates=["datetime"])
failures = pd.read_csv("data/raw/PdM_failures.csv", parse_dates=["datetime"])
machines = pd.read_csv("data/raw/PdM_machines.csv")

# Add Statistical Features Using a 3-Hour Rolling Window
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

# Create Target: Will It Fail in the Next 24 Hours?
failures["failure_within_24h"] = 1
df = pd.merge_asof(rolling.sort_values("datetime"),
                   failures[["datetime", "machineID", "failure_within_24h"]]
                   .sort_values("datetime"),
                   by="machineID",
                   on="datetime",
                   direction="forward",
                   tolerance=pd.Timedelta("24h"))

df["failure_within_24h"] = df["failure_within_24h"].fillna(0).astype(int)

# Add Machine Information
df = df.merge(machines, on="machineID", how="left")

# Save Final Dataset
df.to_csv("data/processed/train_dataset.csv", index=False)
print("Processed Dataset Saved in 'data/processed/train_dataset.csv'")