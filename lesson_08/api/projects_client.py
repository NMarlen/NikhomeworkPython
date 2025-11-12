import requests
from urllib.parse import urljoin
from typing import Dict, Any
from ..settings import BASE_URL, auth_headers

class ProjectsClient:
    def __init__(self):
        self.s = requests.Session()
        self.s.headers.update(auth_headers())

    def create(self, payload: Dict[str, Any]):
        return self.s.post(urljoin(BASE_URL + "/", "projects"), json=payload)

    def get(self, project_id: str):
        return self.s.get(urljoin(BASE_URL + "/", f"projects/{project_id}"))

    def update(self, project_id: str, payload: Dict[str, Any]):
        return self.s.put(urljoin(BASE_URL + "/", f"projects/{project_id}"), json=payload)

    @staticmethod
    def unauthorized():
        c = ProjectsClient()
        c.s.headers.clear()
        c.s.headers.update({"Content-Type": "application/json"})
        return c
