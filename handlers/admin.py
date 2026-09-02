from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from services.database import add_tracked_artist, save_release
from services.discogs_service import get_releases

router = Router()


@router.message(Command("addartist"))
async def add_artist(message: Message):
    artist = (
        message.text or ""
    ).replace("/addartist", "", 1).strip()

    if not artist:
        await message.answer(
            "Usa: /addartist Nome Artista"
        )
        return

    if not add_tracked_artist(artist):
        await message.answer(
            "Questo artista è già monitorato."
        )
        return

    await message.answer(
        f"Sto inizializzando {artist}..."
    )

    try:
        releases = get_releases(artist)

        count = 0
        for release in releases:
            release_id = release.get("id")
            if release_id is None:
                continue

            save_release(artist, release_id)
            count += 1

        await message.answer(
            f"✅ {artist} aggiunto.\n"
            f"{count} release iniziali salvate.\n\n"
            f"Da ora verrà incluso nei controlli automatici.\n"
            f"Per ricevere le notifiche usa: /sub {artist}"
        )

    except Exception as e:
        # L'artista resta nel database: al prossimo controllo
        # automatico il checker proverà nuovamente a interrogarlo.
        await message.answer(
            f"⚠️ {artist} è stato aggiunto, ma non sono riuscito "
            "a inizializzare le release in questo momento.\n"
            "Riproverò nei controlli automatici."
        )
        print(f"Errore inizializzazione {artist}: {e}")
