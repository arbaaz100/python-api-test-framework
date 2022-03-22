import pytest
import requests
import json
import jsonpath


# Setting up the base variables
baseUrl = "https://gorest.co.in/"
service = "/public-api/users"
file = open('TestData/user.json', "r")
inputData = json.loads(file.read())
user_id = ""


# Setting up Authentication Token
@pytest.fixture()
def AUTH_TOKEN():
    return "?access-token=" + str(inputData["Authentication Token"])


# Test to get a list of all users
def test_get_all_users():
    path = service
    response = requests.get(url=baseUrl + path)
    responseJson = json.loads(response.text)
    assert response.status_code == 200
    print(responseJson)


# Create New User and save its User Id
def test_create_user_and_get_user_id(AUTH_TOKEN):
    path = service + AUTH_TOKEN
    response = requests.post(url=baseUrl + path, json=inputData["primary user"])
    responseJson = json.loads(response.text)
    assert response.status_code == 200 or response.status_code == 201
    print(responseJson)
    global user_id
    user_id = str(jsonpath.jsonpath(responseJson, '$.data.id')[0])


# Validate that the New User has been added successfully
def test_get_user_data(AUTH_TOKEN):
    path = service + "/" + user_id + AUTH_TOKEN
    response = requests.get(url=baseUrl + path)
    responseJson = json.loads(response.text)
    print(responseJson)
    assert response.status_code == 200
    assert jsonpath.jsonpath(responseJson, '$.data.name')[0] == inputData["primary user"]["name"]
    assert jsonpath.jsonpath(responseJson, '$.data.email')[0] == inputData["primary user"]["email"]
    assert jsonpath.jsonpath(responseJson, '$.data.gender')[0] == inputData["primary user"]["gender"]
    assert jsonpath.jsonpath(responseJson, '$.data.status')[0] == inputData["primary user"]["status"]


# Update the Data for New User created
def test_put_user_data(AUTH_TOKEN):
    path = service + "/" + user_id + AUTH_TOKEN
    response = requests.put(url=baseUrl + path, data=inputData["updated user"])
    print(baseUrl + path)
    responseJson = json.loads(response.text)
    assert response.status_code == 200
    print(responseJson)
    assert jsonpath.jsonpath(responseJson, '$.data.name')[0] == inputData["updated user"]["name"]
    assert jsonpath.jsonpath(responseJson, '$.data.email')[0] == inputData["updated user"]["email"]
    assert jsonpath.jsonpath(responseJson, '$.data.gender')[0] == inputData["updated user"]["gender"]
    assert jsonpath.jsonpath(responseJson, '$.data.status')[0] == inputData["updated user"]["status"]


# Delete the created New User
def test_delete_user(AUTH_TOKEN):
    path = service + "/" + user_id + AUTH_TOKEN
    response = requests.delete(url=baseUrl + path)
    responseJson = json.loads(response.text)
    print(responseJson)
    assert response.status_code == 200


# Validate that the User has been deleted Successfully
def test_validate_user_has_been_deleted(AUTH_TOKEN):
    path = service + "/" + user_id + AUTH_TOKEN
    response = requests.get(url=baseUrl + path)
    responseJson = json.loads(response.text)
    assert response.status_code == 200
    print(responseJson)
    assert jsonpath.jsonpath(responseJson, '$.data.message')[0] == 'Resource not found'
