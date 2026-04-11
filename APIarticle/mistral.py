import requests
import json
from datetime import datetime, timedelta


NEWS_API_KEY = "d71e0c92715d481581ba0e4a4344b2c1"
MISTRAL_API_KEY = "ZbqJhMWw3vg7qvvhfvYTh8hJDLRaMkRH"

TOPIC = "artificial intelligence ethics OR AI regulation OR AI safety" #эт тема
DAYS_BACK = 1
MAX_ARTICLES = 10



# 1. ПОЛУЧ СТАТЕЙ
def fetch_articles():
    url = "https://newsapi.org/v2/everything"
    #пр запр к апи
    params = {
        "q": "technology OR AI OR software", #поиск
        "language": "en",
        "sortBy": "relevancy",
        "pageSize": MAX_ARTICLES, #скок вернуть
        "apiKey": NEWS_API_KEY
    }

    response = requests.get(url, params=params)
    #преобраз в յսօն
    data = response.json()

    print("DEBUG RESPONSE:", data)

    return data.get("articles", [])





# 2. АНАЛИЗ ЧЕРЕЗ MISTRAL
def generate_summary(articles):
    url = "https://api.mistral.ai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json"
    }
    #заголовки итд
    articles_text = "\n\n".join([
        f"{a.get('title', '')}. {a.get('description', '')}"
        for a in articles
    ])

    prompt = f"""
Ты аналитик новостей.
Напиши аналитическую аннотацию на русском языке по следующим статьям.

Требования:
- 250–300 слов
- без списков
- аналитический стиль
- оцени, что произошло за последние сутки

Статьи:
{articles_text}
"""

    data = {
        "model": "mistral-small-latest",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    result = response.json()

    return result["choices"][0]["message"]["content"]



# 3. ЗАПУСК ПРОГИ

def main():
    print("Получаем статьи...")

    articles = fetch_articles()

    if not articles:
        print("Нет статей")
        return

    print("Статей найдено:", len(articles))

    print("Отправляем в Mistral...")

    summary = generate_summary(articles)

    print("\n===== АННОТАЦИЯ =====\n")
    print(summary)

    with open("text.txt", "w", encoding="utf-8") as f:
        f.write(summary)

    print("\nГотово: текст сохранён в text.txt")


if __name__ == "__main__":
    main()




