# Automated Tinder Swiping Bot

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from time import sleep
from dotenv import load_dotenv
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

load_dotenv()

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)
chrome_options.add_experimental_option("detach", True)

EMAIL = os.getenv('EMAIL')
PASSWORD_TWITTER = os.getenv('PASSWORD_TWITTER')
PROMISED_DOWN = 15
PROMISED_UP = 5


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = driver
        self.up = 0
        self.down = 0
    
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        sleep(10)
        go_button = self.driver.find_element(By.CSS_SELECTOR, value = ".start-button a")
        go_button.click()
        sleep(90)
        self.up = self.driver.find_element(By.XPATH, value='/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.down = self.driver.find_element(By.XPATH, value='/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text


    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        sleep(60)
        email_input = self.driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
        email_input.send_keys(EMAIL, Keys.ENTER)
        sleep(10)
        pass_input = self.driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
        pass_input.send_keys(PASSWORD_TWITTER,Keys.ENTER)


        sleep(10)
        tweet_compose = self.driver.find_element(By.XPATH, value='/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')

        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        sleep(3)

        tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()

bot=InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
print(bot.up)
print(bot.down)
sleep(2)
# driver.quit()

