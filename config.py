import os



class Config(object):
      BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7295637877:AAGgcbpmQ03Q22LuLKlWl5EEG_BaUrU8XSU")
      API_ID = int(os.environ.get("APP_ID", "23790461"))
      API_HASH = os.environ.get("API_HASH", "2d0a7fb85f06246e93948bf7afc05fb3")
      CAPTION_TEXT = os.environ.get("CAPTION_TEXT", "")
      CAPTION_POSITION = os.environ.get("CAPTION_POSITION", "nil")
      ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "Amit_Shadow")
