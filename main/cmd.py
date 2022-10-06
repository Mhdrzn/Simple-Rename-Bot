from pyrogram import Client, filters
from pyrogram.types import * 


@Client.on_message(filters.command("start") & filters.private)                             
async def start_cmd(bot, msg):
    await help_cb(bot, msg, cb=False)


@Client.on_callback_query(filters.regex("start"))
async def start(bot, msg, cb=True):
    txt=f"hai {msg.from_user.mention} i am simple rename bot"
    button= [[
        InlineKeyboardButton("ℹ️ ʜᴇʟᴩ", callback_data="help"),
        Inlinekeyboardbutton("📡 ᴀʙᴏᴜᴛ", callback_data="about") 
    ]]  
    if cb:
        await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button))
    else:
        await msg.reply_text(text=txt, reply_markup=InlineKeyboardMarkup(button))


Client.on_callback_query(filters.regex("help"))
async def help(bot, msg):
    await msg.message.edit(text="soon")


Client.on_callback_query(filters.regex("about"))
async def about(bot, msg, cb=True):
    await msg.message.edit(text="soon")


Client.on_callback_query(filters.regex("del"))
async def del(bot, msg, cb=True):
    try:
        await update.message.delete()
    except:
        return     





                   
