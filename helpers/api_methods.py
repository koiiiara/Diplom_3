import random
import requests
from data.urls import ApiUrls


class UserMethods:

    def create_user(self, email, name, password):
        payload = {}
        if name:
            payload["name"] = name
        if password:
            payload["password"] = password
        if email:
            payload["email"] = email

        response = requests.post(ApiUrls.USER_REGISTER_URL, data=payload)
        return response.status_code, response.json()

    def delete_user(self, token):
        headers = {
            'Authorization': token,
        }
        response = requests.delete(ApiUrls.USER_URL, headers=headers)
        return response.status_code, response.json()


class OrderMethods:

    def create_order(self, ingredients, token):
        payload = {"ingredients": ingredients}
        if token:
            headers = {"Authorization": token}
            response = requests.post(ApiUrls.ORDER_URL, data=payload, headers=headers)
        else:
            response = requests.post(ApiUrls.ORDER_URL, data=payload)
        return response.status_code, response

    def get_ingredients(self):
        response = requests.get(ApiUrls.INGREDIENTS_URL)
        if response.status_code == 200:
            return response.json()["data"]
        else:
            return None

    def get_random_ingredients_ids(self, count):
        order_methods = OrderMethods()
        ingredients_full = order_methods.get_ingredients()
        ingredients = []
        for i in range(count):
            ingredient = random.choice(ingredients_full)
            ingredients.append(ingredient["_id"])
        return ingredients
