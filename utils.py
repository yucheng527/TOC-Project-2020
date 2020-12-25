import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ButtonsTemplate, TemplateSendMessage, ImageCarouselColumn, MessageTemplateAction, ImageCarouselTemplate, FlexSendMessage, ImageSendMessage
import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random

channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
name = ['Sora', 'Roboco', 'Miko', 'Suisei', 'Mel', 'Aki', 'Haato', 'Matsuri', 'Fubuki', 'Aqua', 'Shion', 'Ayame', 'Choco', 'Subaru', 'Pekora', 'Rusia', 'Flare', 'Noel', 'Marine', 'Kanata', 'Coco', 'Watame', 'Towa', 'Luna', 'Lamy', 'Nene', 'Botan', 'Polka', 'Mio', 'Okayu', 'Korone','Calliope', 'Kiara', 'Ina', 'Gura', 'Amelia']
id = ['UCp6993wxpyDPHUpavwDFqgg', 'UCDqI2jOz0weumE8s7paEk6g', 'UC-hM6YJuNYVAmUWxeIr9FeA', 'UC5CwaMl1eIgY8h02uZw7u8A', 'UCD8HOxPs4Xvsm8H0ZxXGiBw', 'UCFTLzh12_nrtzqBPsTCqenA', 'UC1CfXB_kRs3C-zaeTG3oGyg', 'UCQ0UDLQCjY0rmuxCDE38FGg', 'UCdn5BQ06XqgXoAxIhbqw5Rg', 'UC1opHUrw8rvnsadT-iGp7Cg', 'UCXTpFs_3PqI41qX2d9tL2Rw', 'UC7fk0CB07ly8oSl0aqKkqFg', 'UC1suqwovbL1kzsoaZgFZLKg', 'UCvzGlP9oQwU--Y0r9id_jnA', 'UC1DCedRgGHBdm81E1llLhOQ', 'UCl_gCybOJRIgOXw6Qb4qJzQ', 'UCvInZx9h3jC2JzsIzoOebWg', 'UCdyqAaZDKHXg4Ahi7VENThQ', 'UCCzUftO8KOVkV4wQG1vkUvg', 'UCZlDXzGoo7d44bwdNObFacg', 'UCS9uQI-jC3DE0L4IpXyvr6w', 'UCqm3BQLlJfvkTsX_hvm0UmA', 'UC1uv2Oq6kNxgATlCiez59hw', 'UCa9Y57gfeY0Zro_noHRVrnw', 'UCFKOVgVbGmX65RxO3EtH3iw', 'UCAWSyEs_Io8MtpY3m-zqILA', 'UCUKD-uaobj9jiqB-VXt71mA', 'UCK9V2B22uJYu3N7eR_BT9QA', 'UCp-5t9SrOQwXMU7iIjQfARg', 'UCvaTdHTWBGv3MKj3KVqJVCw', 'UChAnqc_AY5_I3Px5dig3X1Q', 'UCL_qhgtOy0dy1Agp8vkySQg', 'UCHsx4Hqa-1ORjQTh9TYDhww', 'UCMwGHR0BTZuLsmjY_NT5Pwg', 'UCoSrY_IQQVpmIRZ9Xf-y93g', 'UCyl1z3jo3XHR1riLFKG5UAg']
twitter = [
    'https://twitter.com/tokino_sora',
    'https://twitter.com/robocosan',
    'https://twitter.com/sakuramiko35',
    'https://twitter.com/suisei_hosimati',
    'https://twitter.com/yozoramel',
    'https://twitter.com/akirosenthal',
    'https://twitter.com/akaihaato',
    'https://twitter.com/natsuiromatsuri',
    'https://twitter.com/shirakamifubuki',
    'https://twitter.com/minatoaqua',
    'https://twitter.com/murasakishionch',
    'https://twitter.com/nakiriayame',
    'https://twitter.com/yuzukichococh',
    'https://twitter.com/oozorasubaru',
    'https://twitter.com/usadapekora',
    'https://twitter.com/uruharushia',
    'https://twitter.com/shiranuiflare',
    'https://twitter.com/shiroganenoel',
    'https://twitter.com/houshoumarine',
    'https://twitter.com/amanekanatach',
    'https://twitter.com/kiryucoco',
    'https://twitter.com/tsunomakiwatame',
    'https://twitter.com/tokoyamitowa',
    'https://twitter.com/himemoriluna',
    'https://twitter.com/yukihanalamy',
    'https://twitter.com/momosuzunene',
    'https://twitter.com/shishirobotan',
    'https://twitter.com/omarupolka',
    'https://twitter.com/ookamimio',
    'https://twitter.com/nekomataokayu',
    'https://twitter.com/inugamikorone',
    'https://twitter.com/moricalliope',
    'https://twitter.com/takanashikiara',
    'https://twitter.com/ninomaeinanis',
    'https://twitter.com/gawrgura',
    'https://twitter.com/watsonameliaEN'
]
context = [
    'hololive零期生\n\n跟四天王幾乎同時期存在的元祖vtuber，走王道偶像唱歌路線，外加點滿的恐怖耐性，以及媽媽般的包容力，讓視聽者都退化成了幼稚園小孩。\n\n近期轉變風格開始在家直播一些雜談或是演奏練習，偶爾也有懷舊以及恐怖遊戲。',
    'hololive零期生\n\nkuromaru9氏依照自己的愛好所製成的3D模組，後來賣給公司，相較於一期生算是很早就出道，走穩扎穩打實況路線，除了固定放送外突擊放送也非常頻繁，外交實力很強，雖然自稱高性能機器人，但是常常被觀眾嘲諷”這就是高性能 ”。也曾經與彩虹社的阿凜、楓合作過，但是個人特色不強，因此人氣上升速度只能算普通，由於海外兄貴大量湧入hololive，出現不知道RBC是hololive 0期生的窘境。',
    'hololive零期生\n\n很喜歡エロgame，歸屬於hololive之後人氣上漲，與彩虹社的狗以及個人勢星月/書法家/板手關係不錯，目前因存在感太稀薄成為不人氣角色之一。\n\n但因GTA5的尼哥影片被外國人剪輯瘋狂轉推，意外造成海外人氣大漲，巫女也藉勢持續實況，造就觀眾數量大增，長久的努力終於有了相當的回報。\n\n為holo MC常客，常有自滅舉動，人氣穩定成長中，因為與三期生兔田打鬧很有趣聲勢大漲，但遊戲還是常需要人介護，屬於凡人努力打拼上來的類型，一開始接觸可能沒甚麼特色，但是知道她努力痕跡的人會默默支持她，證明無論多麼底邊或是沒特色還是有往上爬的一天。\n\n之後瘋狂ARK被ARK官方關注，被認證為ARK廢人 (最近ARK時數有被巧可老師跟蘋果超越的跡象)。因為先天遺傳疾病發作目前休養中，目前已經回歸。',
    'hololive零期生\n\n個人勢轉進hololive的成員，以唱歌勢出道，除唱歌之外也擅長繪圖以及專精俄羅斯方塊，遊戲能力不錯。在3D演唱會大放異彩，人氣大幅成長。\n\n號稱六邊形戰士，意思是樣樣都通，意外的是英文能力卻不怎麼樣。',
    'hololive一期生\n\n從外部請來的打手，原來經營的youtube頻道已超過10萬人，以ASMR實況為主，放送頻率很低，因此人氣上升緩慢，開始嘗試不同實況風格，但由於YT君對金髮巨乳審查嚴格，頻道經常被隱藏。',
    'hololive一期生\n\n人妻型 liver，由於早期網路問題失去了很多實況機會，雖然後來有急起直追但為時已晚，屬於電腦白癡的類型，經常開深夜實況以及ASMR，不人氣代表之一，因ASMR被水管取消收益化。\n\n收益復原後積極經營ARK大成功，人氣大幅成長。',
    'hololive一期生\n\n努力的代言人，有一陣子常常一日兩次實況，但早期因為2DLIVE沒調整好，表情捕捉很怪，又有網路問題，導致人氣上不去，現在已經改善很多，傲嬌角色，觀眾的代表物是被斬首的豬，英文能力不錯，遊戲能力差，以雜談為主，情緒浮動很大。\n\n因ASMR使用羅莉當標題被水管取消收益化，反而激起對抗心頻繁實況，用英語實況吸收了許多歐美觀眾，之後去菲律賓留學活動休止，歐美觀眾則順利引導到4期生可可會長的頻道。\n\n回澳洲後又積極開播，與會長合作良好，人氣大幅提升，自稱為はあちゃま，澳洲狂人代表。',
    'hololive一期生也在hololive Gamers兼任隊長\n\n一開始強烈的個性讓人印象深刻，擅長猩猩叫，最初與吹雪合作時兩人就在百合營業，對狐狸求愛被拒絕，因為本職是新人聲優很忙碌，前期沒有時間實況，個性又是蘿莉控大叔。\n\n失去了竄紅的機會，最近雖然放送頻率增加但是表現保守許多。與狐狸合作時，會用夏色吹雪當作標題，對於繪圖跟唱歌也非常拿手，狐狼組團後，與吹雪的互動降低很多。\n\n由於已經從聲優學校畢業，目前專心以實況為主，在二期生各種開放的個性下逐漸恢復原有的下捏他性騷擾實況風格，被會長稱為hololive的癌。',
    'hololive一期生\n\n唯一在hololive中以驚人速度成長的liver，以可愛的聲音跟貓叫聲著名，偶爾會黑化展現帥氣的聲線。FGO廢人，非常喜歡克蘇魯系列的TRPG，繪圖/唱歌/料理/遊戲/MMD無一不精，跟任何vtuber都能合作，不論是跟偶像部/彩虹社/有閒喫茶/ 各個バ美肉大叔 都建立良好的關係，不愧是吹雪　(さすフブ)，擁有七色聲線，能扮演TRPG任何角色。\n\n由於初放送時把すき說成すこ，後來就將錯就錯把代表物當成玉米(Corn)。\n擅長的遊戲是麥塊終界龍RTA跟DbD的豬女。\n\n個性十分深謀遠慮，對於司儀以及vtuber對應十分擅長，具有強大的野心跟慾望。\n\n成立hololive gamers，FAMS成員之一。之後將gamers也加了近來組成了OKFAMS，在ARK流行時期扮演可靠的凱瑟琳媽媽。\n近期因愚人節促成新的團體バカタレ共(笨蛋同盟)，一起玩恐怖遊戲或是看蠟筆小新劇場版等節目。在20年8月21號因為船長跟詩音早晨線下會沒準時開台，特別開了一台待機實況，整整雜談了4個小時，誕生了2詩音=1ババ的新名詞。\n\n將Phasmophobia這款抓鬼遊戲玩破百等，帶團一起與成員同樂。',
    'hololive二期生最強王牌\n\n笨手笨腳系女僕，非常努力在實況，大多以遊戲為主，各種玩梗發狂企劃，聲音卻清純可愛造成反差萌。\n\nFPS/TPS高手，有五次solo PUBG吃雞的實況，經常在PUBG跟麥塊自爆各種黑歷史，hololive職業廢人玩家，達成2周目無傷斬劍聖一心以及5周目隻狼58分破關，金壺，歌唱能力很高，但英文/漢字/常識力很低。\n\n24小時實況中的底特律變人創下hololive有史以來最高同時觀眾數(14036)，之後觀眾數量激增，由於一年約到期與營運續約意見不合，而休息一周，回歸後與營運達成協議繼續實況，之後又創下女性Vtuber第一個馬力歐maker2第一位S帶以及用100殘機完成人氣100關卡的傳說。\n\n在19年8月31號完成節奏天國全完美偉業，20年1月18號用共7小時半破關超魔界村。一度以觀眾參加大亂鬥節目達到人氣頂峰，而後又因ARK 離開部落以及大亂鬥職業選手亂入事件降低人氣，目前又瘋狂沉迷APEX。近期有10分內壺，Jump king通關等成績。\n\n20年8月21號初次sololive演唱會，以新的3D婚紗造型亮麗演出。\n20年11月15號大亂鬥耐久花費6小時15分進入VIP房。',
    'hololive二期生\n\n死小孩性格，由於造型的關係受到各種蘿莉控繪師的關注，創作的插畫品質最高也最豐富，但是缺乏企劃能力又有溝通障礙在人氣成長上受限。\n\n曾經開台遲到過兩小時，狐狸開待機實況撐場了2小時，此後奠定1詩音=2小時的遲到新單位。\n\n之後因為跟女僕在麥塊互動而人氣提升，與會長的互動也誕生了シオンよ．．．名句，是會長的無敵男友，人氣超幅成長，但因為到處出軌被會長認證為メスクソガキ。',
    'hololive二期生\n\n由於人設的關係獲得不錯的關注度，呆萌型角色，唱歌也很好聽，FAMS成員之一，記憶力很差，常時會進入虛無狀態。\n\n沉迷於LOL以及APEX。',
    'hololive二期生\n\n實況廢人，擅長DbD，對於合作企劃很拿手，因為ASMR受到海外關注而訂閱數上漲，缺點是說話有輕微的大舌頭，因ASMR被水管取消收益化。\n\n收益化回復後努力經營其他項目，在ARK表現不錯人氣有回升的跡象，由於金髮巨乳太過色情已經被YT君鎖定成隱藏常客。',
    'hololive二期生\n\n搞笑型藝人，各種謎企劃，與原Seeds的舞元以及繪師時雨媽關係不錯，所有成員中最自由的人，由於唐老鴨ASMR聲勢大漲，從最底層一路暴衝到中層，也是內部連接彩虹社的橋梁，大家的開心果，FAMS成員之一。',
    'hololive三期生\n\n語尾帶ぺこ，RAP藝人以及暴言擔當，遊戲反射神經還不錯，努力家，唱歌能力跟女僕差不多。\n\n在holo MC非常活躍，吸引了許多箱內觀眾，心理測試顯示為強勢腹黑策士愛錢性格。\n\n三期生的王牌，與巫女有強大的信賴關係，唯一敢對其惡作劇的前輩。\n\n由於有嚴重的交流障礙，線下時常常因為緊張存在感薄弱，被戲稱為網路弁慶。\n破關超魔界村以及不使用即時存檔接關過完號稱最鬼畜的馬利歐2。\n\n在ARK流行時一度組成CAMP ARK四大廢人，換地圖後遊玩時數下降，沉迷於MGS後人氣超幅成長。\n\n特徵是具備魔性的笑聲HA↗HA↘HA↗HA↘。',
    'hololive三期生\n\n可愛擔當，有時會顯露出抖S的氣質，是電腦白痴，實況內容以手機恐怖遊戲，雜談，寶可夢等等。\n\n在三期生線下會時解放性格，聲音出奇的大，一句"活該"徹底改變配信風格，成了遜炮奇聲藝人，換新衣裝後從綠毛變成粉毛。\n\n由於初號機影片的關係，有更多人認識這位狂戰士。',
    'hololive三期生\n\n擅長繪圖跟企畫合作的聯絡人，中性姊貴的聲音，陽角。holo MC廢人擔當，像是守護妖精一樣暗地的維護holo MC。\n個性開朗很會照顧人，跟團長關係非常要好，被女僕稱為第二媽媽。\n\n中性聲線非常的帥氣，連狐狸也抵擋不住，不經意會作出貼心男友的舉動。',
    'hololive三期生\n\n蠢萌エロ大姊姊擔當，不太擅長玩遊戲，清楚的SSR聲線出道2周訂閱隨即突破3萬人，一舉超越率先出道的兔田與死靈。\n\n腦筋團長的實況內容以雜談或是ASMR居多，玩遊戲需要人介護，因ASMR被水管取消收益化。\n\n收益化回復後將ASMR改成立體音響，食量很大，與不知火是一對。',
    'hololive三期生\n\n繪圖能力專業級的藝人，跟死靈有明顯的百合營業。\n\n船長由於聲音酷似大谷育江而且唱歌的選曲久遠，被人懷疑有50歲，常玩光彥梗。\n目前開始大量合作而與犬山老師有交流，強力推廣櫻花大戰與東方，雜談力堪稱hololive最強，有許多搞笑舉動，社畜時期被稱為不可思議之子。',
    'hololive四期生\n\n遜炮天使，初配信以ソーラン節引起熱烈回響，以遊戲配信為主，想要學兔田挑戰超魔界村卻連連失敗終於動用即時存檔，唱歌跟雜談都不錯，由於初配信以及之後都很喜歡用PPT作雜談節目，被會長冠上PP天使的綽號，簡稱PP，唱低音歌曲的能力非常強大，自稱以燃燒生命的方式唱歌，具有煽動人心的魔力。老毛病檢查出院後歌唱功力明顯不如以往。\n\n目前PP天使，會長與星街同居中，稱為同居組。',
    'hololive四期生\n\n君臨hololive的外國龍王，初配信以史詩動畫爆破holo本社，早晨的可可live則類似VB各種玩梗嘲諷的20分鐘配信，日文用詞很迷，有很重的外國口音，幫助四期生玩出各種特色，是四期生的中心人物。\n\n曾經被youtube AI BAN過直播權數天又解除，正是桐生之龍不可或缺的經歷。\n\n將ARK風潮推廣到hololive之中引起極大的熱潮，但與麥塊命運相同也不免落入遊玩人數減少的命運。',
    'hololive四期生\n\n聲音酷似有地方口音的唯媽，網路雜魚，可能有羊騷味，唱歌功力不錯，網路斷線變成一種梗每次斷線觀眾都會幫忙計數，目前最高次數一次配信斷線61次，自創RAP的能力驚人。\n\n網路問題解決後與會長密切合作，穩定成長中。',
    'hololive四期生\n\n擅長FPS遊戲，經常在早上進行直播，唱歌有獨特的低音聲線，海外觀眾居多。',
    'hololive四期生\n\n幼兒般的聲音，喜歡老遊戲，與FAMS成員混得不錯，因為聲音很欠打跟船長或486組合效果出眾，深夜電子琴節目獲得不錯的回響。',
    'hololive五期生\n\n由於一開始出道給予成員鼓勵的聲音，被當作媽媽看待，連狐狸也拿了一份，主要在早晨雜談直播，魔性之女，不自覺勾引許多人，酒中豪傑。',
    'hololive五期生\n\n由於中華風一開始並不討喜，但由於標題圖跟實況方式太過遜炮，反而誕生獨一無二的特色，日常ね又遜，唱歌有實力又很可愛，由於實況Good Job!在遊戲中大肆破壞以及麥塊建造5期生大樓另有社長的稱呼。',
    'hololive五期生\n\nHololive有史以來最強遊戲勢，擅長各種歐美遊戲，COD，R6，APEX等等。\n\n電腦為自組PC，使用2PC實況。\n在巧可老師身體檢測合作學力測驗項目拿到28點，是目前合作對象中最高成績。\n被5期生戲稱為什麼都做得到的獅白牡丹。',
    'hololive五期生\n\n出道後即刻各種玩梗的狂人，以廢片混合直播的方式，遊戲玩得很爛，但是雜談自由奔放，由於雜談會出現與平常極大的失落反差，被reddit拿來玩小丑梗，放開RP後歌唱功力極高。',
    '由狐狸所企劃的組織，hololive Gamers成員\n\n作為狐狸的親友登場，經由狐狸的絕讚推廣，人氣快速上升中，擅長的遊戲是烏賊娘，個性認真，為狐狸的副手，由於經驗老道加上台風很穩，擅長做整合箱內成員的企劃，FAMS成員之一，塔羅牌占卜節目很受歡迎，經常傾聽內部成員的心聲，被當成hololive的母親。\n\n由於卡普空版權問題未經授權播放到劇情向遊戲，營運正在與卡普空洽談中。',
    '由狐狸所企劃的組織，hololive Gamers成員\n\n專精老遊戲，有沉穩的聲線，深夜放送時聽起來很舒適，狗狗的介護者，唱歌時帥氣的聲線深受狐狸的賞識，個性懶散，合作時性格會變成強勢的搞笑藝人，喜歡在holo MC中對其他人惡作劇。',
    '由狐狸所企劃的組織，hololive Gamers成員\n\n未正式出道因在烏賊娘虐殺486，被冠稱"ぶっころね" 殺人狗的稱號，初配信事故連連，需要其他三位gamers的看護，天然病嬌發言被視為新的問題兒童，喜歡恐怖跟獵奇電影，但討厭蟲跟幽靈，各種奇言奇行讓實況很有趣，專長遊戲是烏賊娘。\n\n以懷舊遊戲深夜耐久配信為主，風格為給社會人看的療育(病嬌)型老奶奶。',
    'hololiveEN一期生\n\nRap之神，剛出道就發布一堆原創曲，酒豪，喜好雜談。',
    'hololiveEN一期生\n\n不死鳥，精通日文與德文，各種企劃遊戲嘗試中。',
    'hololiveEN一期生\n\n超越船長的神繪師，冷笑話大叔，用冷笑話破壞觀眾的SAN值。',
    'hololiveEN一期生\n\n可愛的化身，出道的"a"生產了一堆meme，擅長音遊，幹話王，是可愛的屁孩類型，曾經有MC 3小時只做了1道門的偉業，唱歌非常可愛。',
    'hololiveEN一期生\n\n一出場就吃毒，被稱作2代はあちゃま，喜歡FPS遊戲，嘴王，與鯊魚關係很好。'
]

def send_text_message(user_id, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.push_message(user_id, TextSendMessage(text=text))
    
    return "OK"

#def send_idol_image_carousel(user_id):



def send_button_message(user_id, image_url, title, text, action):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            thumbnail_image_url=image_url,
            title=title,
            text=text,
            actions=action
        )
    )
    #print("check1")
    line_bot_api.push_message(user_id, message)
    #print("check2")
    return "OK"

def send_recommend_image_carousel(user_id):
    line_bot_api = LineBotApi(channel_access_token)
    gur = 'https://user-images.strikinglycdn.com/res/hrscywv4p/image/upload/c_limit,fl_lossy,h_1000,w_500,f_auto,q_auto/1369026/251247_457554.jpg'
    kor = 'https://user-images.strikinglycdn.com/res/hrscywv4p/image/upload/c_limit,fl_lossy,h_1000,w_500,f_auto,q_auto/1369026/305905_549251.png'
    fub = 'https://user-images.strikinglycdn.com/res/hrscywv4p/image/upload/c_limit,fl_lossy,h_1000,w_500,f_auto,q_auto/1369026/215939_891350.png'
    pek = 'https://user-images.strikinglycdn.com/res/hrscywv4p/image/upload/c_limit,fl_lossy,h_1000,w_500,f_auto,q_auto/1369026/231089_544274.png'
    aqu = 'https://user-images.strikinglycdn.com/res/hrscywv4p/image/upload/c_limit,fl_lossy,h_1000,w_500,f_auto,q_auto/1369026/309110_49678.png'
    mar = 'https://user-images.strikinglycdn.com/res/hrscywv4p/image/upload/c_limit,fl_lossy,h_1000,w_500,f_auto,q_auto/1369026/363888_28473.png'
    coc = 'https://user-images.strikinglycdn.com/res/hrscywv4p/image/upload/c_limit,fl_lossy,h_1000,w_500,f_auto,q_auto/1369026/433211_700099.jpeg'
    haa = 'https://user-images.strikinglycdn.com/res/hrscywv4p/image/upload/c_limit,fl_lossy,h_1000,w_500,f_auto,q_auto/1369026/970398_960056.png'
    mor = 'https://user-images.strikinglycdn.com/res/hrscywv4p/image/upload/c_limit,fl_lossy,h_1000,w_500,f_auto,q_auto/1369026/603788_561144.jpg'
    rus = 'https://user-images.strikinglycdn.com/res/hrscywv4p/image/upload/c_limit,fl_lossy,h_1000,w_500,f_auto,q_auto/1369026/975809_103938.png'
    images = [gur, kor, fub, pek, aqu, mar, coc, haa, mor, rus]
    labels = ['がうる・ぐら', '戌神ころね', '白上フブキ', '兎田ぺこら', '湊あくあ', '宝鐘マリン', '桐生ココ', '赤井はあと', '森美声', '潤羽るしあ']
    texts = ['Gura', 'Korone', 'Fubuki', 'Pekora', 'Aqua', 'Marine', 'Coco', 'Haato', 'Calliope', 'Rushia']
    cols = []
    for i in range(10):
        cols.append(
            ImageCarouselColumn(
                image_url=images[i],
                action=MessageTemplateAction(
                    label=labels[i],
                    text=texts[i]
                )
            )
        )
    message = TemplateSendMessage(
        alt_text='ImageCarousel template',
        template=ImageCarouselTemplate(columns=cols)
    )
    line_bot_api.push_message(user_id, message)
    return "OK"

def send_show_message(user_id, memberName):
    line_bot_api = LineBotApi(channel_access_token)
    if memberName in name:
        index = name.index(memberName)
        chrome = webdriver.Chrome("./chromedriver")
        chrome.get("https://www.youtube.com/channel/"+id[index])
        #time.sleep(1)
        soup = BeautifulSoup(chrome.page_source, "html.parser")
        chrome.close()
        channel_name = soup.find("yt-formatted-string", {"id": "text", "class": "style-scope ytd-channel-name"}).text
        channel_avatar = soup.find("img", {"id": "img", "class": "style-scope yt-img-shadow"})["src"]
        subscriber = soup.find("yt-formatted-string", {"id": "subscriber-count", "class": "style-scope ytd-c4-tabbed-header-renderer"}).text
        subscriber = subscriber.replace("subscribers", "訂閱")
        channel_banner = soup.find("ytd-c4-tabbed-header-renderer", {"class": "style-scope ytd-browse"})["style"]
        channel_banner = channel_banner[24::]
        channel_banner = channel_banner.replace('\\', '')
        channel_banner = channel_banner[0:channel_banner.find('='):]
        message = {
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "image",
                                "url": channel_banner,
                                "size": "full",
                                "aspectMode": "cover",
                                "aspectRatio": "500:110",
                                "gravity": "center",
                                "flex": 1
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "image",
                                    "url": channel_avatar,
                                    "aspectMode": "cover",
                                    "size": "full",
                                    "margin": "none"
                                }
                                ],
                                "cornerRadius": "100px",
                                "width": "72px",
                                "height": "72px"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "text",
                                    "contents": [
                                    {
                                        "type": "span",
                                        "text": channel_name,
                                        "size": "md",
                                        "weight": "regular",
                                        "decoration": "none"
                                    }
                                    ],
                                    "size": "sm",
                                    "wrap": True
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": subscriber,
                                        "size": "sm",
                                        "color": "#bcbcbc"
                                    }
                                    ],
                                    "spacing": "sm",
                                    "margin": "md"
                                }
                                ],
                                "offsetTop": "xl"
                            }
                            ],
                            "spacing": "xl",
                            "paddingAll": "20px",
                            "margin": "none"
                        }
                        ],
                        "paddingAll": "0px"
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "uri",
                            "label": "Youtube",
                            "uri": "https://www.youtube.com/channel/"+id[index]
                            },
                            "margin": "xs",
                            "height": "sm"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "uri",
                            "label": "Twitter",
                            "uri": twitter[index]
                            },
                            "margin": "none",
                            "height": "sm"
                        }
                        ],
                        "margin": "none",
                        "spacing": "none"
                    }
                }
        line_bot_api.push_message(user_id, TextSendMessage(text=context[index]))
        line_bot_api.push_message(user_id, FlexSendMessage(alt_text='flex', contents=message))
        return "OK"
    else:
        line_bot_api.push_message(user_id, TextSendMessage(text='請輸入正確名稱'))
        raise ValueError('name is not matched')
        
def send_living_message(user_id):
    line_bot_api = LineBotApi(channel_access_token)
    chrome = webdriver.Chrome("./chromedriver")
    lst = []
    for i in range(len(id)):
        try:
            print(len(lst))
            chrome.get("https://www.youtube.com/channel/"+id[i])
            WebDriverWait(chrome, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-thumbnail-overlay-time-status-renderer[class='style-scope ytd-thumbnail']")))
            #chrome.implicitly_wait(10)
            #time.sleep(2)
            soup = BeautifulSoup(chrome.page_source, "html.parser")
            living_now = soup.find("ytd-thumbnail-overlay-time-status-renderer", {"class": "style-scope ytd-thumbnail", "overlay-style": "LIVE"}).text
            channel_tag = soup.find("a", {"id": "video-title", "class": "yt-simple-endpoint style-scope ytd-video-renderer"})
            video_id = channel_tag["href"]
            video_title = channel_tag["title"]
            video_image = soup.find("img", {"id": "img", "class": "style-scope yt-img-shadow", "width": "246"})["src"]
            video_image = video_image[0:video_image.find("?")]
            message = {
                        "type": "bubble",
                        "header": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                {
                                    "type": "image",
                                    "url": video_image,
                                    "size": "full",
                                    "aspectMode": "cover",
                                    "aspectRatio": "480:270",
                                    "gravity": "center",
                                    "flex": 1
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": "Live",
                                        "size": "xs",
                                        "color": "#ffffff",
                                        "align": "center",
                                        "gravity": "center"
                                    }
                                    ],
                                    "backgroundColor": "#EC3D44",
                                    "paddingAll": "2px",
                                    "paddingStart": "4px",
                                    "paddingEnd": "4px",
                                    "flex": 0,
                                    "position": "absolute",
                                    "offsetStart": "18px",
                                    "offsetTop": "18px",
                                    "cornerRadius": "100px",
                                    "width": "48px",
                                    "height": "25px"
                                }
                                ]
                            }
                            ],
                            "paddingAll": "0px"
                        },
                        "body": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "contents": [],
                                        "size": "md",
                                        "wrap": True,
                                        "text": video_title,
                                        "color": "#ffffff",
                                        "weight": "bold"
                                    }
                                    ],
                                    "spacing": "sm"
                                },
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                    {
                                        "type": "button",
                                        "action": {
                                        "type": "uri",
                                        "label": "點我看直播",
                                        "uri": "https://www.youtube.com"+video_id
                                        },
                                        "height": "sm",
                                        "style": "link",
                                        "color": "#ffffff"
                                    }
                                    ],
                                    "paddingAll": "13px",
                                    "cornerRadius": "2px",
                                    "margin": "xl",
                                    "backgroundColor": "#ffffff1A",
                                    "paddingTop": "xs",
                                    "paddingBottom": "xs"
                                }
                                ]
                            }
                            ],
                            "paddingAll": "20px",
                            "backgroundColor": "#464F69"
                        }
                    }
            lst.append(message)
        except:
            continue
    chrome.close()
    if len(lst) == 0:
        line_bot_api.push_message(user_id, TextSendMessage(text="目前沒有直播QQ"))
    else:
        for i in range(len(lst)):
            line_bot_api.push_message(user_id, FlexSendMessage(alt_text='flex', contents=lst[i]))   

def send_image(user_id):
    line_bot_api = LineBotApi(channel_access_token)
    url = "https://yande.re/post?page="+str(random.randint(1,20))+"&tags=hololive"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    image = soup.find_all("a", {"class": "directlink largeimg"})
    image_url = image[random.randint(0, len(image)-1)]["href"]
    line_bot_api.push_message(user_id, ImageSendMessage(original_content_url=image_url, preview_image_url=image_url))
    #print(image[random.randint(0, len(image)-1)]["href"])   
"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
