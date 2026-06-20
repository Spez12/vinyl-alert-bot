from services.discogs_service import search_artist

artists = [
    "Ariana Grande",
    "Sabrina Carpenter",
    "Taylor Swift"
]

for artist in artists:
    releases = search_artist(artist)
    print(artist)
    print(releases)
