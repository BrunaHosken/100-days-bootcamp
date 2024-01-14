# Data entry job aplication
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
from time import sleep
from dotenv import load_dotenv
import requests

load_dotenv()

LINKS_DOCS_JOB_AUTOMATIZATION = os.getenv('LINKS_DOCS_JOB_AUTOMATIZATION')
USER_AGENT =  os.getenv('USER_AGENT')


url = "https://appbrewery.github.io/Zillow-Clone/"

headers={
    "User-Agent":USER_AGENT,
    "Accept-Language": "en-US,en;q=0.5",
    "sec-ch-ua-platform": "Linux",
    "Accept-Encoding": "gzip, deflate, br"
}

response = requests.get(url=url, headers=headers)
data = response.text

soup = BeautifulSoup(data, "html.parser")
all_link_elements = soup.select(".StyledPropertyCardDataWrapper a") 

all_link = [link["href"] for link in all_link_elements]
len_all_link = len(all_link)
print(all_link)

all_price_elements = soup.select(".PropertyCardWrapper span")
all_price = [price.get_text().replace("/mo","").split("+")[0] for price in all_price_elements]
print(all_price)

all_address_elements = soup.select(".StyledPropertyCardDataWrapper address")
all_address = [address.get_text().replace("|","").strip() for address in all_address_elements]
print(all_link)


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

for i in range(len_all_link):
    driver.get(LINKS_DOCS_JOB_AUTOMATIZATION)
    sleep(5)
    address = driver.find_element(by=By.XPATH, 
                        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input') 
    price = driver.find_element(by=By.XPATH, 
                        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input') 
    link = driver.find_element(by=By.XPATH, 
                        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit = driver.find_element(by=By.XPATH, 
                        value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    
    address.send_keys(all_address[i])
    price.send_keys(all_price[i])
    link.send_keys(all_link[i])

    submit.click()