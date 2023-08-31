# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 

# Выполнение заданий:
# Пункт A
import random

# Выбираем три случайные песни из списка
random_songs = random.sample(my_favorite_songs, 3)

# Считаем общую длительность трех песен
total_duration = sum(song[1] for song in random_songs)

# Выводим результат
print("Три песни звучат", total_duration, "минут")


# Пункт B
import random

# Выбираем три случайные песни из словаря
random_songs = random.sample(list(my_favorite_songs_dict.items()), 3)

# Считаем общую длительность трех песен
total_duration = sum(song[1] for song in random_songs)

# Выводим результат
print("Три песни звучат", total_duration, "минут")


# Пункт C
import random
import datetime

# Генерируем случайную песню
random_song = ['Random Song', round(random.uniform(2, 6), 2)]

# Выводим результат
print(random_song)


# Пункт D
import datetime

# Преобразуем минуты и секунды в формат времени
duration = datetime.timedelta(minutes=random_song[1])

# Выводим результат
print(duration)