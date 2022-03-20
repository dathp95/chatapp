from app.chatbot.model_bot import send_message
from .config import GOOGLE_CLOUD_API
from . import chatbot




'''
  BOT AZURE: create bot /newbot

'''
APP_ID = "6399b9dc-d267-4646-9adc-c5784e1c667b"
VALUE_ID ="5447Q~Q2fX1EfrG0MF9OGuNVM1-HltSw3rlGq"


skypeBot = chatbot.Skype(client_id =APP_ID , client_secret = VALUE_ID)
key_sheet = GOOGLE_CLOUD_API
