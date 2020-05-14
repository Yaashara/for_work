import requests 
import lxml
from bs4 import BeautifulSoup
from datetime import datetime

today = datetime.today()
today = today.strftime("%d/%m/%Y")
url = "https://www.cbr.ru/scripts/XML_daily.asp?"
payload = {"date_req":today}

responce = requests.get(url, params = payload)

xml = BeautifulSoup(responce.content, "lxml")

def getCourse(id):
    return xml.find("valute", {'id': id}).value.text

