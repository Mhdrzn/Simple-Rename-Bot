from os import environ

API_ID = int(environ.get("API_ID", ""))
API_HASH = environ.get("API_HASH", "")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
ADMIN = int(environ.get("ADMIN", ""))
CAPTION = environ.get("CAPTION", "")

Current_Thumb = environ.get("THUMBNAIL", "")
THUMBNAIL = [set(x) for x in (Current_Thumb).split()]                 













