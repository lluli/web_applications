
# {{ NAME }} Route Design Recipe

_Copy this design recipe template to test-drive a plain-text Flask route._

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
# EXAMPLE

# Adding ablums route
POST /albums
title string
release_year number
artist_id number

# Home route
GET /albums

```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python
# EXAMPLE

# GET /albums
# Album(1, 'Janky Star', 2022)
# Album(2, 'Malibu', 2016)
#  Expected response (200 OK):
"""
def test_viewing_all_albums(web_client):
    response = web_client.get("/albums")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Album(2, Voyage, 2022), Album(2, 'Malibu', 2016)"
"""

# Adding ablums route
# POST /albums
# title: 'Malibu' 
# release_year: 2016
# artist_id: 2 
#  Expected response (200 OK):
"""
def test_adding_an_album(web_client):
    response = web_client.post("/albums/title=?release_year=")

"""


## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python

# Adding ablums route
# POST /albums
# title: 'Malibu' 
# release_year: 2016
# artist_id: 2 
#  Expected response (200 OK):

def test_adding_an_album(web_client):
    response = web_client.post("/albums/title=?release_year=")


# GET /albums
# Album(1, 'Janky Star', 2022)
# Album(2, 'Malibu', 2016)
#  Expected response (200 OK):

def test_viewing_all_albums(web_client):
    response = web_client.get("/albums")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Album(2, Voyage, 2022,1 ), Album(2, 'Malibu', 2016, 2)"





