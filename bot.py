import PIL
import telebot

# API должен быть записан в файл API.txt
API = open("API.txt", "r")
bot = telebot.TeleBot(API.read())


# Отклик на команду /start (Отправка изображения raspisanie.jpg)
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Загружаю расписание. Подождите.')
   
    img = open('raspisanie.jpg', 'rb')
    bot.send_photo(message.chat.id, img)    



bot.polling()

