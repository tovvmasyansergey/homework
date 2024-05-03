import requests
import json
import argparse

"""
This file is show weather of city
Create by: Sergey Tovmasyan
Date: 01.05.2024
"""


def get_arguments():
    """
    Function: get_arguments
    Brief: The functiom is return name of city and parametrs of weather
    Params: city:name of city,parametrs:parametr of weather
    Return: name of city and parametrs
    """

    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('-c', '--city', required=True, help="This is a input name of city")
        parser.add_argument('-p', '--parametr', default= "all",choices = ["temperature","humidity","max_temperature","cloud"], help="Please input parametre")
        args = parser.parse_args()
        name_city = args.city
        parametr = args.parametr
        return name_city,parametr
    except  argparse.ArgumentError as e:
        print(f"please input name city and parametr of weather {e}")
        return None,None



def get_url(city,parametre):
    """
    Function: get_url
    Brief: The function requests and get data of city
    Params: name of city and parametrs
    Return: return all information about weather of city
    """

    try:
        key = "32e6bc67af0fccc1b7c2ce889e0560a7"
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {"q" : city,"appid":key,"units":"metric"}
        response = requests.get(url,params = params)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print("city not found")
            return None
    except requests.exceptions.RequestsException as e:
        print(f"error in api requests:{e}")
        return None
    except json.JSONDecodeError as e:
        print(f"error in json file{e}")
        return None


def print_all(cnt,city):
    """
    Function: print_all
    Brief: The function print all deafault information
    Params: data of city and name of city
    Return: return 0
    """

    print("Temperatue of ",city,": " ,cnt['main']['temp'])
    print("cloudly of ",city,": ",cnt["weather"][0]['main'])
    print("humidity of ",city,": ",cnt['main']['humidity'])
    print("max temperature of ",city,": ",cnt['main']['temp_max'])


def print_parametr(cnt,param,city):
    """
    Function: print_parametr
    Brief: the function print pametr of weather of city
    Params: data of city,parametr of city,name of city
    Return:return 0
    """


    if param.lower() == "temperature":
        print("Temperatue of ",city,": " ,cnt['main']['temp'])
    elif param.lower() == "cloudly":
        print("cloudly of ",city,": ",cnt["weather"][0]['main'])
    elif param.lower() == "humidity":
        print("humidity of ",city,": ",cnt['main']['humidity'])
    elif param.lower() == "max_temperature":
        print("max temperature of ",city,": ",cnt['main']['temp_max'])
    else:
        print("param not found")
def main():
    city,param = get_arguments()
    if city is not None and param is not None:
        data = get_url(city,param)
        if data is not None:
            if param == 'all':
                print_all(data,city)
            else:
                print_parametr(data,param,city)

if __name__ == "__main__":
	main()
