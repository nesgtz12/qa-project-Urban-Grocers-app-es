user_body = {
    "firstName": "Andrea",
    "phone": "+10005553535",
    "address": "Manuel Acuña 2212",
    "metroStation": "4",
    "rentTime": 5,
    "deliveryDate": "2023-10-10",
    "comment": "Prueba"
}

headers = {
    "Content-Type": "application/json"
}

def get_kit_body(name):
    return {
        "name": name
    }
