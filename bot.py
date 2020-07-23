import requests
from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters

TOKEN = '1385978687:AAGSeBuD4hQSS2DEALZiyVgenXQzgeem4GY'


def do_start(bot: Bot, update: Update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Хочешь получить рандомную музыку?, тогда кликай /get_music , либо ты можешь найти музыку по названию, для этого отправь сообщение"
    )


def search_music(bot: Bot, update: Update):
    name = str(update.message.text)
    l = name.split()
    name2 = '+'.join(l)
    search_music = requests.get('http://127.0.0.1:8000/api/filter/?name={}'.format(name2)).json()
    array = []
    if search_music!=array:
        audio = search_music[0]['audio']
        audio_url =  audio[33:len(audio)]
        bot.send_message(chat_id=update.message.chat_id, text="Мы кажется что-то нашли, секунду...")
        bot.send_audio(chat_id=update.message.chat_id,
                       audio=open(audio_url, 'rb')
        )
    else:
        bot.send_message(
            chat_id=update.message.chat_id,
            text="Песни '{}' еще нет в нашей медиатеке".format(name)
        )


def send_music(bot: Bot, update: Update):
    music = requests.get('http://127.0.0.1:8000/api/music/').json()
    audio = music[0]['audio']
    bot.send_message(
        chat_id=update.message.chat_id,
        text='Секунду...',
    )
    bot.send_audio(chat_id=update.message.chat_id,
                   audio=open(audio, 'rb')
    )


def main():
    bot = Bot(
        token=TOKEN,
    )
    updater = Updater(
        bot=bot,
    )
    start_handler = CommandHandler("start", do_start)
    music_search_handler = MessageHandler(Filters.text, search_music)
    send_task_handler = CommandHandler("get_music", send_music)
    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(send_task_handler)
    updater.dispatcher.add_handler(music_search_handler)


    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
