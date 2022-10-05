from pyrogram import Client
from config import *

class App(Client):
    def __init__(self):
        super().__init__(
            name="renamer",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=50,
            plugins={"root": "main"},
            sleep_threshold=5,
        )

bot = App()
bot.run()
