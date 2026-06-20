from aiogram import Bot
from config import BOT_TOKEN

bot = Bot(BOT_TOKEN)


async def notify_users(
    user_ids,
    artist,
    title,
    link,
    cover=None
):

    if not user_ids:
        return

    message = (
        "🎵 Nuovo vinile trovato!\n\n"
        f"🎤 Artista: {artist}\n"
        f"💿 Titolo: {title}\n\n"
        f"🔗 {link}"
    )

    for user_id in user_ids:

        try:

            if cover:

                await bot.send_photo(
                    chat_id=user_id,
                    photo=cover,
                    caption=message
                )

            else:

                await bot.send_message(
                    chat_id=user_id,
                    text=message
                )

        except Exception as e:

            print(
                f"Errore con {user_id}: {e}"
            )