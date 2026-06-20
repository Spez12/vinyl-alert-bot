from aiogram import Bot
from config import BOT_TOKEN

bot = Bot(BOT_TOKEN)

async def send_alert(user_id, text):
    await bot.send_message(user_id, text)
