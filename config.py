# © Cyril C Thomas
# https://t.me/cyril_c_10

import os

class Config(object):
    API_ID = int(os.getenv("API_ID", "28714959")) #Telegram API ID
    API_HASH = os.getenv("API_HASH", "c0b9797634090ee3f4c1c56db6c051a7") #Telegram API HASH
    BOT_TOKEN = os.getenv("BOT_TOKEN", "7130118875:AAFiAqDKqApt3ahGHnv7qhcaxaE18M75vik") #Telegram BOT TOKEN
  
    BOT_OWNER = os.environ.get("BOT_OWNER", "5398056049") #User ID of Owner
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://jiosaavn:jiosaavn@cluster0.ouhhe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") #MongoDB URI
    SESSION_NAME = os.environ.get("SESSION_NAME", "nopmbot") #Session Name for Batabase
  
  
    CHANNEL = os.environ.get("CHANNEL", "-1001678094109") #BOT Support Channel

    BANNED_USERS = os.environ.get("BANNED_USERS", []) #Banned Users
    ADMIN = int(os.environ.get("ADMINS", "5398056049 1905251964")) #BOT ADMIN
