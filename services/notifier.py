from aiogram import Bot
from config import BOT_TOKEN

bot = Bot(BOT_TOKEN)


async def notify_users(user_ids, artist, title):

    if not user_ids:
        return

    message = (
        "🎵 Nuova release trovata!\n\n"
        f"Artista: {artist}\n"
        f"Titolo: {title}"
    )

    for user_id in user_ids:
        try:
            await bot.send_message(
                user_id,
                message
            )
        except Exception as e:
            print(
                f"Errore con {user_id}: {e}"
            )