import requests
import urllib3

urllib3.disable_warnings()
base = "https://www.shoppersstack.com/shopping"

token = ""
UserId = ""

def register():
    body = {
        "city": "Banglore",
        "country": "India",
        "email": "pradipt@gmail.com",
        "firstName": "PP",
        "gender": "MALE",
        "lastName": "LL",
        "password": "123",
        "phone": 7667842116,
        "state": "Rajasthan",
        "zoneId": "ALPHA"
    }

    response = requests.post(f"{base}/shoppers",json=body, verify=False)

    print(response.status_code)
    print(response.json())

    # assert response.status_code == 201

def user_login():
    global token, UserId
    body = {
        "email": "pradipt@gmail.com",
        "password": "123",
        "role": "SHOPPER"
        }

    response = requests.post(f"{base}/users/login", json=body, verify=False)

    print(response.status_code)
    print(response.json())
    token = response.json()["data"]['jwtToken']
    UserId = response.json()["data"]['userId']
    print(f"Token value: {token}")
    print(f"User Id: {UserId}")

def get_user_info_byID():
    header = { "Authorization": f"Bearer {token}"}
    response = requests.get(f"{base}/shoppers/{UserId}",
                headers=header, verify=False)
    print(response.status_code)
    print(response.json())

register()
user_login()
get_user_info_byID()