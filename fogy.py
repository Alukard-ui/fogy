import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import datetime



vk = vk_api.VkApi(token="b21626b6a9e092ae79a192433cf734034757323ff67c234be0120bcf076f9792f22da0d43230445372156")
longpoll = VkBotLongPoll(vk,'189309602')
vk = vk.get_api()

print('Бот запущен')

start = VkKeyboard(one_time=False)
start.add_button('Я из ПУНКа',color=VkKeyboardColor.POSITIVE)
start.add_line()
start.add_button('Из Петергофа',color=VkKeyboardColor.POSITIVE)

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
        if event.type == VkBotEventType.MESSAGE_NEW:
            request = event.object.message['text'].lower()
            peer_ida = event.object.message['peer_id']
            reply = event.object.message['date']
            linka = event.object.message['attachments']
            if request == "начать":
                vk.messages.send(
                    random_id=get_random_id(),
                    peer_id=peer_ida,
                    keyboard=start.get_keyboard(),
                    message='Откуда ты?'
                )

            if request == "я из пунка":
                vk.messages.send(
                    random_id=get_random_id(),
                    peer_id = peer_ida,
                    message =  'Привет ПУНКУ от FOGGY FROG 🐸'
                                'Наверняка думаешь, зачем попал в этот чат. Не переживай, мы ответим на все вопросы, но только лично 🙃\n\n'
                                'Приходи к нам на дымный отдых с друзьями, но для начала взгляни, что тебя ждёт :\n'
                                '📲 Instagram.com/foggyfrog.spb\n'
                                'Да, ты прав, у нас есть все - PS4, море игр, любимые напитки и вкусные кальяны 😏💨\n\n'
                                'Мы ждём по адресу 📍Чичеринская, 2 - да, верно, это в 10-ти минутах от тебя\n\n'
                                'Не забудь забронировать лучший столик по номеру 📲 89627226225 '
                )