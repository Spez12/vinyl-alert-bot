from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

router = Router()


@router.message(CommandStart())
async def start(message: Message):

    text = (
        "🎵 Benvenuto su Vinyl Alert Bot!\n\n"
        "Questo bot controlla automaticamente Discogs "
        "e ti avvisa quando esce un nuovo vinile "
        "degli artisti che segui.\n\n"
        "Comandi:\n"
        "• /artists → artisti disponibili\n"
        "• /sub artista → segui un artista\n"
        "• /unsub artista → smetti di seguirlo\n"
        "• /list → i tuoi artisti\n"
        "• /addartist artista → aggiungi un artista\n"
        "• /help → aiuto\n\n"
        "Inizia con /artists e scegli chi seguire 🎶"
    )

    await message.answer(text)