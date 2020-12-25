from transitions.extensions import GraphMachine

from utils import send_text_message, send_button_message, send_recommend_image_carousel, send_show_message, send_living_message, send_image, send_reply_message
from linebot.models import MessageTemplateAction

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_homepage(self, event):
        return True

    def is_going_to_recommend(self, event):
        text = event.message.text
        return text == "人氣成員介紹"

    def is_going_to_showMember(self, event):
        return True

    def is_going_to_backToHompage(self, event):
        text = event.message.text
        return text == "不了"

    def is_going_to_introduce(self, event):
        text = event.message.text
        return text == "成員介紹"

    def is_going_to_living(self, event):
        text = event.message.text
        return text == "實況中"

    def is_going_to_livingBackHompage(self, event):
        return True

    def is_going_to_card(self, event):
        text = event.message.text
        return text == "抽卡"

    def is_going_to_showCard(self, event):
        text = event.message.text
        return text == "抽"

    def on_enter_homepage(self, event):
        print("I'm entering hompage")
        #userid = event.source.user_id
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
            ),
            MessageTemplateAction(
                label='抽卡',
                text='抽卡'
            )
        ]
        url = 'https://i.imgur.com/y99Dsat.jpg'
        send_button_message(event.reply_token, url, title, text, action)


    def on_enter_recommend(self, event):
        print("I'm entering recommend")
        #userid = event.source.user_id
        send_recommend_image_carousel(event.reply_token)
        print("success")

    def on_enter_showMember(self, event):
        print("I'm entering showMember")
        userid=event.source.user_id
        memberName = event.message.text
        try:
            send_show_message(userid, memberName)
            title = '要繼續看成員介紹嗎？'
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
                    label='回到主選單',
                    text='不了'
                )
            ]
            url = 'https://pbs.twimg.com/media/Enl6SeJUcAUWdrP?format=jpg&name=small'
            send_button_message(event.reply_token, url, title, text, action)
        except:
            self.go_back(event)
        #self.go_back()

    def on_enter_introduce(self, event):
        #userid=event.source.user_id
        message = "零期生\n   又稱「無印組」。\n •時乃空（Sora）\n •蘿蔔子（Roboco）\n •櫻巫女（Miko）\n •星街彗星（Suisei）\n一期生\n   除特殊標註外，均為2018年6月1日出道。\n •夜空梅露（Mel）\n •亞綺·羅森塔爾（Aki）\n •赤井心（Haato）\n •夏色祭（Matsuri）\n •白上吹雪（Fubuki）\n二期生\n •湊阿庫婭（Aqua）\n •紫咲詩音（Shion）\n •百鬼綾目（Ayame）\n •癒月巧可（Choco）\n •大空昴（Subaru）\n三期生\n   又名「Hololive Fantasy」。\n •兔田佩克拉（Pekora）\n •潤羽露西婭（Rusia）\n •不知火芙蕾雅（Flare）\n •白銀諾艾爾（Noel）\n •寶鐘瑪琳（Marine）\n四期生\n •天音彼方（Kanata）\n •桐生可可（Coco）\n •角卷綿芽（Watame）\n •常闇永遠（Towa）\n •姬森璐娜（Luna）\n五期生\n •雪花菈米（Lamy）\n •桃鈴音音（Nene）\n •獅白牡丹（Botan）\n •尾丸波爾卡（Polka）\n\nGamers\n   以遊戲實況為主的活動團體，於2018年12月6日宣布組建，2019年4月又新增成員。\n •白上吹雪（Fubuki）\n •大神澪（Mio）\n •貓又小粥（Okayu）\n •戌神沁音（Korone）\n\nhololive English是hololive production針對英語圈及國際市場推出的品牌，成立於2020年9月9日。\n一期生\n   又名「HoloMyth」。以下出道時間以日本時間（UTC+9）為準，如以北美太平洋時區計算則全部均於2020年9月12日出道。\n •森美聲（Calliope）\n •小鳥遊琪亞拉（Kiara）\n •一伊那爾栖（Ina）\n •噶嗚·古拉（Gura）\n •華生·艾米莉亞（Amelia）\n\n請輸入括號內英文名看更詳細介紹..."
        send_reply_message(event.reply_token, message)
        '''send_text_message(userid, message)
        message = "一期生\n   除特殊標註外，均為2018年6月1日出道。\n •夜空梅露（Mel）\n •亞綺·羅森塔爾（Aki）\n •赤井心（Haato）\n •夏色祭（Matsuri）\n •白上吹雪（Fubuki）"
        send_text_message(userid, message)
        message = "二期生\n •湊阿庫婭（Aqua）\n •紫咲詩音（Shion）\n •百鬼綾目（Ayame）\n •癒月巧可（Choco）\n •大空昴（Subaru）" 
        send_text_message(userid, message)     
        message = "三期生\n   又名「Hololive Fantasy」。\n •兔田佩克拉（Pekora）\n •潤羽露西婭（Rusia）\n •不知火芙蕾雅（Flare）\n •白銀諾艾爾（Noel）\n •寶鐘瑪琳（Marine）"
        send_text_message(userid, message) 
        message = "四期生\n •天音彼方（Kanata）\n •桐生可可（Coco）\n •角卷綿芽（Watame）\n •常闇永遠（Towa）\n •姬森璐娜（Luna）"
        send_text_message(userid, message) 
        message = "五期生\n •雪花菈米（Lamy）\n •桃鈴音音（Nene）\n •獅白牡丹（Botan）\n •尾丸波爾卡（Polka）"
        send_text_message(userid, message) 
        message = "Gamers\n   以遊戲實況為主的活動團體，於2018年12月6日宣布組建，2019年4月又新增成員。\n •白上吹雪（Fubuki）\n •大神澪（Mio）\n •貓又小粥（Okayu）\n •戌神沁音（Korone）"
        send_text_message(userid, message) 
        message = "hololive English是hololive production針對英語圈及國際市場推出的品牌，成立於2020年9月9日。\n\n一期生\n   又名「HoloMyth」。以下出道時間以日本時間（UTC+9）為準，如以北美太平洋時區計算則全部均於2020年9月12日出道。\n •森美聲（Calliope）\n •小鳥遊琪亞拉（Kiara）\n •一伊那爾栖（Ina）\n •噶嗚·古拉（Gura）\n •華生·艾米莉亞（Amelia）"
        send_text_message(userid, message) 
        message = "請輸入括號內英文名看更詳細介紹"
        send_text_message(userid, message) '''

    def on_enter_living(self, event):
        userid = event.source.user_id
        send_reply_message(event.reply_token, "請稍待資訊跑完再輸入...\n大約花費幾分鐘時間...\n查詢資料中......")
        send_living_message(userid)
        send_text_message(userid, "請輸入任何字反回主選單")

    def on_enter_card(self, event):
        send_reply_message(event.reply_token, "若想抽卡,請打\"抽\"\n若想離開抽卡,請打\"不了\"")
        
    def on_enter_showCard(self, event):
        send_image(event.reply_token)