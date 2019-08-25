from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
from datetime import datetime

login, password = 'логин', 'пароль'
vk_session = vk_api.VkApi(token="76e64ec2c1f24ee2db2babde4072f234aa2c38de6b5c85814d890efe0460c983ac2abb550c9553a5fcc12")


session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
            print('Текст сообщения: ' + str(event.text))
            print(event.user_id)
            response=event.text.lower()
            if event.from_user and not (event.from_me):
                if response == "привет":
                    vk_session.method('messages.send',{'user_id': event.user_id, 'message': 'Привет', 'random_id': 0})
