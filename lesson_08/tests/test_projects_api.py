# lesson_08/tests/test_projects_api.py
# Тесты Yougile Projects API (POST/GET/PUT) под pytest + requests.
# Позитивные тесты помечены @pytest.mark.requires_token — они скипнутся, если нет API-ключа.
# Особенность API: POST /projects может вернуть только {"id": "..."} без поля title/name,
# поэтому для проверки имени используем дополнительный GET /projects/{id}.

import pytest


# ---------------------- POST /projects ----------------------

@pytest.mark.requires_token
def test_create_project_positive(client, unique_name):
    """Создание проекта с корректным title: проверяем через follow-up GET"""
    payload = {"title": unique_name}
    r = client.create(payload)
    assert r.status_code in (200, 201), r.text

    data = r.json()
    # На create сервер может вернуть только {"id": "..."} — это ОК.
    project_id = data.get("id") or data.get("project", {}).get("id")
    assert project_id, f"Unexpected create response, no id: {data}"
    # Сохраняем id для следующих позитивных тестов
    pytest.created_project_id = project_id

    # Подтверждаем корректность через GET
    r2 = client.get(project_id)
    assert r2.status_code == 200, r2.text
    info = r2.json()
    returned_title = info.get("title") or info.get("name")
    assert returned_title == unique_name, f"Expected title '{unique_name}', got: {info}"


def test_create_project_negative_empty_title(client):
    """Создание проекта с пустым названием — ожидаем валидационную ошибку"""
    r = client.create({"title": ""})
    assert r.status_code in (400, 422), f"Expected 400/422, got {r.status_code}: {r.text}"


def test_create_project_negative_unauthorized(client_unauth, unique_name):
    """Создание проекта без авторизации — ожидаем 401/403"""
    r = client_unauth.create({"title": unique_name})
    assert r.status_code in (401, 403), f"Expected 401/403, got {r.status_code}: {r.text}"


# ---------------------- GET /projects/{id} ----------------------

@pytest.mark.requires_token
def test_get_project_positive(client):
    """Получение ранее созданного проекта"""
    project_id = getattr(pytest, "created_project_id", None)
    assert project_id, "No project created before (create test did not set project_id)"
    r = client.get(project_id)
    assert r.status_code == 200, r.text
    data = r.json()
    assert data.get("id") == project_id
    assert (data.get("title") or data.get("name")), f"No title/name in response: {data}"


def test_get_project_negative_not_found(client):
    """GET по несуществующему ID — ожидаем 404/400"""
    r = client.get("non-existent-id-123")
    assert r.status_code in (404, 400), f"Expected 404/400, got {r.status_code}: {r.text}"


# ---------------------- PUT /projects/{id} ----------------------

@pytest.mark.requires_token
def test_update_project_positive(client):
    """Обновление названия проекта: PUT, затем верификация через GET"""
    project_id = getattr(pytest, "created_project_id", None)
    assert project_id, "No project created before (create test did not set project_id)"

    new_title = "updated_" + project_id[:6]
    r = client.update(project_id, {"title": new_title})
    # Некоторые инсталляции могут вернуть 204 No Content — это тоже ОК
    assert r.status_code in (200, 204), r.text

    r2 = client.get(project_id)
    assert r2.status_code == 200, r2.text
    info = r2.json()
    returned_title = info.get("title") or info.get("name")
    assert returned_title == new_title, f"Expected updated title '{new_title}', got: {info}"


def test_update_project_negative_invalid_payload(client):
    """Обновление с некорректными данными — ожидаем 400/404/422"""
    r = client.update("non-existent-id-456", {"title": ""})
    assert r.status_code in (400, 404, 422), f"Expected 400/404/422, got {r.status_code}: {r.text}"
