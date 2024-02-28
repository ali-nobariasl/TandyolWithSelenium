
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup as bs
import requests

from accuount_info import  product_list , telegram_API ,telegram_chat_id

#todo email 


def telegramPriceTracer(mes:str):
    api = telegram_API
    requests.post(api, data={"chat_id":telegram_chat_id,
                            "text":mes}).json()
    
    
    
def pricing(producturl:str):
    product_page = requests.get(url)
    product_page_html = bs(product_page.content,"html.parser")
    price = product_page_html.find('span',class_='prc-dsc').getText()
    name = product_page_html.find('h1',class_='pr-new-br').getText()
    return f"product:{name} has this price: {price}"
    
    


while True:
    for i in range(2):
        url = product_list[i]
        telegramPriceTracer(pricing(url))
        time.sleep(5)





    
    
