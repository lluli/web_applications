
# {{ NAME }} Route Design Recipe

_Copy this design recipe template to test-drive a plain-text Flask route._

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
# EXAMPLE

# Request:
GET /names?add=Eddie

# This route should return a list of pre-defined names, plus the name given.

# Expected response (2OO OK):
Julia, Alice, Karim, Eddie
```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python
# EXAMPLE

# GET /names?add=Eddie
#  Expected response (200 OK):
"""
Adds Eddie to list of preditermined names 
"""

```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
"""
Sorts a list of names in alpahbetical order 
  Expected response (200 OK):
  'Alice,Joe,Julia,Kieran,Zoe'
"""
def test_names_are_sorted_in_order():
    response = web_client.post('/names?add=Eddie', data={'name': 'Eddie'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Julia, Alice, Karim, Eddie'

"""

```

