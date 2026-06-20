import asyncio

from services.discogs_service import get_releases
from services.database import (
    get_tracked_artists,
    release_exists,
    save_release,
    get_subscribers
)
from services.notifier import notify_users


async def check_releases():

    artists = get_tracked_artists()

    for artist in artists:

        print(f"Controllo {artist}...")

        releases = get_releases(artist)

        for release in releases[:10]:

            release_id = release["id"]

            if release_exists(release_id):
                continue

            save_release(
                artist,
                release_id
            )

            users = get_subscribers(artist)

            await notify_users(
                users,
                artist,
                release["title"]
            )

            print(
                f"Nuova release trovata: "
                f"{release['title']}"
            )