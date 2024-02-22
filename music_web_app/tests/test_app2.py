# import json 
# # def test_example(web_client):
# #     response = web_client.get("/users")
# #     assert response.status_code == 200


# # GET /books
# # 2. Use Postman to send some requests
# #    - `GET "http://127.0.0.1:5000/users/"` should return a list of all the users
# #    - `GET "http://127.0.0.1:5000/users/1"` should return the user with an `id` of `1`. What happens if you use an `id`, like `100`, that doesn't correspond to an existing user?
# #    - `POST "http://127.0.0.1:5000/users"` can be used to create new user - [you'll need to provide params](#params). What happens if you omit the params?
# #    - `PUT "http://127.0.0.1:5000/users/1"` can be used to update a user - [you'll need to provide params](#params). What happens if you omit the params and / or use an invalid `id`?
# #    - `DELETE "http://127.0.0.1:5000/users/1"` will delete the user with an ad of `1`


# def test_get_all_users(web_client): # Note web_client fixture, see conftest.py
#     # We seed our database with the book store seed file

#     # We make a GET request to /books
#     response = web_client.get("/users")

#     # We assert that the response status code is 200
#     assert response.status_code == 200

#     # We assert that the response data is the same as the string we expect
#     assert response.json == [{"id": 1, "username": "john"}, {"id": 2, "username": "jane"}, {"id": 3, "username": "alice"}]

# def test_get_specific_users(web_client): 
#     response = web_client.get("/users/1")
#     assert response.status_code == 200
#     assert response.json == {"id": 1, "username": "john"}

# def test_specific_user_wrong_id(web_client): 
#     response = web_client.get("/users/20993")
#     assert response.status_code == 404
#     assert response.json == {'error': 'User not found'}

# def test_get_create_users(web_client):
#     users = web_client.get("/users")
#     response = web_client.post("/users", json={'username': 'josh'})
#     assert response.status_code == 201
#     assert response.json == {"id": 4, "username": "josh"}

#     # Assuming `users` is a list containing user data
# def test_create_user_with_no_username(web_client): 
#     response = web_client.post("/users", json={})
#     assert response.status_code == 400
#     assert response.json == {'error': "Username is required"}

# def test_update_user(web_client): 
#     response = web_client.put("/users/4", json={'username': 'pete'})
#     assert response.status_code == 200
#     assert response.json == {"id": 4, "username": "pete"}

# def test_delete_user(web_client): 
#     response = web_client.delete("/users/4")
#     assert response.status_code == 200
#     assert response.json == {'message': 'User deleted'}

