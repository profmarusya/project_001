import sqlite3

# Создание соединения с базой данных
connection = sqlite3.connect('teatchers.db')
cursor = connection.cursor()


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