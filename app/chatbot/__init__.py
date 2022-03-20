### Vui lòng xem kĩ hơn hướng dẫn các hàm tại Readme.md
# |  Now you can use base methods:  |
# | ------------------------------- |
# | send_message                    |
# | send_media                      |
# | create_animation_card           |
# | create_card_attachment          |
# | create_card_image               |
# | create_button                   |
# | send_card                       |
# | create_card_adaptive            |
# | create_item_for_adaptive_card   |
# | create_action_for_adaptive_card |
# | create_html_card                |
#### list card  : Adaptive Card	
# Animation card	
# Audio card	
# Hero card	Receipt card	
# Sign-in card	
# Thumbnail card	
# Video card

import threading
import time
from .model_bot import *


class Skype:
    '''### Vui lòng xem kĩ hơn hướng dẫn các hàm tại Readme.md
    # |  Now you can use base methods:  |
    # | ------------------------------- |
    # | send_message                    |
    # | send_media                      |
    # | create_animation_card           |
    # | create_card_attachment          |
    # | create_card_image               |
    # | create_button                   |
    # | send_card                       |
    # | create_card_adaptive            |
    # | create_item_for_adaptive_card   |
    # | create_action_for_adaptive_card |
    # | create_html_card                |
    # *_________________________________*
    '''
    def __init__(self, client_id, client_secret):

        def get_token():
            global token

            payload = "grant_type=client_credentials&client_id=" + client_id + "&client_secret=" + client_secret + \
                      "&scope=https%3A%2F%2Fapi.botframework.com%2F.default"
            response = requests.post("https://login.microsoftonline.com/common/oauth2/v2.0/token?client_id=" +
                                     client_id + "&client_secret=" + client_secret + "&grant_type=client_credentials&"
                                     "scope=https%3A%2F%2Fgraph.microsoft.com%2F.default", data=payload,
                                     headers={"Host": "login.microsoftonline.com",
                                              "Content-Type": "application/x-www-form-urlencoded"})
            data = response.json()
            token = data["access_token"]

        def run_it():
            while True:
                get_token()
                time.sleep(3590)

        self.t = threading.Thread(target=run_it)
        self.t.daemon = True
        self.t.start()

    @staticmethod
    def send_message(bot_id, bot_name, recipient, service, sender, text, text_format='markdown'):
        """
        send_message(bot_id, bot_name, recipient, service, sender, text, text_format),
        bot_id - id bot skype, bạn có thể lấy nó theo yêu cầu data['recipient']['id'].,
        bot_name - tên bot skype, bạn có thể lấy nó theo yêu cầu data['recipient']['name'].,
        recipient - người dùng, người mà bạn đang gửi tin nhắn. Bạn có thể lấy nó từ yêu cầu data['from'].,
        service - url dịch vụ, bạn có thể lấy nó theo yêu cầu data['serviceUrl'].,
        sender  - id cuộc trò chuyện, bạn có thể lấy nó theo yêu cầu data['conversation']['id'].,
        text - nhắn tin những gì bạn muốn gửi cho người nhận. Phải là một string.,
        text_format - các giá trị được hỗ trợ: "trơn", "markdown" hoặc "xml" (mặc định: "markdown").,
        """

        return send_message(token, bot_id, bot_name, recipient, service, sender, text, text_format)

    @staticmethod
    def send_card(bot_id, bot_name, recipient, reply_to_id, service, sender, message_type, card_attachment, text=''):
        """
        bot_id - id bot skype, bạn có thể lấy nó theo yêu cầu data['recipient']['id'].
        bot_name - tên bot skype, bạn có thể lấy nó theo yêu cầu data['recipient']['name'].
        reply_to_id - id tin nhắn bạn đang trả lời, bạn có thể lấy nó theo yêu cầu data['id'].
        recipient - người dùng, người mà bạn đang gửi tin nhắn. Bạn có thể lấy nó từ yêu cầu data['from'].
        service - url dịch vụ, bạn có thể lấy nó theo yêu cầu data['serviceUrl'].
        sender  - id cuộc trò chuyện, bạn có thể lấy nó theo yêu cầu data['conversation']['id'].
        message_type - nếu bạn gửi nhiều thẻ, hãy chọn cách hiển thị ("carousel" hoặc "list").
        card_attachment - list các thẻ, trong tin nhắn (để tạo thẻ sử dụng phương pháp create_card_attachment). Phải là một list.
        text - nội dung tin nhắn của bạn.
        """
        return send_card(token, bot_id, bot_name, recipient, reply_to_id, service, sender, message_type,
                         card_attachment, text)

    @staticmethod
    def send_media(bot_id, bot_name, recipient, service, sender, message_type, url, attachment_name=None):
        '''
        _.Gửi tệp phương tiện:

        bot_id - id bot skype, bạn có thể lấy nó theo yêu cầu data['recipient']['id'].
        bot_name - tên bot skype, bạn có thể lấy nó theo yêu cầu data['recipient']['name'].
        recipient  - người dùng, người mà bạn đang gửi tin nhắn. Bạn có thể lấy nó từ yêu cầu data['from'].
        service - url dịch vụ, bạn có thể lấy nó theo yêu cầu data['serviceUrl'].
        sender - id cuộc trò chuyện, bạn có thể lấy nó theo yêu cầu data['conversation']['id'].
        message_type - loại tệp phương tiện của bạn, ví dụ: "hình ảnh / png".
        url - mở url cho tệp phương tiện của bạn.
        attachment_name - name, được hiển thị cho người nhận.
        '''

        return send_media(token, bot_id, bot_name, recipient, service, sender, message_type, url,
                          attachment_name)

    @staticmethod
    def create_card_image(url, alt=None):
        """
        url - mở url cho hình ảnh của bạn.
        alt - văn bản thay thế cho hình ảnh.
        """
        return create_card_image(url, alt)

    @staticmethod
    def create_card_adaptive(items=None, actions=None):
        return create_card_adaptive(items, actions)

    @staticmethod
    def create_button(button_type, title, value):
        """
        _.Tạo hình ảnh cho thẻ:
        button_type - loại nút của bạn (ví dụ: "openUrl", "postBack").
        title - tên của nút.
        value - giá trị của nút (ví dụ: if button_type = "openUrl", value = "example.com").

        *______________*_____________________________________________________________________________________*
        │Loại hành động |	Nội dung của tài sản giá trị                                                     |
        │_______________|____________________________________________________________________________________|
        │ openUrl	    | URL sẽ được mở trong trình duyệt cài sẵn.                                          |
        │---------------|------------------------------------------------------------------------------------|
        │ imBack	    | Nội dung tin nhắn để gửi đến bot (từ người dùng đã nhấp vào nút hoặc chạm vào thẻ).| 
        |               | Thông báo này (từ người dùng đến bot) sẽ hiển thị với tất cả những người tham gia  | 
        |               |cuộc trò chuyện thông qua ứng dụng khách đang lưu trữ cuộc trò chuyện.              |
        │---------------|------------------------------------------------------------------------------------|
        | postBack	    | Nội dung tin nhắn để gửi đến bot (từ người dùng đã nhấp vào nút hoặc chạm vào thẻ).| 
        |               | Một số ứng dụng khách có thể hiển thị văn bản này trong nguồn cấp tin nhắn,        |
        |               | nơi nó sẽ hiển thị cho tất cả những người tham gia cuộc trò chuyện.                |
        │---------------|------------------------------------------------------------------------------------|
        | call          | Đích đến cho cuộc gọi ở định dạng sau: "tel: 123123123123"                         |
        │---------------|------------------------------------------------------------------------------------|
        | playAudio	    | URL của âm thanh sẽ được phát                                                      |
        │---------------|------------------------------------------------------------------------------------|
        | playVideo	    | URL của video sẽ được phát                                                         |
        │---------------|------------------------------------------------------------------------------------|
        | showImage	    | hiển thị hình ảnh được tham chiếu bởi URL                                          |
        │---------------|------------------------------------------------------------------------------------|
        | downloadFile  | URL của tệp được tải xuống                                                         |
        │---------------|------------------------------------------------------------------------------------|
        | signin	    | URL của luồng OAuth sẽ được bắt đầu                                                |
        *______________ *____________________________________________________________________________________*

        """

        return create_button(button_type, title, value)

    @staticmethod
    def create_card_attachment(card_type, title, subtitle=None, text=None, images=None, buttons=None):
        """ 
        _.Tạo tệp đính kèm thẻ ("hero", "thumbnail", "receipt"):
        card_type - loại tệp đính kèm thẻ ("hero", "thumbnail", "receipt")#https://docs.microsoft.com/en-us/microsoftteams/platform/task-modules-and-cards/cards/cards-reference
        title - tiêu đề cho thẻ của bạn. Phải là một string.
        subtitle - phụ đề cho thẻ của bạn. Phải là một string.
        text - văn bản cho thẻ của bạn. Phải là một string.
        images - list các hình ảnh, trong phần đính kèm thẻ (để tạo phương pháp sử dụng hình ảnh create_card_image). Phải là một list.
        buttons - list các nút, trong phần đính kèm thẻ (để tạo phương pháp sử dụng nút create_button). Phải là một list.
        """

        return create_card_attachment(card_type, title, subtitle, text, images, buttons)

    @staticmethod
    def create_animation_card(card_type, url, images, title, subtitle, text, buttons, autoloop=True, autostart=True,
                              shareable=True):
        """
        _.Tạo thẻ có thể phát GIF động hoặc video ngắn:

        card_type - loại tệp đính kèm thẻ ("hero", "thumbnail", "receipt")#https://docs.microsoft.com/en-us/microsoftteams/platform/task-modules-and-cards/cards/cards-reference#receipt-card
        url - mở url cho tệp hoạt hình của bạn.
        images - list các hình ảnh, trong phần đính kèm thẻ (để tạo phương pháp sử dụng hình ảnh create_card_image). Phải là một list.
        title - tiêu đề cho thẻ của bạn. Phải là một string.
        subtitle - phụ đề cho thẻ của bạn. Phải là một string.
        text - văn bản cho thẻ của bạn. Phải là một string.
        button - list các nút, trong phần đính kèm thẻ (để tạo phương pháp sử dụng nút create_button). Phải là một list.
        autoloop - mặc định:  True.
        autostart - mặc định: True.
        có thể chia sẻ - mặc định: True.
        """

        return create_animation_card(card_type, url, images, title, subtitle, text, buttons, autoloop,
                                     autostart, shareable)





    @staticmethod
    def create_item_for_adaptive_card(items):
        return items

    @staticmethod
    def create_action_for_adaptive_card(actions):
        return actions
