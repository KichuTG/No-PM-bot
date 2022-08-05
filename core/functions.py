import enum
import imp
import shutil
import psutil

from pyrogram import enums

from database.access_db import db


async def status(bot, message):
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    total_users = await db.total_users_count()
    await message.reply_text(
        text=f"**Total Disk Space:** {total} \n**Used Space:** {used}({disk_usage}%) \n**Free Space:** {free} \n**CPU Usage:** {cpu_usage}% \n**RAM Usage:** {ram_usage}%\n\n**Total Users in DB:** `{total_users}`",
        parse_mode=enums.ParseMode.MARKDOWN,
        quote=True
    )



#-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*
def humanbytes(n):
    if not n:
        return(None)

    pow = 2**10
    p = 0
    unit = {0: " ", 1 : "KB", 2 : "MB", 3: "GB"}
    while n > pow:
        n /= pow
        p += 1
    final = str(round(n, 2)) + " " + unit[p]
    return(final)
#-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*