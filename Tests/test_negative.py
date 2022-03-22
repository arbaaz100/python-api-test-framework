import pytest
import requests
import json
import jsonpath


# Setting up the base variables
baseUrl = "https://gorest.co.in/"
service = "/public-api/users"
file = open('TestData/user.json', "r")
inputData = json.loads(file.read())
non_existent_user_id = "123"


# Setting up Incorrect Authentication Token
@pytest.fixture()
def WRONG_AUTH_TOKEN():
    return "?access-token=" + str(inputData["Wrong Authentication Token"])


# Setting up Correct Authentication Token
@pytest.fixture()
def AUTH_TOKEN():
    return "?access-token=" + str(inputData["Authentication Token"])


# Validate new user can not be created with wrong Authentication Token
def test_delete_user_with_incorrect_auth(WRONG_AUTH_TOKEN):
    path = service + WRONG_AUTH_TOKEN
    response = requests.post(url=baseUrl + path, json=inputData["primary user"])
    responseJson = json.loads(response.text)
    assert response.status_code == 200
    assert jsonpath.jsonpath(responseJson, '$.data.message')[0] == "Authentication failed"
    print(responseJson)


# Validate that a Non-Existent User can not be deleted
def test_delete_non_existent_user(AUTH_TOKEN):
    path = service + "/" + non_existent_user_id + AUTH_TOKEN
    response = requests.delete(url=baseUrl + path)
    responseJson = json.loads(response.text)
    assert response.status_code == 200
    assert jsonpath.jsonpath(responseJson, '$.data.message')[0] == "Resource not found"
    print(responseJson)

