from pyrogram import Client, filters 
from config import THUMBNAIL, ADMIN

@Client.on_message(filters.private & filters.command("set") & filters.user(ADMIN))                            
async def (bot, msg):
    print("soon..")









