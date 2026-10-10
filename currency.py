import requests


def get_rates():
    """Получить курсы с ЦБ РФ"""
    url = "https://www.cbr-xml-daily.ru/daily_json.js"
    response = requests.get(url)
    return response.json()


def show_rates():
    """Показать основные курсы валют"""
    data = get_rates()
    date = data["Date"][:10]

    print("=" * 30)
    print(f"КУРСЫ ВАЛЮТ НА {date}")
    print("=" * 30)

    for code in ["USD", "EUR", "CNY"]:
        valute = data["Valute"][code]
        name = valute["Name"]
        curr = valute["Value"]
        prev = valute["Previous"]

        if curr > prev:
            arrow = "↑"
        elif curr < prev:
            arrow = "↓"
        else:
            arrow = "="

        print(f"{name}: {curr:.2f} ₽ {arrow}")

    print("=" * 30)


def show_all_rates():
    """Показать ВСЕ валюты"""
    data = get_rates()
    date = data["Date"][:10]

    print("=" * 40)
    print(f"ВСЕ ВАЛЮТЫ НА {date}")
    print("=" * 40)

    for code, valute in data["Valute"].items():
        name = valute["Name"]
        curr = valute["Value"]
        print(f"{code} — {name}: {curr:.2f} ₽")

    print("=" * 40)


def save_rates():
    """Сохранить курсы в файл"""
    data = get_rates()
    date = data["Date"][:10]

    with open("currency.txt", "a") as file:
        file.write(f"{date}: Доллар {data['Valute']['USD']['Value']:.2f}, ")
        file.write(f"Евро {data['Valute']['EUR']['Value']:.2f}, ")
        file.write(f"Юань {data['Valute']['CNY']['Value']:.2f}\n")


def show_history():
    """Показать историю из файла"""
    try:
        with open("currency.txt", "r") as file:
            content = file.read()
            if content:
                print("=" * 30)
                print("ИСТОРИЯ КУРСОВ")
                print("=" * 30)
                print(content)
            else:
                print("История пуста")
    except FileNotFoundError:
        print("Файл истории не найден")


# === МЕНЮ ===
while True:
    print()
    print("=== КУРСЫ ВАЛЮТ ===")
    print("1. Показать курсы")
    print("2. Сохранить в историю")
    print("3. Показать историю")
    print("4. Все валюты")
    print("5. Выход")
    choice = input("Что выбираешь? ")

    if choice == "1":
        show_rates()
    elif choice == "2":
        save_rates()
        print("Сохранено!")
    elif choice == "3":
        show_history()
    elif choice == "4":
        show_all_rates()
    elif choice == "5":
        print("Пока!")
        break
    else:
        print("Не понял, попробуй ещё")

