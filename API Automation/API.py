
# Imported Requests
import requests

# Fetching the data

#### GET METHOD

# response = requests.get("https://petstore.swagger.io/v2/store/inventory")

# response = requests.get("https://petstore.swagger.io/v2/pet/findByStatus?status=sold")

# Using the response variable
# print(response.text)
# print(response.status_code)
# print(response.json())
# print(response.json()['Busy'])
#
# expected = 200
# actual = response.status_code
#
# assert expected == actual , f"Not Equal {actual}"

# expected = 201
# actual = response.status_code
#
# assert expected == actual , "Not Equal"

#### POST METHOD

payload = {
  "id": 111,
  "category": {
    "id": 5,
    "name": "string"
  },
  "name": "xyz",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

response = requests.post("https://petstore.swagger.io/v2/pet/", json=payload)

expected = 200
actual = response.status_code

assert actual == expected , f"Status: {actual}"

# print(response.status_code)

print(response.json())

def func1():
    return response.json()['id']


val = func1()
print("ID fetched in POST method : ",val)

### DELETE METHOD

response1 = requests.delete(f"https://petstore.swagger.io/v2/pet/{val}")

def func2():
    print("Status Code after deleting the ID using DELETE Method : ", response1.status_code)

func2()
# print(response1.json())

# print(response1.status_code)

