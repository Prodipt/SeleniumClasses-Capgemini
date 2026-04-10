# TASK 01 : 06-04
# Execution flow:
# 1. Register new user
# 2. Login to get token and userId
# 3. Fetch user details using token


import requests
import urllib3

# Disable SSL warnings (because we are using verify=False in requests)
urllib3.disable_warnings()

# Base URL for all API endpoints
base = "https://www.shoppersstack.com/shopping"

# Global variables to store token and userId after login
token = ""
UserId = ""

session = requests.Session()

def register():
    # Request body for user registration
    body = {
        "city": "Bangalore",
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

    # Sending POST request to create a new shopper
    # verify=False skips SSL certificate validation (used only for testing)
    response = session.post(f"{base}/shoppers", json=body, verify=False)

    # Print response status and data to verify registration
    print(response.status_code)
    print(response.json())

    # Assertion can be used in testing to validate expected result
    # assert response.status_code == 201


def user_login():
    global token, UserId  # Allows modification of global variables

    # Login request body
    body = {
        "email": "pradipt@gmail.com",
        "password": "123",
        "role": "SHOPPER"
    }

    # Sending POST request to login user
    response = session.post(f"{base}/users/login", json=body, verify=False)

    # Print response for debugging/verification
    print(response.status_code)
    print(response.json())

    # Extract JWT token and userId from response JSON
    token = response.json()["data"]['jwtToken']
    UserId = response.json()["data"]['userId']

    # Print extracted values for confirmation
    print(f"Token value: {token}")
    print(f"User Id: {UserId}")


def get_user_info_byID():
    # Create Authorization header using Bearer token
    header = { "Authorization": f"Bearer {token}"}

    # Sending GET request to fetch user details by userId
    # Header is required because this is a protected API
    response = session.get(
        f"{base}/shoppers/{UserId}",
        headers=header,
        verify=False
    )

    # Print response status and user data
    print(response.status_code)
    print(response.json())

register()
user_login()
get_user_info_byID()