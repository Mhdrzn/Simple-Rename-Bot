from os import environ

API_ID = int(environ.get("API_ID", ""))
API_HASH = environ.get("API_HASH", "")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
ADMIN = int(environ.get("ADMIN", ""))
THUMBNAIL = [set(x) for x in environ.get("THUMBNAIL", "")]                       
CAPTION = environ.get("CAPTION", "")
















