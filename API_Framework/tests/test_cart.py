from api.cart.cart_api import CartAPI
from utils.read_data import read_json
from core.auth import get_auth_data

cart_api = CartAPI()

def test_add_to_cart(auth_data, headers):

    payload = read_json("test_data/cart_data.json")
    details = get_auth_data()
    shopper_id = details["shopper_id"]
    response = cart_api.cart(shopper_id,payload, headers)
    assert response.status_code in [201,200,409]

def tests_get_cart(auth_data, headers):

    details = get_auth_data()
    shopper_id = details["shopper_id"]
    response = cart_api.get_cart(shopper_id, headers)
    res_json = response.json()
    file = res_json["data"]
    print(file)

    assert response.status_code == 200