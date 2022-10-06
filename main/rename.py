import time 
from pyrogram import Client, filters, enums
from config import temp, CAPTION
from main.utils import progress_message

@Client.on_message(filters.command("rename"))             
async def rename_file(bot, msg):
    reply = msg.reply_to_message
    file_name = msg.text.split(" ", 1)[1]
    new_name = f"./DOWNLOADS/{file_name}"
    sts = await msg.reply_text("Trying to Downloading.....")
    c_time = time.time()
    downloaded = await reply.download(
        file_name=new_name,
        progress=progress_message,
        progress_args=("Download Started.....", sts, c_time)                    
    )
    if CAPTION:
        cap = CAPTION.format(file_name=new_name)
    else:
        cap = f"{new_name}"
    raw_thumbnail = temp.THUMBNAIL 
    if raw_thumbnail:
       og_thumbnail = await bot.download_media(raw_thumbnail)
    await sts.edit("Trying to Uploading")
    c_time = time.time()
    await bot.send_document(
            msg.message.chat.id,
            document=downloaded,
            thumb=og_thumbnail, 
            caption=cap, 
            progress=progress_message,
            progress_args=("Uploade Started.....", sts, c_time)
    )      




   
