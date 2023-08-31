# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!

# вариант решения на входные данные от пользователя user_input
def minimum(arr):
    min_num = arr[0]
    for num in arr:
        if num < min_num:
            min_num = num
    return min_num

def maximum(arr):
    max_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num
    return max_num

user_input = input("Введите список целых чисел, разделенных запятыми: ")
numbers = [int(num) for num in user_input.split(",")]

print("Максимальное число:", maximum(numbers))
print("Минимальное число:", minimum(numbers))