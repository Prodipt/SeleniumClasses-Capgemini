import requests

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

def func1():
    response = requests.post("https://petstore.swagger.io/v2/pet/", json=payload)
    return response.json()['id']

id = func1()

print("ID fetched in POST method : ",id, "\n")

def func2():
    response1 = requests.get(f"https://petstore.swagger.io/v2/pet/{id}")
    print(response1.status_code, "\n")

def func3():
    response3 = requests.delete(f"https://petstore.swagger.io/v2/pet/{id}")
    print("Status Code after deleting the ID using DELETE Method : ", response3.status_code, "\n")


func2()
func3()

# if __name__ == "__main__":
#     id = func1()
#     func2()
#     func3()