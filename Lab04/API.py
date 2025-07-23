import requests
from datetime import datetime, timedelta


class OpenWeatherMap:
    def __init__(self):
        self.__API_KEY = "97ec21b1167131032e51009f91dfae8b"

    def getcurrenttemperature(self, city):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.__API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        return data["main"]["temp"]

    def get_lat_and_long(self, city):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.__API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        return data["coord"]["lat"], data["coord"]["lon"]

    def getTwo(self, city):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.__API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        return data["main"]["temp"], data["coord"]["lat"], data["coord"]["lon"]

    def get_temperature_after(self, city, days, hour=None):
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={self.__API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        target_date = datetime.now() + timedelta(days=days)
        if hour is None:
            hour = 12

        target_str = target_date.replace(
            hour=hour, minute=0, second=0, microsecond=0
        ).strftime("%Y-%m-%d %H:00:00")

        for item in data["list"]:
            if item["dt_txt"] == target_str:
                temp = item["main"]["temp"]
                print(f"Expected temperature in {city} at {target_str}: {temp}°C")
                return temp

        print("No forecast found for the specified time.")
        return None


def main():
    weather = OpenWeatherMap()
    city = input("Enter city name: ")

    print("\n--- Current Weather ---")
    try:
        temp = weather.getcurrenttemperature(city)
        print(f"Current temperature in {city}: {temp}°C")
    except:
        print("Couldn't fetch current temperature.")

    print("\n--- Coordinates ---")
    try:
        lat, lon = weather.get_lat_and_long(city)
        print(f"{city} is located at: Latitude = {lat}, Longitude = {lon}")
    except:
        print("Couldn't fetch coordinates.")

    print("\n--- Future Temperature ---")
    try:
        days = int(input("Enter number of days into the next forecast (max 5): "))
        hour = int(input("Enter hour (0-23): "))
        temp_future = weather.get_temperature_after(city, days, hour)
        if temp_future:
            print(f"Forecasted temperature: {temp_future}°C")
    except:
        print("Couldn't fetch future temperature.")


if __name__ == "__main__":
    main()
