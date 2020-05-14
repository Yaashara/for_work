
import requests
import lxml
from bs4 import BeautifulSoup

def getWeather():

    url = "https://yandex.ru/pogoda/moscow"
    response = requests.get(url)

    html = BeautifulSoup(response.content, "lxml")

    return html.find("span", {'class': 'temp__value'}).text 



if __name__ == "__main__":
    print(getWeather())
