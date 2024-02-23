from lib.Album import * 


"""
Album constructs with a title, release_year, artist_id
"""
def test_book_constructs():
    album = Album(1, "Test Title", 2000, 1)
    assert album.id == 1
    assert album.title == "Test Title"
    assert album.release_year == 2000
    assert album.artist_id == 1

"""
We can format albums to strings nicely
"""
def test_albums_format_nicely():
    album = Album(1, "Test Title", 2000, 1)
    assert str(album) == "Album(1, Test Title, 2000, 1)"
    # Try commenting out the `__repr__` method in lib/book.py
    # And see what happens when you run this test again.

"""
We can compare two identical albums
And have them be equal
"""
def test_albums_are_equal():
    album1 = Album(1, "Test Title", "Test Release Year", "Test Artist ID")
    album2 = Album(1, "Test Title", "Test Release Year", "Test Artist ID")
    assert album1 == album2
    # Try commenting out the `__eq__` method in lib/book.py
    # And see what happens when you run this test again.
