# Adding ablums route
# POST /albums
# title: 'Malibu' 
# release_year: 2016
# artist_id: 2 
#  Expected response (200 OK):

from lib.Album import * 


def test_adding_an_album(db_connection, web_client):
    db_connection.seed('seeds/music_store.sql')
    response = web_client.post("/albums", data={'title': 'Malibu', 'release_year': '2016', 'artist_id': '2'})
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ''

# GET /albums
# Album(1, 'Janky Star', 2022)
# Album(2, 'Malibu', 2016)
#  Expected response (200 OK):

def test_viewing_all_albums(web_client):
    response = web_client.get("/albums")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == [Album(1, 'Janky Star', 2022, 1),Album(2, 'Malibu', 2016, 2)]
