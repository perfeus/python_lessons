from functools import reduce


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
        print(f"{x} is a simple number")
    else:
        print(f"{x} is not a simple number")


def divisors_list(x):
    """
    данная функция выводит список всех делителей числа "х"
    :param x: число от 1 до 1000
    :return: выводить все делители в качестве списка
    """
    divisors = []
    for i in range(1, x + 1):
        if x % i == 0:
            divisors.append(i)
    print(divisors)


def max_simple_divisor(x):
    """
    данная функция выводит наибольший простой делитель числа "х"
    :param x: число от 1 до 1000
    :return: число которое является наибоьших простым делителем числа "х"
    """
    divisors = []
    simple_divisors = []
    for i in range(1, x + 1):
        if x % i == 0:
            divisors.append(i)
    print(f"All divisors list of the number {x} is {divisors}")
    for element in divisors:
        counter = 0
        for i in range(1, element + 1):
            if element % i == 0:
                counter += 1
        if counter == 2:
            simple_divisors.append(element)
    print(f"The list of simple divisors is {simple_divisors}")


def max_divisor(x):
    """
    функция опрделяет наибольший делитель числа "х"
    :param x: число от 1 до 1000
    :return: возращает наибольший делитель
    """
    divisors = []
    for i in range(1, x + 1):
        if x % i == 0:
            divisors.append(i)
    print(f"All divisors list of the number {x} is {divisors}")
    great_divisor = reduce(lambda a, b: a if a > b else b, divisors)
    print(f"The greatest divisor of the number {x} is {great_divisor}")


# здесь код решения задачи по каноническому разложению числа
def simple(x):
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


def primfacs(n):
    """
    данная функция производит каноническое разложение числа
    на простые множители
    :param n: число от 1 до 1000
    :return: выводит список простых множителей
    """
    if simple(n):
        print(f"{n} is a simple, try another number")
        return None
    else:
        i = 2
        primfac = []
        while i * i <= n:
            while n % i == 0:
                primfac.append(i)
                n = n / i
            i = i + 1
        if n > 1:
            primfac.append(int(n))
        return primfac
