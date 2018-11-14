
__author__ = 'Ханаев Валентин'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

# код пишем тут...
input_number = int(input('введите число: '))
if input_number:
    while input_number>0:
        digit = input_number%10
        print(digit)
        input_number = input_number//10
else:
    print('0')

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную 
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

first_variable = input('введите значение первой переменной: ')
second_variable = input('введите значение второй переменной: ')
tmp_variable = first_variable
first_variable = second_variable
second_variable = tmp_variable
print('новое значение первой переменной: ', first_variable)
print('новое значение второй переменной: ', second_variable)

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

user_age = int(input('введите свой возраст: '))
if user_age>=18:
    print('Доступ разрешен')
else:
    print('Извините, пользование данным ресурсом только с 18 лет')