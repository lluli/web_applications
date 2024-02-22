from lib.AlbumRepository import * 
from lib.database_connection import * 
from lib.Album import * 

def test_get_all_albums(db_connection):
    albums = AlbumRepository(db_connection)
    assert albums.all() == [Album(1, 'Janky Star', 2022, 1), Album(2, 'Malibu', 2016, 2)]


def test_return_album_from_the_id(db_connection):
    albums = AlbumRepository(db_connection)
    assert albums.find(1) == Album(1, 'Janky Star', 2022, 1)

def test_creating_an_album(db_connection):
    albums = AlbumRepository(db_connection)
