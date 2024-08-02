import sender_stand_request
import data
import pytest

@pytest.fixture
def auth_token():
    new_user = sender_stand_request.create_count(data.user_body)
    response_data = new_user.json()
    if 'authToken' not in response_data:
        raise Exception(f"Error: 'authToken' no se encontró en la respuesta. Respuesta completa: {response_data}")
    return response_data['authToken']

def positive_assert(kit_body, auth_token):
    new_kit = sender_stand_request.create_kit(kit_body, auth_token)
    assert new_kit.status_code == 201
    assert new_kit.json()["name"] == kit_body["name"]

def negative_assert(kit_body, auth_token):
    new_kit = sender_stand_request.create_kit(kit_body, auth_token)
    assert new_kit.status_code == 400

def test_create_kit_name_length_1(auth_token):
    kit_body = data.get_kit_body("a")
    positive_assert(kit_body, auth_token)

def test_create_kit_name_length_511(auth_token):
    kit_body = data.get_kit_body("Abcd" * 127 + "a")
    positive_assert(kit_body, auth_token)

def test_create_kit_name_length_0(auth_token):
    kit_body = data.get_kit_body("")
    negative_assert(kit_body, auth_token)

def test_create_kit_name_length_512(auth_token):
    kit_body = data.get_kit_body("Abcd" * 128)
    negative_assert(kit_body, auth_token)
    print(kit_body)

def test_create_kit_name_special_chars(auth_token):
    kit_body = data.get_kit_body("!@#$%^&*()")
    positive_assert(kit_body, auth_token)

def test_create_kit_name_with_spaces(auth_token):
    kit_body = data.get_kit_body(" A Aaa ")
    positive_assert(kit_body, auth_token)

def test_create_kit_name_with_numbers(auth_token):
    kit_body = data.get_kit_body("123")
    positive_assert(kit_body, auth_token)

def test_create_kit_no_name(auth_token):
    kit_body = {}
    negative_assert(kit_body, auth_token)

def test_create_kit_name_as_number(auth_token):
    kit_body = {"name": 123}
    negative_assert(kit_body, auth_token)
# Nota del auditor: test_create_kit_name_length_512: La prueba intenta crear un kit con un nombre de 512 caracteres. En este caso, su prueba está fallando porque el resultado esperado es el error 400 y está obteniendo el código 200 como respuesta en su prueba. Verifique si realmente se están pasando 512 caracteres en la función. 
#Lo mismo ocurre con las pruebas test_create_kit_name_as_number y test_create_kit_no_name. NOTAS DEL ESTUDIANTE:Estas pruebas estan bien debido a que no esta bien porgramado los requisitos en el codigo, y por ende estan destinadas a fallar, esa es la razon por la que no corresponde los estatus de respuesta de los servidores, por ejemplo el la prueba de los 512: da respuesta 201 en vez de 400, ya que no funciona la restriccion de que no deberia de poder introducirse un nombre de mas de 512 caracteres, pero vemos que si es el caso
