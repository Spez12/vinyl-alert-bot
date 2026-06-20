from services.discogs_service import get_releases
from services.database import save_release

ARTISTS = [
    "Taylor Swift",
    "Ariana Grande",
    "Sabrina Carpenter"
]

for artist in ARTISTS:
    print(f"Controllo {artist}...")

    releases = get_releases(artist)

    for release in releases:
        save_release(
            artist,
            release["id"]
        )

print("Database inizializzato.")