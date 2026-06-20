from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

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

subscriptions = {}


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

    if user_id not in subscriptions:
        subscriptions[user_id] = []

    if artist in subscriptions[user_id]:
        await message.answer(
            f"Sei già iscritto a {artist}."
        )
        return

    subscriptions[user_id].append(artist)

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

    if (
        user_id not in subscriptions
        or artist not in subscriptions[user_id]
    ):
        await message.answer(
            f"Non segui {artist}."
        )
        return

    subscriptions[user_id].remove(artist)

    await message.answer(
        f"Hai smesso di seguire {artist}."
    )