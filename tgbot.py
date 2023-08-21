from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
import telebot
import os
import csv
from worker import Worker


def see(name_product):
    index_product = []
    with open('prices.csv', encoding='utf-8') as file:
        read = [*csv.reader(file, delimiter=';')]  # Создаем список где по индексу 0 название столбцов, а дальше идут магазины и цены продуктов
        for product in name_product:   # составляем список с индексами продуктов в магазинах
            index_product.append(read[0].index(product))
        d = {}
        d_min = []
        for search_product in range(1,len(read)):  # Проходим по базе данных
            if search_product == 0:   # Пропускаем строку которая является заголовками
                continue
            for price_product in index_product: # добавляем в словарь цены продуктов в каждом магазине
                d.setdefault(read[search_product][0], []).append(int(read[search_product][price_product]))
        return(min(d,key=lambda x: sum(d[x])), sum(min(d.values(),key=lambda x: sum(x)))) # возвращаем название магазина и цену где самая дешёвая корзина




load_dotenv()
TOKEN = os.getenv('TOKEN')

#app = ApplicationBuilder().token(os.getenv('TOKEN')).build()
bot = telebot.TeleBot(TOKEN)


#app.add_handler(CommandHandler("start", hello))
#app.add_handler(CommandHandler("see", start))

#app.run_polling()

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    print(message.text)
    if  message.text == '/start':
        bot.send_message(message.from_user.id, f'Hello, {message.from_user.first_name} напиши мне список продуктов который хотел бы купить через запятую')
    else:
        try:

            list_product = message.text.split(',')
            list_product = list(map(str.strip, list_product))
            list_product = [prod.capitalize() for prod in list_product]

            magazin = str(see(list_product)[0]) + ' ' + str(see(list_product)[1])
            bot.send_message(message.from_user.id, magazin + ' руб')
        except:
            bot.send_message(message.from_user.id, 'Таких продуктов нет в моей базе данных')

bot.polling(none_stop=True, interval=0)



'''async def see(name_product):
    index_product = []
    with open('prices.csv', encoding='utf-8') as file:
        read = [*csv.reader(file, delimiter=';')]  # Создаем список где по индексу 0 название столбцов, а дальше идут магазины и цены продуктов
        for product in name_product:   # составляем список с индексами продуктов в магазинах
            index_product.append(read[0].index(product))
        d = {}
        d_min = []
        for search_product in range(1,len(read)):  # Проходим по базе данных
            if search_product == 0:   # Пропускаем строку которая является заголовками
                continue
            for price_product in index_product: # добавляем в словарь цены продуктов в каждом магазине
                d.setdefault(read[search_product][0], []).append(int(read[search_product][price_product]))
        return(min(d,key=lambda x: sum(d[x])), sum(min(d.values(),key=lambda x: sum(x)))) # возвращаем название магазина и цену где самая дешёвая корзина
'''

'''async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello, {update.effective_user.first_name}, напиши мне список продуктов который хотел бы купить через пробел')



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Смотри, \n {see()}')'''