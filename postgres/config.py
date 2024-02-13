import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv(dotenv_path="/Users/quangtn/Desktop/01_work/01_job/02_ml/PySpark/HeartStrokePrediction/env")

def get_setting():
    POSTGRES_USER : str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER : str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT : str = os.getenv("POSTGRES_PORT", 5432)
    POSTGRES_DB : str = os.getenv("POSTGRES_DB", "tdd")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

    return DATABASE_URL

if __name__ == "__main__":
    get_setting()