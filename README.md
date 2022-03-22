# Pytest - API testing with Python `requests`

#### Pytest is a mature full-featured Python testing frame that helps you write and run tests in Python.

#### The `requests` module allows you to send HTTP requests using Python.

## Getting started

* To download and install `pytest`, run this command from the terminal : `pip install pytest`
* To download and install `requests`, run this command from the terminal : `pip install requests`
* To download and install `pytest-html`, run this command from the terminal : `pip install pytest-html`

To ensure all dependencies are resolved in a CI environment, in one go, add them to a `requirements.txt` file.
* Then run the following command : `pip install -r requirements.txt`

By default pytest only identifies the file names starting with `test_` or ending with `_test` as the test files.

Pytest requires the test method names to start with `test`. All other method names will be ignored even if we explicitly ask to run those methods.

A sample test below :

```python
# Test to get a list of all users
def test_get_all_users():
    path = service
    response = requests.get(url=baseUrl + path)
    responseJson = json.loads(response.text)
    assert response.status_code == 200
    print(responseJson)

```
## Running tests

If your tests are contained inside a folder 'Tests', then run the following command : `pytest Tests` 

If you want HTML Reports after Tests' Execution, then run the following command : `pytest --html=report.html`

To generate xml results, run the following command : `pytest Tests --junitxml="result.xml"`

For more on Pytest, go [here.](https://docs.pytest.org/en/stable/)
