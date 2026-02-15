# задача 1
import random
name = "Алексей"
question = "Будет ли мне сопутствовать удача сегодня?"
answer = ""
answers = [
    "Да, безусловно.",
    "Это решительно так.",
    "Без сомнения.",
    "Ответ туманный, попробуйте еще раз.",
    "Спросите еще раз позже.",
    "Лучше не говорить вам сейчас.",
    "Мои источники говорят «нет».",
    "Прогноз не очень хороший.",
    "Очень сомнительно."
]
if question == "":
    print("Магический шар не может ответить, если вопрос не задан.")
else:
    answer = random.choice(answers)
    if name == "":
        print(f"Вопрос: {question}")
    else:
        print(f"{name} спрашивает: {question}")
    print(f"Магический шар отвечает: {answer}")
# задача 2
mean = 100
std_dev = 5
maximum = 120
minimum = 80

if maximum > mean + 5 * std_dev or minimum < mean - 5 * std_dev:
    print("В ваших данных имеются экстремальные значения и требуют предобработки")
elif maximum > mean + 3 * std_dev or minimum < mean - 3 * std_dev:
    print("В ваших данных имеются выбросы")
else:
    print("Ваши данные пригодны для анализа")

# задача 3
driver_age = int(input("Введите возраст водителя (например, 30): "))
experience = int(input("Введите стаж водителя (например, 5): "))
reputation = int(input("Введите репутацию водителя (например, 4): "))
traffic = int(input("Введите длительность пробок (например, 6): "))
trip_duration = int(input("Введите длительность поездки в минутах (например, 25): "))

tariff_table = [
    {"age": (20, 27), "exp": (2, 9), "rep": (1, 2), "traffic": (1, 3), "rate": 12.0},
    {"age": (20, 27), "exp": (2, 9), "rep": (1, 2), "traffic": (4, 7), "rate": 12.5},
    {"age": (20, 27), "exp": (2, 9), "rep": (3, 5), "traffic": (1, 3), "rate": 11.6},
    {"age": (20, 27), "exp": (2, 9), "rep": (3, 5), "traffic": (4, 7), "rate": 11.3},
    {"age": (27, 34), "exp": (2, 9), "rep": (1, 2), "traffic": (1, 3), "rate": 11.4},
    {"age": (27, 34), "exp": (2, 9), "rep": (3, 5), "traffic": (1, 3), "rate": 11.7},
    {"age": (27, 34), "exp": (2, 9), "rep": (3, 5), "traffic": (4, 7), "rate": 11.9},
    {"age": (27, 34), "exp": (10, 15), "rep": (1, 2), "traffic": (1, 3), "rate": 10.8},
    {"age": (27, 34), "exp": (10, 15), "rep": (3, 5), "traffic": (4, 7), "rate": 10.9},
    {"age": (27, 34), "exp": (10, 15), "rep": (1, 2), "traffic": (4, 7), "rate": 11.0},
]

selected_rate = None
for tariff in tariff_table:
    age_min, age_max = tariff["age"]
    exp_min, exp_max = tariff["exp"]
    rep_min, rep_max = tariff["rep"]
    traffic_min, traffic_max = tariff["traffic"]

    if (
            age_min <= driver_age <= age_max and
            exp_min <= experience <= exp_max and
            rep_min <= reputation <= rep_max and
            traffic_min <= traffic <= traffic_max
    ):
        selected_rate = tariff["rate"]
        break

if selected_rate is not None:
    price = selected_rate * trip_duration
    print(f"Стоимость вашей поездки составит {price:.2f}")
else:
    print("Не найден подходящий тариф для указанных параметров.")
# задача 4
purchase_amount = float(input("Введите сумму покупки: "))
if purchase_amount < 1000:
    discount = 0
elif 1000 <= purchase_amount <= 5000:
    discount = 0.05
else:
    discount = 0.10

final_price = purchase_amount * (1 - discount)

print(f"Итоговая цена с учетом скидки: {final_price:.2f} руб.")
# задача 5
use_butter = input("Хотите использовать сливочное масло вместо маргарина? (да/нет): ").lower() == "да"
use_vanilla = input("Хотите добавить ванильный экстракт? (да/нет): ").lower() == "да"

steps = [
    "1. Разогрейте духовку до 180°C.",
    "2. В большой миске смешайте муку, соду и соль.",
    f"3. В отдельной миске разотрите { 'сливочное масло' if use_butter else 'маргарин' } с сахаром.",
    "4. Добавьте яйца и хорошо перемешайте.",
    f"5. { 'Добавьте ванильный экстракт.' if use_vanilla else '' }",
    "6. Постепенно добавьте сухие ингредиенты к влажным.",
    "7. Добавьте шоколадную крошку.",
    "8. Выложите тесто на противень.",
    "9. Выпекайте 10-12 минут."
]

for step in steps:
    if step.strip():  # Пропускаем пустые строки
        print(step)
# задача 6
import random

col1 = ["Уважаемые", "Совершенно", "Друзья,", "Господа,", "Товарищи,", "Дамы и господа,", "Соседи,", "Коллеги,"]
col2 = ["коллеги,", "приятелей,", "все,", "товарищи,", "гости,", "слушатели,", "все присутствующие,", "все друзья,"]
col3 = ["призываю", "прошу", "настоятельно рекомендую", "советую", "прошу внимания", "напоминаю", "уверяю", "утверждаю"]
col4 = ["вас", "всех", "вас, коллег", "вас, друзей", "вас, уважаемые", "вас, слушатели", "вас, гости", "вас, присутствующие"]
col5 = ["к анализу", "к размышлению", "к обсуждению", "к действию", "к рассмотрению", "к изучению", "к обобщению", "к синтезу"]

idx1 = random.randint(0, 7)
idx2 = random.randint(0, 7)
idx3 = random.randint(0, 7)
idx4 = random.randint(0, 7)
idx5 = random.randint(0, 7)

phrase = f"{col1[idx1]} {col2[idx2]} {col3[idx3]} {col4[idx4]} {col5[idx5]}"
print(phrase)

