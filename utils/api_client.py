import requests

class APIClient:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    def create_project(self, tenant_id, name, description):
        endpoint = f"{self.base_url}/api/v1/projects"
        headers = {**self.headers, "X-Tenant-ID": tenant_id}
        payload = {
            "name": name, 
            "description": description, 
            "team_members": []
        }
        # Using a timeout is a best practice for CI/CD environments
        response = requests.post(endpoint, json=payload, headers=headers, timeout=10)
        return response