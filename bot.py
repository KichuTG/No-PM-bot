#Cyril C Thomas
#https://t.me/cyril_c_10

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

from pyrogram import Client, filters
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from config import Config
from core.handler import start, help, text_for, reply_text, media_for, reply_media
from database.access_db import db
from database.add_user import AddUserToDatabase
# from helpers.broadcast import broadcast_handler


cbot = Client(
        "Messenger", 
        bot_token=Config.BOT_TOKEN, 
        api_hash=Config.API_HASH,
        api_id=Config.API_ID
)


@cbot.on_message(filters.private & filters.command('start'))
async def sender(bot, update):
        await AddUserToDatabase(bot, update)
        await start(bot, update)

@cbot.on_message(filters.private & filters.command('help'))
async def sender(bot, update):
        await AddUserToDatabase(bot, update)
        await help(bot, update)

@cbot.on_message(filters.private & filters.text)
async def texter(bot, update):
        await AddUserToDatabase(bot, update)
        await text_for(bot, update)


@cbot.on_message(filters.private & filters.media)
async def media_msg(bot, update):
        await AddUserToDatabase(bot, update)
        await media_for(bot, update)

@cbot.on_message(filters.user(Config.ADMIN) & filters.text)
async def admin_msg(bot, update):
        print("\n\nText\n\n")
        await reply_text(bot, update)

@cbot.on_message(filters.user(Config.ADMIN) & filters.media)
async def admin_media(bot, update):
        print("\n\nMedia\n\n")
        await reply_media(bot, update)

cbot.run()