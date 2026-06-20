from services.discogs_service import get_releases
from services.database import (
    get_tracked_artists,
    release_exists,
    save_release,
    get_subscribers
)
from services.notifier import notify_users

import asyncio

async def check_releases():

    print("Avvio controllo release...")

    artists = get_tracked_artists()

    for artist in artists:

        try:
            print(f"Controllo {artist}...")

            releases = get_releases(artist)

            for release in releases[:10]:

                release_id = release.get("id")

                if release_id is None:
                    continue

                if release_exists(release_id):
                    continue

                title = release.get(
                    "title",
                    "Titolo sconosciuto"
                )

                link = f"https://www.discogs.com/release/{release_id}"
                cover = release.get("cover_image")

                save_release(
                    artist,
                    release_id
                )

                users = get_subscribers(artist)

                await notify_users(
                    users,
                    artist,
                    title,
                    link,
                    cover
                )

                print(
                    f"Nuova release trovata: {title}"
                )

        except Exception as e:

            print(
                f"Errore durante il controllo di "
                f"{artist}: {e}"
            )

    print("Controllo completato.")

    import asyncio

if __name__ == "__main__":
    asyncio.run(check_releases())
