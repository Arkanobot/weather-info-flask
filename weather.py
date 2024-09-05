from dotenv import load_dotenv
from pprint import pprint
import requests
import os

# loading the env
load_dotenv()


# function to get the current weather data from the open weather map api
# requires API Key to be in the .env file with name WEATHER_API_KEY
# API key can be obtained from https://home.openweathermap.org/users/sign_up
# Once the signup is done it will be in the user settings called your api keys
# Returns data in JSON format which is returned or printed if the file is called directly
def get_current_weather(city="Bangalore"):
    # request url for getting the current weather of the given city in params and the api key from .env file
    requests_url = f"http://api.openweathermap.org/data/2.5/weather?appid={os.getenv('WEATHER_API_KEY')}&q={city}&units=metric"

    # get the data from the url
    weather_data = requests.get(requests_url).json()

    # return the data
    return weather_data


if __name__ == "__main__":
    # if the file is being run directly
    print("\n*** Get Current Weather Conditions ***\n")

    # get input from the user
    city = input("\nPlease enter a city name: ")

    # check for empty strings or strings with spaces
    if not bool(city.strip()):
        city = "Bangalore"

    # get weather data
    weather_data = get_current_weather(city)

    # print weather data
    print("\n")
    pprint(weather_data)
