from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from services.database import get_tracked_artists

router = Router()


@router.message(Command("artists"))
async def artists(message: Message):

    artists = get_tracked_artists()

    if not artists:
        await message.answer(
            "Nessun artista monitorato."
        )
        return

    text = "🎵 Artisti monitorati:\n\n"

    for artist in artists:
        text += f"• {artist}\n"

    await message.answer(text)