import requests
import argparse
import json
import time

"""
This file is about cripto with https,requests
Create by: Sergey Tovmasyan
Date: 02 may 2024
"""


def get_arguments():

    """
    Function: get_arguments
    Brief: The functions return filter by name or by value
    Params: name: name of the crypto valute or value by filter
    Return: return name ,value
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filter_name', default=None, help="Имя криптовалюты для фильтрации")
    parser.add_argument('-v', '--value_filter', default=None, type=float, help="Минимальная цена для фильтрации")
    args = parser.parse_args()
    name = args.filter_name
    value = args.value_filter
    return name,value

def get_crypto_data():

    """
    Function: get_crypto_data
    Brief: The function request url and get all data about crypto
    Params: 
    Return: returns the list of crypto data
    """

    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd","price_change_percentage":"24h"
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data

def filter_data(data, filter_name=None, value_filter=None):

    """
    Function: filter_data
    Brief: The functions is filtered by name or value
    Params: data of crypto,name,value
    Return: return list of crypto by filtered
    """

    filter_list = []
    for line in data:
        flag = True
        if filter_name and filter_name.lower() not in line['name'].lower():
            flag = False
        if value_filter and line['current_price'] < value_filter:
            flag = False
        if flag:
            filter_list.append({
                'name': line['name'],
                'symbol': line['symbol'],
                'current_price': line['current_price'],
                'market_cap': line['market_cap'],
                'total_volume': line['total_volume'],
                'price_change_24h': line['price_change_24h']
            })
    return filter_list

def main():
    """
    Function: main
    """
    name,value = get_arguments()
    while True:
        cnt = get_crypto_data()
        if name is None and value is None:
            print("Please input parametrs for filters")
            return
        filtered_coins = filter_data(cnt, name, value)
        if filtered_coins != []:
            for coin in filtered_coins:
                print(f"Name: {coin['name']}")
                print(f"Symbol: {coin['symbol']}")
                print(f"Current_price: {coin['current_price']}")
                print(f"Market_cap: {coin['market_cap']}")
                print(f"Total_volume: {coin['total_volume']}")
                print(f"Price_change_24h: {coin['price_change_24h']}")
                print("--------------------")
        else:
            print("No data by your filters")
        time.sleep(5)

if __name__ == "__main__":
    main()
