import requests


def get_crypto_prices():
    """Получить курсы крипты с Binance (с изменением за 24ч)"""
    url = "https://api.binance.com/api/v3/ticker/24hr"
    response = requests.get(url)
    return response.json()


def show_crypto():
    """Показать курсы крипты"""
    data = get_crypto_prices()
    coins = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "SOLUSDT", "XRPUSDT"]

    print("=" * 50)
    print("КУРСЫ КРИПТОВАЛЮТ (за 24 часа)")
    print("=" * 50)

    for item in data:
        if item["symbol"] in coins:
            symbol = item["symbol"].replace("USDT", "")
            price = float(item["lastPrice"])
            change = float(item["priceChangePercent"])

            if change > 0:
                arrow = "↑"
            elif change < 0:
                arrow = "↓"
            else:
                arrow = "="

            print(f"{symbol}: {price:.2f} $  {arrow} {change:+.2f}%")

    print("=" * 50)


def save_crypto():
    """Сохранить курсы в файл"""
    data = get_crypto_prices()
    coins = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "SOLUSDT", "XRPUSDT"]

    with open("crypto.txt", "a") as file:
        for item in data:
            if item["symbol"] in coins:
                symbol = item["symbol"].replace("USDT", "")
                price = float(item["lastPrice"])
                change = float(item["priceChangePercent"])
                file.write(f"{symbol}: {price:.2f} $ ({change:+.2f}%)  ")
        file.write("\n")

    print("Сохранено!")


def show_history():
    """Показать историю из файла"""
    try:
        with open("crypto.txt", "r") as file:
            content = file.read()
            if content:
                print("=" * 50)
                print("ИСТОРИЯ КУРСОВ КРИПТЫ")
                print("=" * 50)
                print(content)
            else:
                print("История пуста")
    except FileNotFoundError:
        print("Файл истории не найден")


# === МЕНЮ ===
while True:
    print()
    print("=== КРИПТОВАЛЮТЫ ===")
    print("1. Показать курсы")
    print("2. Сохранить в историю")
    print("3. Показать историю")
    print("4. Выход")
    choice = input("Что выбираешь? ")

    if choice == "1":
        show_crypto()
    elif choice == "2":
        save_crypto()
    elif choice == "3":
        show_history()
    elif choice == "4":
        print("Пока!")
        break
    else:
        print("Не понял, попробуй ещё")
