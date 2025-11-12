import pytest


@pytest.mark.requires_token
def test_create_project_positive(client, unique_name):
    payload = {"title": unique_name}
    r = client.create(payload)
    assert r.status_code in (200, 201), r.text

    data = r.json()
    project_id = data.get("id") or data.get("project", {}).get("id")
    assert project_id, f"Unexpected create response, no id: {data}"
    pytest.created_project_id = project_id

    r2 = client.get(project_id)
    assert r2.status_code == 200, r2.text
    info = r2.json()
    returned_title = info.get("title") or info.get("name")
    assert returned_title == unique_name, f"Expected title '{unique_name}', got: {info}"


def test_create_project_negative_empty_title(client):
    r = client.create({"title": ""})
    assert r.status_code in (400, 422), f"Expected 400/422, got {r.status_code}: {r.text}"


def test_create_project_negative_unauthorized(client_unauth, unique_name):
    r = client_unauth.create({"title": unique_name})
    assert r.status_code in (401, 403), f"Expected 401/403, got {r.status_code}: {r.text}"


@pytest.mark.requires_token
def test_get_project_positive(client):
    project_id = getattr(pytest, "created_project_id", None)
    assert project_id, "No project created before (create test did not set project_id)"
    r = client.get(project_id)
    assert r.status_code == 200, r.text
    data = r.json()
    assert data.get("id") == project_id
    assert (data.get("title") or data.get("name")), f"No title/name in response: {data}"


def test_get_project_negative_not_found(client):
    r = client.get("non-existent-id-123")
    assert r.status_code in (404, 400), f"Expected 404/400, got {r.status_code}: {r.text}"


@pytest.mark.requires_token
def test_update_project_positive(client):
    project_id = getattr(pytest, "created_project_id", None)
    assert project_id, "No project created before (create test did not set project_id)"
    new_title = "updated_" + project_id[:6]
    r = client.update(project_id, {"title": new_title})
    assert r.status_code in (200, 204), r.text

    r2 = client.get(project_id)
    assert r2.status_code == 200, r2.text
    info = r2.json()
    returned_title = info.get("title") or info.get("name")
    assert returned_title == new_title, f"Expected updated title '{new_title}', got: {info}"


def test_update_project_negative_invalid_payload(client):
    r = client.update("non-existent-id-456", {"title": ""})
    assert r.status_code in (400, 404, 422), f"Expected 400/404/422, got {r.status_code}: {r.text}"

