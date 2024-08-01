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
