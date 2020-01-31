import time
import random
import json
import sys
import psutil
import os


# задание №1

def show_time(f):
    """
    декоратор, замеряющий время исполнения декорируемой функции
    :param f:
    :return: возвращает обертку
    """

    def wrapper():
        start_time = time.time()
        f()
        end_time = time.time()
        print(end_time - start_time)

    return wrapper


@show_time
def random_json():
    """
    функция создает json-файл с произвольным набором данных
    """
    choices_set = [["mercedes", "toyota", "bmw", "mazda", "kia", "ford", "mustang"],
                   ["black", "white", "yellow", "grey", "blue", "green"],
                   [1983, 2008, 2001, 1999, 2018, 2003, 1989, 1993, 2000],
                   [29937, 10293, 2883, 5833, 2398, 23399, 11192, 38563]]
    characters = ["brand", "color", "year", "price"]
    json_list = []
    for i in range(100):
        car_dic = {}
        for num in range(4):
            car_dic[characters[num]] = random.choice(choices_set[num])
        json_list.append(car_dic)

    with open("dict_to_json.txt", "w") as f:
        json.dump(json_list, f)
    print("writing completed!")


# задание №2

@show_time
def sample_gen():
    sample = (x for x in range(1000000))
    print("Completed!")


@show_time
def sample_list():
    sample = [x for x in range(1000000)]
    print("Completed!")


# задание №3

def show_memory(f):
    """
    декоратор, замерающий объем оперативной памяти, потребляемой
    декорируемой функцией
    :param f:
    :return: возвращает обертку
    """

    def wrapper():
        sample = psutil.Process(os.getpid())
        start_memory = sample.memory_info().rss / 1000000
        f()
        end_memory = sample.memory_info().rss / 1000000
        print("Использовано памяти:", end_memory - start_memory)

    return wrapper


# задание №4
@show_memory
def memory_gen():
    for i in range(1000000):
        yield i
    print("Completed!")


@show_memory
def memory_list():
    [x for x in range(1000000)]
    print("Completed!")


memory_gen()
memory_list()
