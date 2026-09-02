import requests
from config import DISCOGS_TOKEN

BASE_URL = "https://api.discogs.com/database/search"

HEADERS = {
    "Authorization": f"Discogs token={DISCOGS_TOKEN}",
    "User-Agent": "VinylAlertBot/1.0",
}


def get_releases(artist):
    params = {
        "artist": artist,
        "format": "Vinyl",
        "sort": "year",
        "sort_order": "desc",
        "per_page": 20,
    }

    response = requests.get(
        BASE_URL,
        headers=HEADERS,
        params=params,
        timeout=30,
    )

    if response.status_code != 200:
        print(
            f"Discogs error {response.status_code} "
            f"per {artist}: {response.text[:200]}"
        )
        return []

    data = response.json()
    return data.get("results", [])
