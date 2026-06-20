from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()


@router.message(Command("help"))
async def help_command(message: Message):
    await message.answer(
        "🎵 Vinyl Alert Bot\n\n"
        "Comandi disponibili:\n\n"
        "/sub <artista>\n"
        "/unsub <artista>\n"
        "/list\n"
        "/artists\n"
        "/help"
    )