from config import Config
from database.access_db import db


async def AddUserToDatabase(bot, update):
    if not await db.is_user_exist(update.from_user.id):
        await db.add_user(update.from_user.id)
        details = await bot.get_users(user_ids=update.from_user.id)
        text = f"**ID:** {details.id}\n**USERNAME:** @{details.username}\n**FIRST NAME:** {details.first_name}\n**LAST NAME:** {details.last_name}\n**DC ID:** {details.dc_id}\n**IS FAKE:** {details.is_fake}\n**IS SCAM:** {details.is_scam}\n**IS SUPPORT:** {details.is_support}"
        await bot.send_message(chat_id=Config.ADMIN,
                                text=f"`BOT Started By:`\n\n{text}")

