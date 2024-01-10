# Automated clicker game bot

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie= driver.find_element(By.CSS_SELECTOR, value="#cookie")
store= driver.find_elements(By.CSS_SELECTOR, value="#store div")

store_ids = [item.get_attribute("id") for item in store]

time_store=time.time()+5
time_out = time.time()+60*60

while True:
    cookie.click()

    if time.time()>time_store:
        prices = driver.find_elements(By.CSS_SELECTOR, value="#store b")
        itens_price = [ int(cost.text.split("-")[1].strip().replace(",", "")) for cost in prices if(cost.text!= "")]
    
        upgrades = {}

        for n in range(len(itens_price)):
            upgrades[itens_price[n]] = store_ids[n]
        

        actual_money = driver.find_element(By.ID, value="money").text
        cookie_money = int(actual_money.replace(",",""))
        
        
        possibles_upgrades = {}
        for cost,id in upgrades.items():
            if cookie_money > cost:
                possibles_upgrades[cost] = id

            print(len(possibles_upgrades))
        if(len(possibles_upgrades) > 0):
            highest_price= max(possibles_upgrades)
            to_buy = possibles_upgrades[highest_price]

            driver.find_element(By.ID, value=to_buy).click()

        time_store=time.time() + 5

    if time.time()>time_out:
        per_s = driver.find_element(By.ID, value="cps").text
        print(per_s + " per sec")
        break




