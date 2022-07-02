import requests
from datetime import datetime
import telebot

token = ""
bot = telebot.TeleBot(token)


req = requests.get('https://yobit.net/api/3/ticker/btc_usd')
responce = req.json()
sell_price = round(responce['btc_usd']['sell'], 2)
buy_price = round(responce['btc_usd']['buy'], 2)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Введи "цена", чтобы узнать цену BTC')

@bot.message_handler(content_types=['text'])
def tell_price(message):
    try:
        if message.text.lower() == 'цена':
            bot.send_message(message.chat.id, f'{datetime.now().strftime("%Y-%m-%d %H:%M")}\n'
                             f'Продажа: {sell_price}\nПокупка: {buy_price}')
        else:
            bot.send_message(message.chat.id, 'Я слишком глупый, и знаю только команду /start и слово "Цена"!')
    except:
        bot.send_message(message.chat.id, 'Что-то пошло не так!')

bot.polling()
