import requests
import json
import win32com.client as wincom
import time

city = input("Enter the city \n")
url = "https://api.weatherapi.com/v1/current.json?key=c42cd94c2f784423915115532232104&q={city}"

r=requests.get(url)
print(r)
# we are using json module as we want output in dictinory format
wdic = json.loads(r.text)
print(wdic["current"]["temp_c"])



speak = wincom.Dispatch("SAPI.SpVoice")

text = "This text is read after 3 seconds"
speak.Speak(f"The Current Temperation in {city} is {wdic['current']['temp_c']} Celcius")
speak.Speak(f"According to wheather forcast today there will be {wdic['current']['condition']['text']} day in {city}")
