
from api.register.register_api import RegisterAPI
from utils.read_data import read_json

register_api = RegisterAPI()

def test_register():
    payload = read_json("test_data/registor_data.json")


    response = register_api.register(payload)
    # assert response.status_code in [201,200]
    res_json = response.json()

    print(res_json)
    # first = res_json["data"]["firstName"]
    # print("Message:", first)



