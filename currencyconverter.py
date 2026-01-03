RATES = {
    "EUR": 0.025,
    "USD": 0.027
}

print("BiTaєMO У Конвертері Валют (UAH -> EUR/USD)!")

try:
    uah_ammount_str = input("Введи суму в гривнях (UAH): ")
    uah_ammount = float(uah_ammount_str)

    if uah_ammount < 0:
        raise ValueError("Сума не може бути від' ємною!")
    
    currency = input("Вибери валюту для конвертації (EUR/USD): "). upper()

    rate = RATES[currency]
    converted_amount = uah_ammount * rate

    print(f"{uah_ammount} гривень - це {converted_amount:.2f} {currency}")

except ValueError as e:
    print(f"X Помилка вводу суми! Будь ласка, перевір, чи ти ввів коректне число. Деталі: {e}")

except KeyError:
    print(f" Помилка вибору валюти! Валюта ** {currency} ** не підтримується. Виберіть EUR або USD.")