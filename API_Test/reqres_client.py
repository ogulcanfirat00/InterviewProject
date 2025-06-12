import requests
from config_api import API_BASE_URL
from utils import logger, retry

class ReqresClient:
    def __init__(self):
        self.base_url = API_BASE_URL
        self.headers = {
            "Content-Type": "application/json",
            "x-api-key": "reqres-free-v1"
        }

    def create_user(self, payload):
        return retry(lambda: requests.post(f"{self.base_url}/users", json=payload, headers=self.headers))

    def get_user(self, user_id):
        return retry(lambda: requests.get(f"{self.base_url}/users/{user_id}", headers=self.headers))

    def update_user(self, user_id, payload):
        return retry(lambda: requests.put(f"{self.base_url}/users/{user_id}", json=payload, headers=self.headers))

    def delete_user(self, user_id):
        return retry(lambda: requests.delete(f"{self.base_url}/users/{user_id}", headers=self.headers))


