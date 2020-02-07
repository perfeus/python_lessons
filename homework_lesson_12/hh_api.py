import requests
import pprint
# делаем первоначальный запрос для определения количеста вакансий
# и количества страниц (переменные vacancies, pages)
URL = "https://api.hh.ru/vacancies"
params = {
    "text": "Python",
    "page": 1,
    "per_page": 20
}
result = requests.get(URL, params=params).json()
vacancies = result["found"]
pages = result["pages"]
print(f"There have been found {vacancies} on {pages} pages.")
salary_from = []
salary_to = []
pprint.pprint(result["items"])

# испльзуем цикл, чтобы пройти по каждой странице
for page in range(1, pages):
    URL = "https://api.hh.ru/vacancies"
    query_par = {
        "text": "Python",
        "page": page,
        "per_page": 20
    }
    query = requests.get(URL, params=query_par).json()
    search = query["items"]
    for item in search:
        currency = item["salary"]
        if item["salary"] is not None and currency["currency"] == "RUR":
            line = item["salary"]
            if line["from"] is not None:
                salary_from.append(line["from"])
            elif line["to"] is not None:
                salary_to.append(line["to"])

min_salary_from = min(salary_from)
max_salary_from = max(salary_from)
middle_salary_from = int(sum(salary_from) / len(salary_from))
min_salary_to = min(salary_to)
max_salary_to = max(salary_to)
middle_salary_to = int(sum(salary_to) / len(salary_to))

print(f"Минимальная начальная зарплата: {min_salary_from}\n"
      f"Максимальная начальная зарплата: {max_salary_from}\n"
      f"Средняя начальная зарплата: {middle_salary_from}\n"
      f"Минимальная конечная зарплата: {min_salary_to}\n"
      f"Максимальная конечная зарплата: {max_salary_to}\n"
      f"Средняя конечная зарплата: {middle_salary_to}")


