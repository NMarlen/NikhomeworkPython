import os

BASE_URL = os.getenv("YOUGILE_BASE_URL", "https://ru.yougile.com/api-v2")
API_KEY = os.getenv("YOUGILE_API_KEY", "").strip()

def get_bearer_token() -> str:
    return API_KEY  # ключ из .env/окружения

def auth_headers():
    headers = {"Content-Type": "application/json"}
    if API_KEY:
        headers["Authorization"] = f"Bearer {API_KEY}"
    return headers
