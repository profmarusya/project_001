# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teachers создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:

import sqlite3

# Создание соединения с базой данных
connection = sqlite3.connect('teachers.db')
cursor = connection.cursor()

# Создание таблицы Schools - так как была ошибка
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Schools (
        School_Id INTEGER PRIMARY KEY,
        School_Name TEXT
    )
''')

# Наполнение таблицы данными
schools_data = [
    (1, 'Школа 1'),
    (2, 'Школа 2'),
    (3, 'Школа 3'),
    (4, 'Школа 4')
]


# Создание таблицы Students
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Students (
        Student_Id INTEGER PRIMARY KEY,
        Student_Name TEXT,
        School_Id INTEGER,
        FOREIGN KEY (School_Id) REFERENCES Schools(School_Id)
    )
''')

# Наполнение таблицы данными
students_data = [
    (201, 'Иван', 1),
    (202, 'Петр', 2),
    (203, 'Анастасия', 3),
    (204, 'Игорь', 4)
]


# Сохранение изменений и закрытие соединения
connection.commit()
connection.close()

# Создание соединения с базой данных
connection = sqlite3.connect('teachers.db')
cursor = connection.cursor()

# Ввод ID студента
student_id = int(input("Введите ID студента: "))

# Получение информации о студенте и школе по ID студента
cursor.execute('''
    SELECT Students.Student_Id, Students.Student_Name, Students.School_Id, Schools.School_Name
    FROM Students
    JOIN Schools ON Students.School_Id = Schools.School_Id
    WHERE Students.Student_Id = ?
''', (student_id,))

result = cursor.fetchone()

# Вывод информации
if result:
    student_id, student_name, school_id, school_name = result
    print("ID Студента:", student_id)
    print("Имя студента:", student_name)
    print("ID школы:", school_id)
    print("Название школы:", school_name)
else:
    print("Студент с таким ID не найден.")

# Закрытие соединения
connection.close()