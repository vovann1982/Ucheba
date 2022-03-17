import telebot
from config import valuty, TOKEN
from extensions import CurrencyConverter, APIException

bot = telebot.TeleBot(TOKEN)

def preobraz (base, quote, amount):
    base = ''.join(base)
    quote = ''.join(quote or 'рубль')
    amount = ''.join(amount or '1')
    return base, quote, amount

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message: telebot.types.Message):
    bot.reply_to(message, f"Привет, {message.chat.username}")

    text = '<Валюта1>                                         |  1*Валюта1 = n рублей\n\
<Валюта1> <Валюта2>                    |  1*Валюта1 = n*Валюта\n\
<Валюта1> <Валюта2> <кол-во> | кол-во*Валюта1 = кол-во*n*Тикер2\n\
Вводить можно только название валюты по русски \n\
Список доступных валют: /valuty'
    bot.send_message(message.chat.id, text)
    pass

@bot.message_handler(commands=['valuty'])
def valuty_(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for i in valuty.keys():
       text = '\n'.join((text, i, ))
    bot.send_message(message.chat.id, text)
    pass

@bot.message_handler(content_types=['text',])
def convert(message: telebot.types.Message):
   try:
      values = [None, None, None]
      for i in range(len(message.text.split(' '))):
          values[i] = message.text.split(' ')[i]
      if len(values) > 3:
          raise APIException('Слишком много параметров.')
      base, quote, amount = preobraz(values[0], values[1], values[2])
      total_base = CurrencyConverter.get_price(base, quote, amount)
   except APIException as e:
      bot.reply_to(message, f'Ошибка пользователя.\n{e}')
   except Exception as e:
      bot.reply_to(message, f'Не удалось обработать команду\n{e}')
   else:
      text = f'Цена {amount} {base} в {quote} - {total_base}'
      bot.send_message(message.chat.id, text)
      pass




bot.polling(non_stop=True)
