from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from services.database import (
    add_subscription,
    remove_subscription,
    get_subscriptions,
    get_tracked_artist,
)

router = Router()

# Alias comodi per gli artisti principali.
# Gli artisti aggiunti con /addartist vengono invece risolti
# direttamente dalla tabella tracked_artists di Supabase.
ARTIST_ALIASES = {
    "ariana grande": "Ariana Grande",
    "ariana": "Ariana Grande",
    "ari": "Ariana Grande",
    "sabrina carpenter": "Sabrina Carpenter",
    "sabrina": "Sabrina Carpenter",
    "sab": "Sabrina Carpenter",
    "taylor swift": "Taylor Swift",
    "taylor": "Taylor Swift",
    "tay": "Taylor Swift",
}


def resolve_artist(artist_input: str):
    normalized = artist_input.strip().casefold()

    alias = ARTIST_ALIASES.get(normalized)
    if alias:
        return alias

    return get_tracked_artist(artist_input.strip())


@router.message(Command("sub"))
async def subscribe(message: Message):
    user_id = message.from_user.id

    artist_input = (
        message.text or ""
    ).replace("/sub", "", 1).strip()

    if not artist_input:
        await message.answer(
            "Usa: /sub Nome Artista"
        )
        return

    artist = resolve_artist(artist_input)

    if artist is None:
        await message.answer(
            "Artista non supportato.\n"
            "Puoi seguire solo artisti presenti tra quelli monitorati."
        )
        return

    if not add_subscription(user_id, artist):
        await message.answer(
            f"Sei già iscritto a {artist}."
        )
        return

    await message.answer(
        f"✅ Ti sei iscritto a {artist}."
    )


@router.message(Command("unsub"))
async def unsubscribe(message: Message):
    user_id = message.from_user.id

    artist_input = (
        message.text or ""
    ).replace("/unsub", "", 1).strip()

    if not artist_input:
        await message.answer(
            "Usa: /unsub Nome Artista"
        )
        return

    artist = resolve_artist(artist_input)

    if artist is None:
        await message.answer(
            "Artista non supportato.\n"
            "Puoi gestire solo artisti presenti tra quelli monitorati."
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
        f"❌ Hai smesso di seguire {artist}."
    )
