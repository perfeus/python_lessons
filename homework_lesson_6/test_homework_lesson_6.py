from functools import reduce
import random


def simple_num(x):
    """
    данная функция определяе является ли число "х" простым
    :param x: число от 1 до 1000
    :return: выводит ответ является ли оно простым или нет
    """
    counter = 0
    for i in range(1, x + 1):
        if x % i == 0:
            counter += 1
    if counter == 2:
        return True
    else:
        return False


def test_simple_num_1():
    assert simple_num(29) is True


def test_simple_num_2():
    assert simple_num(28) is False


def test_simple_num_3():
    assert simple_num(11) is False


def test_simple_num_4():
    assert simple_num(8) is True


def max_divisor(x):
    """
    функция опрделяет наибольший делитель числа "х"
    :param x: число от 1 до 1000
    :return: возращает наибольший делитель
    """
    divisors = []
    for i in range(1, x):
        if x % i == 0:
            divisors.append(i)
    return reduce(lambda a, b: a if a > b else b, divisors)


def test_max_divisor_5():
    assert max_divisor(100) == 50


def test_max_divisor_6():
    assert max_divisor(20) == 15


def test_max_divisor_7():
    assert max_divisor(50) == 45


def test_max_divisor_8():
    assert max_divisor(140) == 70


# тесты к грязной функции
names = ["alex", "mary", "john", "mike", "siri",
         "alice", "james", "michael", "william",
         "david", "richard", "charles", "joseph",
         "thomas", "mary", "christopher", "daniel", "paul",
         "mark", "donald", "george", "kenneth"]


def length_of_names(x, y):
    """
    функция генерирует случайный список из списка на
    входе и выводит другой список с длинной элементов
    случайного списка
    :param x: список имен;
    :param y: количество случайных имен из списка х;
    :return: список случайных имен, полученный из
    списка "х", длинной "у";
    """
    names_length = []
    for i in range(y):
        names_length.append(len(random.choice(x)))
    return names_length


def test_length_of_names_9():
    assert len(length_of_names(names, 5)) == 5


def test_length_of_names_10():
    assert type(length_of_names(names, 10)) is int
