
import vk_api
import json
import random
import requests 
import goslate
import lxml
from bs4 import BeautifulSoup
from datetime import datetime
from vk_api.longpoll import VkLongPoll, VkEventType

from modules.course import getCourse
from modules.weather import getWeather
from modules.wiki import get_summary



def create_button(text, color, payload = ""):
    return { 
        "action": { 
          "type": "text", 
          "payload": json.dumps(payload), 
          "label": text 
        }, 
        "color": color 
      }

keyboard = {
    "one_time": False,
     "buttons":[
         [
             create_button("вариант огэ. математика", "primary"), 
             create_button("вариант огэ. русский", "default"),
             
             ]
         ]
    }


hello = '''Привет! Для начала расскажу, что я умею. 
                Могу сказать, сколько градусов на данный момент в Москве, для этого отправь мне "г". 
                Также я могу сказать курс валют по отношению к Российскому Рублю. 
                Если хочешь узнать курс Доллара, отправь мне "д". 
                Если хочешь узнать курс Евро, отправь мне "е", если хочешь узнать курс Фунтов Стерлингов Соединенного королевства, отправь мне "ф". 
                Если хочешь порешать пробники огэ по математике или русскому, можешь воспользоваться соответствующими кнопками. 
                Ещё я умею переводить твои сообщения на английский. Для этого используй флаг "п", после этого через пробел введите текст. 
                Я могу достать информацию из Википедии по любому существующему запросу.
                Для этого используй флаг "в", после этого через пробел введите запрос.'''

keyboard = json.dumps(keyboard, ensure_ascii = False)


gs = goslate.Goslate()

def main():

    token = ""

    vk_session = vk_api.VkApi(token = token)

    vk = vk_session.get_api()

    longpoll = VkLongPoll(vk_session)

    for event in longpoll.listen():

        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            msg_text = event.text.lower() 
            msg_text = msg_text.replace(" ", "_")
            message_id = event.message_id
            query = msg_text[3:]

            if event.text == 'Привет' or event.text == 'Начать' or event.text == '?': 
                    vk.messages.send(user_id = event.user_id, random_id = message_id, message = hello, keyboard = keyboard)
                    pass
        
            elif event.text == 'Пока' or event.text == 'пока':
                vk.messages.send(user_id = event.user_id, random_id = message_id, message = "Всего доброго! Приходи ещё.")

            elif event.text == "вариант огэ. математика":
                vk.messages.send(user_id = event.user_id, random_id = message_id, message = "https://math-oge.sdamgia.ru")

            elif event.text == "вариант огэ. русский":
                vk.messages.send(user_id = event.user_id, random_id = message_id, message = "https://rus-oge.sdamgia.ru")
        
            elif event.text[:2] == "-д" :
                vk.messages.send(user_id = event.user_id, random_id = message_id, message = getCourse("R01235"))

            elif event.text[:2] == "-ф":
                vk.messages.send(user_id = event.user_id, random_id = message_id, message = getCourse("R01035"))

            elif event.text[:2] == "-е":
                vk.messages.send(user_id = event.user_id, random_id = message_id, message = getCourse("R01239"))

            elif event.text[:2] == "-в":
                    vk.messages.send(user_id = event.user_id, random_id = message_id,  message = get_summary(query))

            elif event.text[:2] == "-г":
                vk.messages.send(user_id = event.user_id, random_id = message_id, message = getWeather())

            elif event.text[:2] == "-п": 
                    query.replace("_", " ")
                    try:
                        query = gs.translate(query, "en")
                        vk.messages.send(user_id = event.user_id, random_id = message_id,  message = query)
                    except Exception:
                        vk.messages.send(user_id = event.user_id, random_id = message_id,  message = "Придётся подождать.\nСервер перегружен")


     
            else:
                vk.messages.send(user_id = event.user_id, random_id = message_id, message = "Я вас не понимаю")
print("i'm working")


if __name__ == "__main__":
    main()