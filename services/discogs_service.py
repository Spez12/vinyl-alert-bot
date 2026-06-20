import requests
from config import DISCOGS_TOKEN

HEADERS = {
    "Authorization": f"Discogs token={DISCOGS_TOKEN}"
}


def get_releases(artist):
    url = (
        "https://api.discogs.com/database/search"
        f"?artist={artist}"
        "&format=Vinyl"
        "&sort=year"
        "&sort_order=desc"
        "&per_page=20"
    )

    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        return []

    data = response.json()

    return data.get("results", [])