from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from services.database import (
    add_subscription,
    remove_subscription,
    get_subscriptions
)

router = Router()

ARTISTS = {
    "ariana grande": "Ariana Grande",
    "ariana": "Ariana Grande",
    "ari": "Ariana Grande",

    "sabrina carpenter": "Sabrina Carpenter",
    "sabrina": "Sabrina Carpenter",
    "sab": "Sabrina Carpenter",

    "taylor swift": "Taylor Swift",
    "taylor": "Taylor Swift",
    "tay": "Taylor Swift"
}


@router.message(Command("sub"))
async def subscribe(message: Message):
    user_id = message.from_user.id

    artist_input = (
        message.text
        .replace("/sub", "")
        .strip()
        .lower()
    )

    artist = ARTISTS.get(artist_input)

    if artist is None:
        await message.answer(
            "Artista non supportato."
        )
        return

    if not add_subscription(user_id, artist):
        await message.answer(
            f"Sei già iscritto a {artist}."
        )
        return

    await message.answer(
        f"Ti sei iscritto a {artist}."
    )


@router.message(Command("unsub"))
async def unsubscribe(message: Message):
    user_id = message.from_user.id

    artist_input = (
        message.text
        .replace("/unsub", "")
        .strip()
        .lower()
    )

    artist = ARTISTS.get(artist_input)

    if artist is None:
        await message.answer(
            "Artista non supportato."
        )
        return

    subscriptions = get_subscriptions(user_id)

    if artist not in subscriptions:
        await message.answer(
            f"Non segui {artist}."
        )
        return

    remove_subscription(user_id, artist)

    await message.answer(
        f"Hai smesso di seguire {artist}."
    )