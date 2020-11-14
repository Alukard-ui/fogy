import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
import datetime



vk = vk_api.VkApi(token="db0e54fc7ee1bf36fa925657dcbb597ef9bc3b941909a1c7852659a65f03d93b22dcda1120e2bd7ecca00")
longpoll = VkBotLongPoll(vk, '197891905')
vk = vk.get_api()
_eng_chars = u"~!@#$%^&qwertyuiop[]asdfghjkl;'zxcvbnm,./QWERTYUIOP{}ASDFGHJKL:\"|ZXCVBNM<>?"
_rus_chars = u"ё!\"№;%:?йцукенгшщзхъфывапролджэячсмитьбю.ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭ/ЯЧСМИТЬБЮ,"
_trans_table = dict(zip(_eng_chars, _rus_chars))

print('Бот запущен')

while True:
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            request = event.object.message['text'].lower()
            peer_ida = event.object.message['peer_id']
            reply = event.object.message['date']
            linka = event.object.message['attachments']
            vk.messages.send(random_id = get_random_id(), peer_id = peer_ida, message = "Чемпион")
