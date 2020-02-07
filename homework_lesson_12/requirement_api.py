import requests
import pprint
import collections


def requirements(position):
    # делаем первоначальный запрос для определения количеста вакансий
    # и количества страниц (переменные vacancies, pages)
    URL = "https://api.hh.ru/vacancies"
    params = {
        "text": position.title(),
        "page": 1,
        "per_page": 20
    }
    result = requests.get(URL, params=params).json()
    vacancies = result["found"]
    pages = result["pages"]
    print(f"There have been found {vacancies} on {pages} pages.")
    list_requirements = []
    # pprint.pprint(result["items"])

    # испльзуем цикл, чтобы пройти по каждой странице и извлечь трубования
    # к выбранной должности
    for page in range(1, pages):
        URL = "https://api.hh.ru/vacancies"
        query_par = {
            "text": position.title(),
            "page": page,
            "per_page": 20
        }
        query = requests.get(URL, params=query_par).json()
        search = query["items"]
        for item in search:
            requirement = item["snippet"]
            try:
                line = requirement["requirement"].replace(",", " ").replace("—", " ").replace(".", " ")\
                          .replace("«", " ").replace("-", " ").replace("»", " ")\
                          .replace("(", " ").replace(")", " ").replace("!", " ")\
                          .replace("?", " ").replace(";", " ").replace(":", " ")
                list_requirements += line.split()
            except Exception:
                print(requirement["requirement"])
    return list_requirements


result = requirements("риэлтор")

# исключаем из списка слова для связи и выводим 20, часто встечающихся слов
words = dict()
conjunctions = {"на", "не", "под", "у", "в", "с", "перед", "до", "о", "по", "из-за", "от", "для",
                "из-под", "над", "без", "близ", "ввиду", "между", "возле", "рядом", "около",
                "отношении", "вокруг", "впереди", "в продожение", "вследствие", "течение",
                "из", "кроме", "от", "подле", "по мере", "после", "прежде", "против",
                "благодаря", "вопреки", "к", "согласно", "соответсвенно", "несмотря",
                "про", "сквозь", "через", "во", "за", "об", "обо", "в", "соответствии",
                "надо", "перед", "согласно", "связи", "при", "без", "до", "для", "из",
                "под", "пред", "при", "ввиду", "насчет", "помощи", "случае", "условии",
                "погодя", "спустя", "благодаря", "начиная", "несмотря", "считая", "после",
                "мимо", "внутри", "вдоль", "вдали", "вокруг", "и", "или", "без", "можно"}
for i in result:
    if i.lower() in conjunctions:
        result.remove(i)
print(len(result))
print(result)
c = collections.Counter(result)
for key, value in c.items():
    words[key] = value

print(c.most_common(100))

