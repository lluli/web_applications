import os
from flask import Flask, request
from lib.database_connection import get_flask_database_connection
from lib.AlbumRepository import *
from lib.Album import * 

# Create a new Flask app
app = Flask(__name__)

@app.route('/albums', methods=['POST'])
def add_an_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = Album(None, request.form['title'], request.form['release_year'], request.form['artist_id'])
    repository.create(album)
    return '', 200 


@app.route('/albums', methods=['GET'])
def show_all_albums():
    connection = get_flask_database_connection(app)
    reposiory = AlbumRepository(connection)
    albums = reposiory.all()
    return '\n'.join(f"{albums}" for album in albums)







# @app.route('/', methods=['GET'])
# def show_all_albums():
#     connection = get_flask_database_connection(app)
#     reposiory = AlbumRepository(connection)
#     repository.all()


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))


if __name__ == '__main__':
    app.run(debug=True)

