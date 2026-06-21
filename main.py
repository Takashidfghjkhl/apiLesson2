import argparse
import requests
import os
from dotenv import load_dotenv

def get_exchange_rates(base_currency, apikey):
    url = f"https://v6.exchangerate-api.com/v6/{apikey}/latest/{base_currency.upper()}"
    response = requests.get(url)
    response.raise_for_status()
    exchange_rates = response.json()["conversion_rates"]
    return exchange_rates

def convert_amount(amount, target_currency, exchange_rates):
    target_rate = exchange_rates[target_currency.upper()]
    print(f"Курс целевой валюты: {target_rate}")
    print(f"Сконвертированная сумма: {target_rate * amount}{target_currency}")

def main():
    load_dotenv()
    apikey = os.getenv("APIKEY")
    parser = argparse.ArgumentParser(description="Описание что делает программа")
    parser.add_argument("--base", type=str, help="Введите код базовой валюты", default="RUB")
    parser.add_argument("--target", type=str, help="Введите код целевой валюты", default="EUR")
    parser.add_argument("--amount", type=float, help="Введите сумму", default=12000)
    args = parser.parse_args()
    try:
        exchange_rates = get_exchange_rates(args.base, apikey)
        convert_amount(args.amount, args.target, exchange_rates)
    
    except requests.exceptions.HTTPError as error:
        print("проверьте правильность кода вводимой вами валюты")
        print(f"код ошибки {error}")
if __name__ == "main":
    main()