# © Cyril C Thomas
# https://t.me/cyril_c_10

import os

class Config(object):
    API_ID = int(os.getenv("API_ID", )) #Telegram API ID
    API_HASH = os.getenv("API_HASH", "") #Telegram API HASH
    BOT_TOKEN = os.getenv("BOT_TOKEN", "") #Telegram BOT TOKEN
  
    BOT_OWNER = os.environ.get("BOT_OWNER", 668069993) #User ID of Owner
    MONGODB_URI = os.environ.get("MONGODB_URI", "") #MongoDB URI
    SESSION_NAME = os.environ.get("SESSION_NAME", "") #Session Name for Batabase
  
  
    CHANNEL = os.environ.get("CHANNEL", "") #BOT Support Channel

    BANNED_USERS = os.environ.get("BANNED_USERS", []) #Banned Users
    ADMIN = int(os.environ.get("ADMINS", )) #BOT ADMIN
