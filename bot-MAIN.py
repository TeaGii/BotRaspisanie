import telebot
import datetime
import urllib.request,  os
# API должен быть записан в файл API.txt


API = open("API.txt", "r")
bot = telebot.TeleBot(API.read())


# Отклик на команду /start (Отправка изображения raspisanie.jpg)
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Подождите. Если загрузка идёт дольше секунды, то я скорее всего загружаю новое расписание.')
    
    # ПроверОЧКА на наличие картинки в папке
    if os.path.isfile('raspisanie.jpg') == False:
         img_url = "https://fpet2010.ru/rasp/25.01.jpg"
         filename = "raspisanie.jpg"
         urllib.request.urlretrieve(img_url, filename)

# Открывается текстовый файлик с датой
    with open('LastDate.txt') as file:
     LastDateString = str(file.readline())
    file.close()
    LastDate = datetime.datetime.strptime(LastDateString, '%Y-%m-%d %H:%M:%S.%f' )
    CurrentDate = datetime.datetime.now()
    DateDelta = CurrentDate - LastDate
    DateDeltaSec = DateDelta.total_seconds()
    DateDeltaHrs = int(DateDeltaSec / 60 / 60)
# Идёт проверка текущая_дата-записанная_дата в часах. Если разница больше n часов, то в файлик записывается текущая дата и происходит медленный парсинг
    if (DateDeltaHrs > 2):
        f = open("LastDate.txt", 'w')
        f.write(str(datetime.datetime.now()))
        f.close
        
                # Ссылка на изображение на сайте и название, под которым позднее сохранится изображение
        img_url = "https://fpet2010.ru/rasp/25.01.jpg"
        filename = "raspisanie.jpg"
        # Если файл расписания уже имеется, то он будет удалён
        if os.path.isfile("raspisanie.jpg"):
                os.remove("raspisanie.jpg")
                print("ФАЙЛ БЫЛ УДАЛЁН")
                # Через библиотеку urllib получается изображение с сайта ФПЭТ
                urllib.request.urlretrieve(img_url, filename)

    img = open('raspisanie.jpg', 'rb')
    bot.send_photo(message.chat.id, img)    
    bot.send_message(message.chat.id, 'Расписание взято с сайта fpet2010.ru и может быть не актуальным на данный момент')

# Отклик на любое сообщение кроме команд
@bot.message_handler(content_types=['text'])
def lalala(message):
    bot.send_message(message.chat.id, 'Привет. Я - бот, который пока что умеет только отправлять расписание ГБПОУ "ФПЭТ". Чтобы начать работу - напиши команду "/start"' )
bot.polling(True)

