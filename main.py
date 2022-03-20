import gspread

from app import key_sheet, bot


#THÔNG SỐ ĐỂ GỬI TIN NHẮN VÀO NHÓM
# ID_GROUP_SKYPE = "19:e42b5520e7254ab7b5acf610b515b607@thread.skype"
# TEST_ID = "19:df47e0c9f7f841a582ff7d697296ed00@thread.skype"

# bot_id, bot_name, recipient, service, sender, text
#THÔNG SỐ ĐỂ GỬI TIN NHẮN VÀO NHÓM
recipient = {
		"id": "29:1ASr6sEwlbQFyaRc7Hsh5JpbgWIpdN-ehjA94xZ2rU28",
		"name": "Mundo-QC"
	}

bot_id = "19:e42b5520e7254ab7b5acf610b515b607@thread.skype"

bot_name = "Giao khách tiết kiệm"

service = "https://smba.trafficmanager.net/apis/"

sender = "19:e42b5520e7254ab7b5acf610b515b607@thread.skype"

text = 'ok redu'

bot.send_message(bot_id,bot_name,recipient,service,sender,text)
#########################################
'''
  Google sheet: Khóa KEY - Trang tính
  credentials: API and Services
'''
KEY_SHEET = "1Jiv9sJn0XWAae-3HKu4VjkKzIPIRiK_nU5UzAUJec5I"
gc = gspread.service_account_from_dict(key_sheet)
sh = gc.open_by_key(KEY_SHEET)
worksheet = sh.worksheet('200VIA')
list_of_lists  = worksheet.get_all_values()
test_id = "100045714163517"
for data in list_of_lists:
  if(test_id in data):
    print('\n'.join(data))
    


  # for string_data in data:
  #   print(string_data)
    # print("-".join(string_data))
