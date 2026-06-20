from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from services.database import get_subscriptions

router = Router()


@router.message(Command("list"))
async def list_subscriptions(message: Message):
    user_id = message.from_user.id

    artists = get_subscriptions(user_id)

    if not artists:
        await message.answer(
            "Non stai seguendo nessun artista."
        )
        return

    text = "🎧 Artisti seguiti:\n\n"

    for artist in artists:
        text += f"• {artist}\n"

    await message.answer(text)