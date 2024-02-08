import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

def get_backend_connection_server():
    BACKEND_SEVER: str = os.getenv("BACKEND_SERVER")

    return BACKEND_SEVER