from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

router = Router()


@router.message(CommandStart())
async def start(message: Message):

    text = (
        "🎵 Benvenuto su Vinyl Alert Bot!\n\n"
        "Ricevi notifiche quando escono nuovi vinili "
        "dei tuoi artisti preferiti.\n\n"
        "Comandi utili:\n"
        "• /artists\n"
        "• /sub artista\n"
        "• /list\n"
        "• /help"
    )

    await message.answer(text)