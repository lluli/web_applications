from playwright.sync_api import Page, expect

# Tests for your routes go here

# === Example Code Below ===

"""
We can get an emoji from the /emoji page
"""
# def test_get_emoji(page, test_web_address): # Note new parameters
#     # We load a virtual browser and navigate to the /emoji page
#     page.goto(f"http://{test_web_address}/emoji")

#     # We look at the <strong> tag
#     strong_tag = page.locator("strong")

#     # We assert that it has the text ":)"
#     expect(strong_tag).to_have_text(":)")

# === End Example Code ===
    
def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_store.sql')
    page.goto(f"http://{test_web_address}/albums")
    div_tags = page.locator('div')
    expect(div_tags).to_have_text([
        'Title: Janky Star\nReleased: 2022',
        'Title: Malibu\nReleased: 2016',
    ])

def test_get_single_albums(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_store.sql')
    page.goto(f"http://{test_web_address}/albums/1")
    p_tags = page.locator('p')
    expect(p_tags).to_have_text([
        'Released: 2022'
    ])

def test_page_links_to_albums(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_store.sql')
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Janky Star released in 2022'")
    h1 = page.locator('h1')
    expect(h1).to_have_text(["Title: Janky Star"])