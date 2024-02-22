import os
from flask import Flask, request
from lib.database_connection import *

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

@app.route('/add_name', methods=['GET'])
def add_name():
    name = request.args['name']
    names = 'Julia, Alice, Karim'
    return f'{names}, {name}'



@app.route('/sort-names', methods=['POST'])
def order_names():
    names = request.form['names'].split(',')
    ordered_names = sorted(names)
    return ','.join(ordered_names)


@app.route('/count_vowels', methods=['POST'])
def count_vowels():
    word = request.form['text']    
    vowel_count = 0
    vowel_count = [vowel_count + 1 for letter in word if letter in 'aeiou']
    return f'There are {sum(vowel_count)} vowels in "{word}"'







#  @app.route('/books', methods=['POST'])
#     def create_book():
#         connection = get_flask_database_connection(app)
#         repository = BookRepository(connection)
#         book = Book(None, request.form['title'], request.form['author_name'])
#         book = repository.create(book)
#         return "Book added successfully"


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

