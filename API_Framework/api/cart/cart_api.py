from core.base_api import BaseAPI
from utils.config import BASE_URL

class CartAPI:

    def __init__(self):
        self.api = BaseAPI(BASE_URL)

    def cart(self, shopper_id, payload, headers):
        return self.api.post(f"/shoppers/{shopper_id}/carts", json=payload, headers=headers)

    def get_cart(self,shopperId, headers):
        return self.api.get(f"/shoppers/{shopperId}/carts", headers=headers)