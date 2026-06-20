from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from handlers.subscription import subscriptions

router = Router()


@router.message(Command("list"))
async def list_subscriptions(message: Message):
    user_id = message.from_user.id

    if (
        user_id not in subscriptions
        or len(subscriptions[user_id]) == 0
    ):
        await message.answer(
            "Non stai seguendo nessun artista."
        )
        return

    text = "Artisti seguiti:\n\n"

    for artist in subscriptions[user_id]:
        text += f"• {artist}\n"

    await message.answer(text)