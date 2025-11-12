import os
from pathlib import Path
import pytest
import uuid
from .api.projects_client import ProjectsClient
from .settings import get_bearer_token

try:
    from dotenv import load_dotenv
    root = Path(__file__).resolve().parents[1]
    load_dotenv(root / ".env")
except Exception:
    pass


@pytest.fixture(scope="session")
def client():
    return ProjectsClient()


@pytest.fixture(scope="session")
def client_unauth():
    return ProjectsClient.unauthorized()


@pytest.fixture
def unique_name():
    return f"autotest_{uuid.uuid4().hex[:8]}"


@pytest.fixture(autouse=True)
def _skip_if_no_auth_for_positive(request):
    if request.node.get_closest_marker("requires_token"):
        token = get_bearer_token()
        if not token:
            pytest.skip("Нет авторизации: ни YOUGILE_API_KEY в .env/окружении")

