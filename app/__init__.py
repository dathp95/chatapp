from dataclasses import dataclass
from email import message
from .config import GOOGLE_CLOUD_API
from .chatbot import Skype
from flask import Flask, request
import gspread


'''
	BOT AZURE: create bot /newbot
	- App registrations -> new registration
	- Client credentials -> Lấy value 

'''
APP_ID = "6399b9dc-d267-4646-9adc-c5784e1c667b"
VALUE_ID ="5447Q~Q2fX1EfrG0MF9OGuNVM1-HltSw3rlGq"
skypeBot = Skype(client_id =APP_ID , client_secret = VALUE_ID)
# bot_id, bot_name, recipient, service, sender, text

'''
	GOOGLE SHEET: Connect google sheet
		- Bước 1: Create account Google console
		- Bước 2: Tạo API and Services, API và Enable Drive + Google sheet
		- Bước 3: Credentials -> Tạo API key + Services account-> Export JSON 

'''
KEYSHEET = "1Jiv9sJn0XWAae-3HKu4VjkKzIPIRiK_nU5UzAUJec5I"
gg_sheet = gspread.service_account_from_dict(GOOGLE_CLOUD_API)
spread_sheet = gg_sheet.open_by_key(KEYSHEET)
work_sheet = spread_sheet.worksheet("200VIA")
value_sheet = work_sheet.get_all_values()


def sending_user(user_id,username,value):
	data_row = value.split('|')
	via_id = data_row[0]
	via_pass = data_row[1]
	via_2fa = data_row[2]
	via_date_of_birth = data_row[3]
	via_mail = data_row[4]
	via_pass_mail = data_row[5]
	message = f'<at id=\"{user_id}\">{username}</at>\nVIA-ID: {via_id}\nVIA-PASS: {via_pass}\nMÃ 2FA: {via_2fa}\nNGÀY SINH:{via_date_of_birth} \nEMAIL: {via_mail}\nPASS_MAIL: {via_pass_mail}'
	return message

def handling_sending(
								user_id,
								username,
								value,
								bot_id,
								bot_name,
								recipient,
								service,
								sender):
	
	message = sending_user(user_id,username,value)
	skypeBot.send_message(bot_id,bot_name,recipient,service,sender,message)
	

def create_app():
	app = Flask(__name__)
	@app.route("/endpoint/",methods=["GET","POST"])  
	def apiMessages():
		if request.method =="POST":
			data = request.get_json()    
			try: 
				print("Dữ liệu trả về-----",data)

				#  Thông số cần thiết cho bot
				bot_id = data["recipient"]["id"]
				bot_name = data["recipient"]["name"]
				recipient = data["from"]
				service = data["serviceUrl"]
				sender = data["conversation"]["id"]
				# Thông số cho người nhận 
				user_id = recipient["id"]
				username = recipient["name"]
				user_text = data["text"]
				if user_text.startswith('Ping id'):
					user_text = user_text.replace('Ping id','').strip()
				
				'''
					list_data là 1 mảng chứa nhiều object
					1 object: "id":[dữ liệu]
				'''
				list_data = []
				for data in value_sheet:
					dict_data = {}
					dict_data[data[1]]= data[0]
					list_data.append(dict_data)
				for data in list_data:
					for key, value in data.items():
						if user_text == key:
							message = sending_user(user_id,username,value)							
							print(message)
							# bot_id,bot_name,recipient,service,sender,message
							skypeBot.send_message(bot_id = bot_id,
																		bot_name =bot_name,
																		recipient=recipient,
																		service= service,
																		sender=sender,
																		message=message)
						
			except:
				return "NG"
			
		return "OK REDU"

	return app
