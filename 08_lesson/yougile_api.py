import requests
from requests import Response


class YougileApi:
    def __init__(self, base_url: str, token: str, company_id: str):
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "yougile-id": company_id
        }

    def create_project(self, title: str) -> Response:
        return requests.post(
            f"{self.base_url}/projects", json={"title": title},
            headers=self.headers)

    def get_project(self, project_id: str) -> Response:
        return requests.get(
            f"{self.base_url}/projects/{project_id}", headers=self.headers)

    def update_project(self, project_id: str, new_title: str) -> Response:
        return requests.put(
            f"{self.base_url}/projects/{project_id}",
            json={"title": new_title}, headers=self.headers)
