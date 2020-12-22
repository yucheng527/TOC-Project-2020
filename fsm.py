from transitions.extensions import GraphMachine

from utils import send_text_message, send_button_message, send_recommend_image_carousel, send_show_message
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

    def is_going_to_recommend(self, event):
        text = event.message.text
        return text.lower() == "人氣成員介紹"

    def is_going_to_showMember(self, event):
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
        userid = event.source.user_id
        title = '歡迎來到Hololive小工具！！'
        text = '請選擇服務項目'
        action = [
            MessageTemplateAction(
                label='人氣成員介紹',
                text='人氣成員介紹'
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
        url = 'https://i.imgur.com/y99Dsat.jpg'
        send_button_message(userid, url, title, text, action)


    def on_enter_recommend(self, event):
        print("I'm entering recommend")
        userid = event.source.user_id
        send_recommend_image_carousel(userid)
        print("success")

    def on_enter_showMember(self, event):
        print("I'm entering showMember")
        userid=event.source.user_id
        memberName = event.message.text
        #try:
        send_show_message(userid, memberName)
        #except:
        self.go_back()
        #self.go_back()
        
