from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from services.database import add_tracked_artist, save_release
from services.discogs_service import get_releases

router = Router()


@router.message(Command("addartist"))
async def add_artist(message: Message):

    artist = (
        message.text
        .replace("/addartist", "")
        .strip()
    )

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

    releases = get_releases(artist)

    count = 0

    for release in releases:
        save_release(
            artist,
            release["id"]
        )
        count += 1

    await message.answer(
        f"✅ {artist} aggiunto.\n"
        f"{count} release salvate."
    )