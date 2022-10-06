from os import environ

class config(object):
   THUMBNAIL = None
   API_ID = int(environ.get("API_ID", ""))
   API_HASH = environ.get("API_HASH", "")
   BOT_TOKEN = environ.get("BOT_TOKEN", "")
   ADMIN = int(environ.get("ADMIN", ""))
   CAPTION = environ.get("CAPTION", "")














