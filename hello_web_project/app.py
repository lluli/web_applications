import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

@app.route('/wave', methods=['GET'])
def wave():
    name = request.args.get('name')

    # Send back a fond farewell with the name
    return f"I am waving at {name}"

# @app.route('/hello', methods=['GET'])
# def hello():curl
#     name = request.args['name'] # The value is 'David'

#     # Send back a friendly greeting with the name
#     return f"Hello {name}!"

# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
# @app.route('/emoji', methods=['GET'])
# def get_emoji():
#     return ":)"

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

