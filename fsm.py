from transitions.extensions import GraphMachine

from utils import send_text_message, send_button_message
from linebot.models import MessageTemplateAction

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_state1(self, event):
        text = event.message.text
        return text.lower() == "go to state1"

    def is_going_to_state2(self, event):
        text = event.message.text
        return text.lower() == "go to state2"

    def is_going_to_homepage(self, event):
        return True

    def on_enter_state1(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state1")
        self.go_back()

    def on_exit_state1(self):
        print("Leaving state1")

    def on_enter_state2(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state2")
        self.go_back()

    def on_exit_state2(self):
        print("Leaving state2")

    def on_enter_homepage(self, event):
        print("I'm entering hompage")
        userid=event.source.user_id
        title='歡迎來到Hololive小工具！！'
        text='請選擇服務項目'
        action=[
            MessageTemplateAction(
                label='十大成員介紹',
                text='十大成員介紹'
            ),
            MessageTemplateAction(
                label='成員介紹',
                text='成員介紹'
            ),
            MessageTemplateAction(
                label='實況中',
                text='實況中'
            )
        ]
        url='https://pgw.udn.com.tw/gw/photo.php?u=https://uc.udn.com.tw/photo/2020/10/27/1/8845618.png&s=Y&x=36&y=0&sw=1906&sh=1271&sl=W&fw=1050'
        send_button_message(userid, url, title, text, action)

        self.go_back()
