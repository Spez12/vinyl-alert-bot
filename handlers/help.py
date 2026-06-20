from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()


@router.message(Command("help"))
async def help_command(message: Message):

    text = (
        "🎵 Vinyl Alert Bot\n\n"
        "Comandi disponibili:\n\n"
        "/artists - Artisti monitorati\n"
        "/sub artista - Segui un artista\n"
        "/unsub artista - Smetti di seguire un artista\n"
        "/list - I tuoi artisti\n"
        "/addartist artista - Aggiungi un artista\n"
        "/help - Mostra questo messaggio"
    )

    await message.answer(text)