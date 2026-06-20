import requests
from config import DISCOGS_TOKEN

HEADERS = {
    "Authorization": f"Discogs token={DISCOGS_TOKEN}"
}

def search_artist(artist):
    url = (
        "https://api.discogs.com/database/search"
        f"?artist={artist}&format=Vinyl"
    )

    response = requests.get(url, headers=HEADERS)
    return response.json()
