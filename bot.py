from pyrogram import Client
from config import config
from pyromod import listen

class App(Client):
    def __init__(self):
        super().__init__(
            name="renamer",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            workers=50,
            plugins={"root": "main"},
            sleep_threshold=5,
        )

bot = App()
bot.run()
