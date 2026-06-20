from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()


@router.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "🎵 Benvenuto nel Vinyl Alert Bot!\n\n"
        "Ricevi notifiche quando escono nuovi vinili dei tuoi artisti preferiti.\n\n"
        "Comandi principali:\n"
        "/sub artista\n"
        "/list\n"
        "/artists\n"
        "/help"
    )