from aiogram import Bot, Dispatcher
from config import BOT_TOKEN

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

if __name__ == "__main__":
    dp.run_polling(bot)
