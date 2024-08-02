import configuration
import data
import requests



def create_count(body):
    print( configuration.URL_SERVICE + configuration.CREATE_USER_PATH)
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        json=body,
        headers=data.headers
    )


def create_kit(kit_body, auth_token):
    # Verificar que auth_token no esté vacío
    if not auth_token:
        raise ValueError("El auth_token no puede estar vacío")

    # Verificar que auth_token no exceda los 511 caracteres
    if len(auth_token) > 512:
        raise ValueError("El auth_token no puede tener más de 511 caracteres")

    headers = data.headers.copy()
    headers['Authorization'] = f'Bearer {auth_token}'
    return requests.post(
        configuration.URL_SERVICE + configuration.KITS_PATH,
        json=kit_body,
        headers=headers
    )
