from .config import GOOGLE_CLOUD_API
from .chatbot import Skype
from flask import Flask, request



'''
  BOT AZURE: create bot /newbot

'''
APP_ID = "6399b9dc-d267-4646-9adc-c5784e1c667b"
VALUE_ID ="5447Q~Q2fX1EfrG0MF9OGuNVM1-HltSw3rlGq"
skypeBot = Skype(client_id =APP_ID , client_secret = VALUE_ID)
# bot_id, bot_name, recipient, service, sender, text
#THÔNG SỐ ĐỂ GỬI TIN NHẮN VÀO NHÓM
recipient = {
		"id": "28:6399b9dc-d267-4646-9adc-c5784e1c667b",
		"name": "Ping id"
	}

bot_id = "19:a8ac39be95ad4d19996e13b7391db93d@thread.skype"

bot_name = "Ping id"

service = "https://smba.trafficmanager.net/apis/"

sender = "19:a8ac39be95ad4d19996e13b7391db93d@thread.skype"





def create_app():
  app = Flask(__name__)
  @app.route("/endpoint/",methods=["GET","POST"])  
  def apiMessages():
    if request.method =="POST":
      data = request.get_json()
      print('ok2')
      print(data)
      # try: 
      #   recipient = data['recipient']
      #   bot_id = recipient['id']
      #   bot_name = recipient['name']
      #   service = data['serviceUrl']
      #   sender = data['conversation']['id']
      #   message = data.get("text","12345")
      #   skypeBot.send_message(bot_id,bot_name,recipient,service,sender,message)
      # except:
      #   return "NG"
      
    return "OK REDU"

  return app
