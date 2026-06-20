from aiogram import Bot, Dispatcher
from config import BOT_TOKEN

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from checker import check_releases

from handlers.start import router as start_router
from handlers.subscription import router as sub_router
from handlers.list_commands import router as list_router
from handlers.help import router as help_router
from handlers.artists import router as artists_router
from handlers.admin import router as admin_router

import asyncio

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

dp.include_router(start_router)
dp.include_router(sub_router)
dp.include_router(list_router)
dp.include_router(help_router)
dp.include_router(artists_router)
dp.include_router(admin_router)


async def main():

    scheduler = AsyncIOScheduler()

    scheduler.add_job(
        check_releases,
        "interval",
        hours=6
    )

    scheduler.start()

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())