import requests
import os

token = os.environ.get("pixela_token")
username = os.environ.get("pixela_username")


base_url = "https://pixe.la"


def create_account():
    # Create user account
    endpoint_url = "/v1/users"
    url = base_url + endpoint_url

    params = {
        "token": token,
        "username": username,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
        # "thanksCode": "",
    }

    response = requests.post(url=url, json=params)
    response.raise_for_status()
    print(response.json())
    print(response.text)
