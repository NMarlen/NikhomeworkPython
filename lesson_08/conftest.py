# lesson_08/conftest.py
import os
from pathlib import Path

# 1) подхватить .env из корня проекта
try:
    from dotenv import load_dotenv
    # root = .../NikhomeworkPython
    root = Path(__file__).resolve().parents[1]
    load_dotenv(root / ".env")
except Exception:
    pass  # если плагина нет, просто пропустим

import pytest
import uuid
from .api.projects_client import ProjectsClient
from .settings import get_bearer_token  # или auth_headers/get_bearer_token — как у тебя

@pytest.fixture(scope="session")
def client():
    return ProjectsClient()

@pytest.fixture(scope="session")
def client_unauth():
    return ProjectsClient.unauthorized()

@pytest.fixture
def unique_name():
    import uuid
    return f"autotest_{uuid.uuid4().hex[:8]}"

@pytest.fixture(autouse=True)
def _skip_if_no_auth_for_positive(request):
    if request.node.get_closest_marker("requires_token"):
        token = get_bearer_token()  # если у тебя функция иначе называется — поправь
        if not token:
            pytest.skip("Нет авторизации: ни YOUGILE_API_KEY в .env/окружении")
