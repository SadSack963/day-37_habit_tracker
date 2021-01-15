import requests
import os
import datetime as dt

token = os.environ.get("pixela_token")
username = os.environ.get("pixela_username")
base_url = "https://pixe.la"
graph_id = "graph1"

headers = {
    "X-USER-TOKEN": token,
}


def post(endpoint_url, params):
    url = base_url + endpoint_url
    response = requests.post(url=url, headers=headers, json=params)
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
    quantity = input("How many hours have you worked on Python? : ")

    date_now = dt.datetime.now().date()
    year = date_now.year
    month = "{:02d}".format(date_now.month)
    day = "{:02d}".format(date_now.day)
    date = str(year) + str(month) + str(day)
    # print(date)

    endpoint_url = f"/v1/users/{username}/graphs/{graph_id}"

    params = {
        "date": date,
        "quantity": quantity,
    }

    post(endpoint_url, params)


def get_pixel():
    pass


# create_account()
# create_graph()
# add_pixel()
get_pixel()
