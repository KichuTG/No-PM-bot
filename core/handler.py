from email import message
from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserIsBlocked, PeerIdInvalid, InputUserDeactivated
from pyrogram import filters


from config import Config
from core.functions import status

# START COMMAND

async def start(bot, update):
    if ((update.from_user.id == Config.ADMIN) or (update.from_user.id == Config.CHECK)):
        await status(bot, update)
    else:
        reply=f"Hi there {update.from_user.first_name},\n\nHow Can I help you Today????\n\n`Send your Questions here and I will get back to you soon........`"
        try:
            await update.reply_text(text=reply)
        except UserIsBlocked:
            await bot.send_message(chat_id=Config.ADMIN,
                                    text=f"User Blocked: {update.from_user.id}")
        except PeerIdInvalid:
            await bot.send_message(chat_id=Config.ADMIN,
                                    text=f"User ID Invalid: {update.from_user.id}")                                    
        except InputUserDeactivated:
            await bot.send_message(chat_id=Config.ADMIN,
                                    text=f"User Deactivated: {update.from_user.id}")


# HELP COMMAND

async def help(bot, update):
    if ((update.from_user.id == Config.ADMIN) | (update.from_user.id == Config.CHECK)):
        await status(bot, update)
    else:
        reply=f"Hi there {update.from_user.first_name},\n\nThis BOT can Be USed To Contact the Admin of @{Config.CHANNEL}\n\nThe Admin Will Get Back to you as Soon as Possible\n\nPlease be patient......."
        await update.reply_text(text=reply)


# TEXT MESSAGE

async def text_for(bot, update):
    if ((update.from_user.id == Config.ADMIN) | (update.from_user.id == Config.CHECK)):
        await reply_text(bot, update)
    else:
        tex = update.text
        text = f"**Private Message from,**\nID: {update.from_user.id}\n\n{tex}"
        await bot.send_message(chat_id=Config.ADMIN,
                    text=text)


# MEDIA MESSAGE

async def media_for(bot, update):
    if ((update.from_user.id == Config.ADMIN) | (update.from_user.id == Config.CHECK)):
        await reply_media(bot, update)
    else:
        tex = update.caption
        if tex is None:
            tex = ""
        cap = f"**Private Message from,**\nID: {update.from_user.id}\n\n{tex}"
        await bot.copy_message(chat_id=Config.ADMIN,
                                from_chat_id=update.from_user.id,
                                message_id=update.id,
                                caption=cap)



# REPLY TEXT MESSAGE

async def reply_text(bot, update):
    if update.reply_to_message is not None:
        tex = update.reply_to_message
        try:
            id = tex.text.split()[4]

        except Exception:
            pass
        try:
            id = tex.caption.split()[4]
        except Exception:
            pass
        text_me = update.text
        await bot.send_message(chat_id=id,
                                    text=text_me)

# REPLY MEDIA MESSAGE

async def reply_media(bot, update):
    if update.reply_to_message is not None:
        tex = update.reply_to_message
        try:
            id = tex.text.split()[4]
        except Exception:
            pass
        try:
            id = tex.caption.split()[4]

        except Exception:
            pass
        await bot.copy_message(chat_id=id,
                                    from_chat_id=update.from_user.id,
                                    message_id=update.id)