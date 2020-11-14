import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import datetime



vk = vk_api.VkApi(token="18010856fa0fdeb10105ba7c978752b588545bdd1de7b4262675e8d465d9be4ab9d78667fd7516cfe5b76")
longpoll = VkBotLongPoll(vk, '199445412')
vk = vk.get_api()

print('Бот запущен')

start = VkKeyboard(one_time=True)
start.add_button('Я из ПУНКа')

kb = VkKeyboard(one_time=False)

kb.add_button('Предложить запись', color=VkKeyboardColor.POSITIVE)

kb.add_line()
kb.add_button('Вызов админа', color=VkKeyboardColor.PRIMARY)

kb.add_line()
kb.add_button('Жалоба', color=VkKeyboardColor.NEGATIVE)

kb.add_line()
kb.add_button('Играть', color=VkKeyboardColor.DEFAULT)


while True:
    for event in longpoll.listen():
        if event.type == VkBotEventType.GROUP_JOIN:
            user_ida = event.object.message['peer_id']
            print(user_ida)
            vk.messages.send(
                random_id=get_random_id(),
                user_id = user_ida,
                keyboard=start.get_keyboard(),
                message='выбирай'
            )
        if event.type == VkBotEventType.MESSAGE_NEW:
            request = event.object.message['text'].lower()
            peer_ida = event.object.message['peer_id']
            reply = event.object.message['date']
            linka = event.object.message['attachments']
            if request == "лох":
                vk.messages.send(
                    random_id=get_random_id(),
                    peer_id=peer_ida,
                    keyboard = kb.get_keyboard(),
                    message='выбирай'
                )