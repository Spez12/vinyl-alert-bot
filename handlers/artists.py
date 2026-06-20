from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()


@router.message(Command("artists"))
async def artists(message: Message):
    await message.answer(
        "🎵 Artisti disponibili:\n\n"
        "• Ariana Grande\n"
        "• Sabrina Carpenter\n"
        "• Taylor Swift\n"
    )