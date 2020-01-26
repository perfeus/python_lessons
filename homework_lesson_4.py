import random
import collections

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
    print(names_length)


def most_common_name(x, y):
    """
    функция выводит самое частое имя из списка на выходе
    :param a: список имен;
    :return: самое частое имя;
    """
    random_list = []
    for i in range(y):
        random_list.append(random.choice(x))
    c = collections.Counter(random_list)
    for i in c.most_common(1):
        print(f"the most common name is {i[0]}")


def rarest_letter(x, y):
    """
    функция выводит самую редкую букву, с которой
    начинаются имена в списке на выходе
    :param x: список имен;
    :param y: количество случайных имен из списка x;
    :return: самая редкая буква;
    """
    random_list = []
    for i in range(y):
        random_list.append(random.choice(x))
    letters = [i[0] for i in random_list]
    c = collections.Counter(letters)
    for i in c.most_common():
        res = i[0]
    print(f"the most common name is {res[0]}")


# в файле с логами найти дату самого позднего лога (по метке времени):

with open("log.txt", encoding="utf-8") as f:
    elements_list = [i.split(",")[0] for i in f]
print(max(elements_list))
