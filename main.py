import requests
import datetime as dt
import os
from dotenv import load_dotenv


load_dotenv("E:/Python/EnvironmentVariables/.env")
token = os.getenv("pixela_token")
username = os.getenv("pixela_username")
base_url = "https://pixe.la"
graph_id = "graph1"

# https://docs.python.org/3.9/library/datetime.html#strftime-and-strptime-format-codes
#   %d - Day of the month as a zero-padded decimal number.
#   %m - Month as a zero-padded decimal number.
#   %Y - Year with century as a decimal number.
today = dt.datetime.now().strftime("%Y%m%d")

headers = {
    "X-USER-TOKEN": token,
}


def post(endpoint_url, params):
    url = base_url + endpoint_url
    response = requests.post(url=url, headers=headers, json=params)
    response.raise_for_status()
    print(response.text)


def put(endpoint_url, params):
    url = base_url + endpoint_url
    response = requests.put(url=url, headers=headers, json=params)
    response.raise_for_status()
    print(response.text)


def create_account():
    # Create user account
    endpoint_url = "/v1/users"
    url = base_url + endpoint_url

    params = {
        "token": token,
        "username": username,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }

    response = requests.post(url=url, json=params)
    response.raise_for_status()
    print(response.text)


def create_graph():
    endpoint_url = f"/v1/users/{username}/graphs"

    params = {
        "id": graph_id,
        "name": "Python Training",
        "unit": "hours",
        "type": "float",
        "color": "shibafu",
    }

    post(endpoint_url, params)


def add_pixel():
    quantity = input("How many hours have you worked on Python today? : ")

    endpoint_url = f"/v1/users/{username}/graphs/{graph_id}"

    params = {
        "date": today,
        "quantity": quantity,
    }

    post(endpoint_url, params)


def get_pixel():
    pass


def update_pixel():
    date = input("What date do you want to alter? YYYYMMDD : ")
    quantity = input("How many hours have you worked on Python today? : ")

    endpoint_url = f"/v1/users/{username}/graphs/{graph_id}/{date}"

    params = {
        "quantity": quantity,
    }

    put(endpoint_url, params)


def delete_pixel():
    date = input("What date do you want to delete? YYYYMMDD : ")

    endpoint_url = f"/v1/users/{username}/graphs/{graph_id}/{date}"

    url = base_url + endpoint_url
    response = requests.delete(url=url, headers=headers)
    response.raise_for_status()
    print(response.text)


# create_account()
# create_graph()
# add_pixel()
# get_pixel()
# update_pixel()
delete_pixel()
