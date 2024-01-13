#Automating job aplications

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time
from dotenv import load_dotenv
from selenium.common.exceptions import NoSuchElementException

load_dotenv()

EMAIL_LINKEDIN = os.getenv('EMAIL_LINKEDIN')
PASSWORD_LINKEDIN = os.getenv('PASSWORD_LINKEDIN')
PHONE_LINKEDIN = "999999999"

def abort():
    print("closing....")
    close = driver.find_element(By.CLASS_NAME, value="artdeco-modal__dismiss")
    close.click()
    time.sleep(2)
    print("discarting....")
    discard=driver.find_elements(By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard.click()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3796191370&f_AL=true&f_WT=3&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&origin=JOB_SEARCH_PAGE_JOB_FILTER&sortBy=R")

time.sleep(2)
sign_in = driver.find_element(By.LINK_TEXT, value="Sign in")
sign_in.click()

time.sleep(5)
email = driver.find_element(By.ID, value="username")
email.send_keys(EMAIL_LINKEDIN)
password = driver.find_element(By.ID, value="password")
password.send_keys(PASSWORD_LINKEDIN,Keys.ENTER)

time.sleep(5)
all_jobs = driver.find_elements(By.CLASS_NAME, value ="jobs-search-results__list-item")

for job in all_jobs:
    time.sleep(5)
    print("Opening Listing")
    print(job)
    job.click()
    time.sleep(2)
    try:
        apply= driver.find_element(By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply.click()

        time.sleep(5)
        phone= driver.find_element(By.CSS_SELECTOR, value="input[id*=phoneNumber]")

        if phone.text=="":
            phone.send_keys(PHONE_LINKEDIN)

        submit = driver.find_element(By.CSS_SELECTOR, value="footer button")

        if submit.get_attribute("data-control-name")=="continue_unify":
            time.sleep(2)
            abort()
            print("Complex, skipped")
            continue
        else:
            print("Submiting....")
            submit.click()

        print("saving...")  
        time.sleep(2)
        save_button = driver.find_element(by=By.XPATH, value="/html/body/div[3]/div[2]/div/div[3]/button[2]/span")
        save_button.click()
        print("exiting...")  
        time.sleep(2)
        close = driver.find_element(By.CLASS_NAME, value="artdeco-modal__dismiss")
        close.click()

    except NoSuchElementException:
        time.sleep(2)
        abort()
        print("No application button, skipped")
        continue

time.sleep(5)
driver.quit()