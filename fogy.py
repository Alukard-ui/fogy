import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
import datetime



vk = vk_api.VkApi(token="919e919e3815b66463acace0ec808f8e88d010e3e2863477fb93d1542a70cdc48245ee3622e9318f7320c")
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