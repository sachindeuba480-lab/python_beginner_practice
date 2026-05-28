import requests

city = input("Enter city name: ")

url = f"https://wttr.in/{city}?format=3"

response = requests.get(url)

print("\nWeather Report:")
print(response.text)