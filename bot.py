from aiogram import Bot, Dispatcher
from config import BOT_TOKEN

from handlers.start import router as start_router
from handlers.subscription import router as sub_router
from handlers.list_commands import router as list_router
from handlers.help import router as help_router
from handlers.artists import router as artists_router

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

dp.include_router(start_router)
dp.include_router(sub_router)
dp.include_router(list_router)
dp.include_router(help_router)
dp.include_router(artists_router)

if __name__ == "__main__":
    dp.run_polling(bot)