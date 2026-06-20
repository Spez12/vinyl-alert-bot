from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from services.database import remove_tracked_artist

router = Router()


@router.message(Command("removeartist"))
async def remove_artist(message: Message):

    artist = (
        message.text
        .replace("/removeartist", "")
        .strip()
    )

    if not artist:
        await message.answer(
            "Usa: /removeartist Nome Artista"
        )
        return

    remove_tracked_artist(artist)

    await message.answer(
        f"{artist} rimosso."
    )