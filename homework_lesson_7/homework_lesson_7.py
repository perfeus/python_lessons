import datetime
import time
import timeit
from datetime import timedelta

from docxtpl import DocxTemplate
import random
import csv
import json


def get_context(brand, model, year, fuel, miles, color, gear, engine,
                date=str(datetime.datetime.now().date())):
    return {
        "Brand": brand,
        "Model": model,
        "Year": year,
        "Fuel_consumption": fuel,
        "Mileage": miles,
        "Color": color,
        "Gearbox": gear,
        "Engine": engine,
        "Date": date
    }


def from_template(brand, model, year, fuel, miles, color, gear, engine, template):
    template = DocxTemplate(template)
    context = get_context(brand, model, year, fuel, miles, color, gear, engine)

    template.render(context)

    template.save(brand + "_" + model + "_" + year + "_" +
                  str(datetime.datetime.now().date()) + "_report.docx")


def generate_report(brand, model, year, fuel, miles, color, gear, engine):
    template = "report.docx"
    document = from_template(brand, model, year, fuel, miles, color, gear, engine, template)


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


generate_report("Lada", "Kalina", "2010", "8.1", "83737", "white", "manual", "1500")

#задание 4 и 5, для начала сгенерируем случайные данные автомобилей

car_data = [["brand", "color", "year", "price"]]
choices_set = [["mercedes", "toyota", "bmw", "mazda", "kia", "ford", "mustang"],
               ["black", "white", "yellow", "grey", "blue", "green"],
               [1983, 2008, 2001, 1999, 2018, 2003, 1989, 1993, 2000],
               [29937, 10293, 2883, 5833, 2398, 23399, 11192, 38563]]

for i in range(100):
    add = []
    for item in choices_set:
        add.append(random.choice(item))
    car_data.append(add)

with open("example.csv", "w") as f:
   writer = csv.writer(f)
   writer.writerows(car_data)
print("writing completed!")

#генерируем случайные данные для создания json-файла
characters = ["brand", "color", "year", "price"]
json_list = []

for i in range(100):
    car_dic = {}
    for num in range(4):
        car_dic[characters[num]] = random.choice(choices_set[num])
    json_list.append(car_dic)

with open("dict_to_json.txt", "w") as f:
    json.dump(json_list, f)
