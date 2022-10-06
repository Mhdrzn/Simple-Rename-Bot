from pyrogram import Client, filters 
from config import config
import os

@Client.on_message(filters.private & filters.command("set") & filters.user(ADMIN))                            
async def set_tumb(bot, msg):
    replied = msg.reply_to_message
    if not replied:
        await msg.reply("use this command with Reply to a photo")
        return
    if not msg.reply_to_message.photo:
       await msg.reply("Oops !! this is Not a photo")
       return
    config.THUMBNAIL = msg.reply_to_message.photo.file_id
    return await msg.reply("done ✅️")


@Client.on_message(filters.private & filters.command("view") & filters.user(ADMIN))                            
async def del_tumb(bot, msg):
    if config.THUMBNAIL is not None:
        await msg.reply_photo(photo=config.THUMBNAIL, text="this is your current thumbnail")
    else:
        await msg.reply_text(text="you don't have any thumbnail")
   




