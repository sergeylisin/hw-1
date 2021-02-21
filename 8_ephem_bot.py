"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
from ephem import Mercury, Venus, Mars, Moon, Saturn, Neptune, Uranus, constellation

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}

API_KEY = '1521578217:AAEnXxtMOFj1Y_1IhHAjVQBR5sRtRxVpC2w'

PLANETS_NAME_OBJ_MAP = {'Mercury': Mercury, 'Venus': Venus, 'Mars': Mars,
                        'Moon': Moon, 'Saturn': Saturn, 'Neptune': Neptune, 'Uranus': Uranus}
#planets = dict(map(lambda x: (x.__name__,x), planet_types))


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(text)


def planet(update, context):
    txt = update.message.text
    planet_name = txt.split()[1]
    try:
        p = PLANETS_NAME_OBJ_MAP[planet_name]()
        p.compute()
        constellation_name = constellation(p)[1]
        update.message.reply_text(constellation_name)
    except KeyError:
        update.message.reply_text("unknown planet")


def main():
    mybot = Updater(API_KEY, request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
