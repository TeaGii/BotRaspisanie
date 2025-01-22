import urllib.request,  time, os


while True:
    # Ссылка на изображение на сайте и название, под которым позднее сохранится изображение
    img_url = "https://fpet2010.ru/rasp/25.01.jpg"
    filename = "raspisanie.jpg"
    # Если файл расписания уже имеется, то он будет удалён
    if os.path.isfile("raspisanie.jpg"):
        os.remove("raspisanie.jpg")
        print("ФАЙЛ БЫЛ УДАЛЁН")
# Через библиотеку urllib получается изображение с сайта ФПЭТ
    urllib.request.urlretrieve(img_url, filename)
    time.sleep(900)