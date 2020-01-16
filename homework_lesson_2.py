# Задачи на циклы и оператор условия------
# ----------------------------------------

'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
# i = 1
# while i < 6:
# print(str(i)+")", 0)
# i += 1
'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
# i = 0
# counter = 0
# while i < 10:
# number = input("Введите число: ")
# i += 1
# if number == "5":
# counter += 1
# print("Число 5 было введено {} раз".format(counter))

'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
# sum = 0
#
# for i in range(1,101):
#     sum+=i
# print(sum)

'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
# result = 1
# for i in range(1, 11):
# result *= i
# print(result)
'''
Задача 5
Вывести цифры числа на каждой строчке.
'''

# integer_number = 2129

# print(integer_number % 10, integer_number // 10)

# while integer_number > 0:
# print(integer_number % 10)
# integer_number = integer_number // 10

'''
Задача 6
Найти сумму цифр числа.
'''
# integer_number = 383792
# counter = 0
# while integer_number > 0:
# counter += integer_number % 10
# integer_number = integer_number // 10
# print(counter)
'''
Задача 7
Найти произведение цифр числа.
'''
# integer_number = 837329
# counter = 1
# while integer_number > 0:
# counter *= integer_number % 10
# integer_number = integer_number // 10
# print(counter)
'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
# integer_number = 213413
# while integer_number>0:
# if integer_number%10 == 5:
# print('Yes')
# break
# integer_number = integer_number//10
# else: print('No')

'''
Задача 9
Найти максимальную цифру в числе
'''
# integer_number = 8220944938
# max_number = 0
# for i in str(integer_number):
# if int(i) > max_number:
# max_number = int(i)
# print(max_number)
'''
Задача 10
Найти количество цифр 5 в числе
'''
# integer_number = 4300055553377365475
# counter = 0
# for i in str(integer_number):
# if int(i) == 5:
# counter += 1
# print(counter)
