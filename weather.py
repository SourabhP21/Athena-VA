import requests


def executeWeatherFn():
    complete_url = "http://api.openweathermap.org/data/2.5/weather?q=bhopal&units=metric&appid="
      
    response = requests.get(complete_url)
    x = response.json() 

    if (x["cod"]!="404"):
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        outst="The Temperature is " +str(current_temperature)+" degree celsius "+" with "+str(weather_description)
        return outst