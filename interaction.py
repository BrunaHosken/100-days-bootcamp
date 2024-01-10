from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# articles = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# print(articles.text)

# all_portal= driver.find_element(By.LINK_TEXT, value="Content portals")
# # all_portal.click()

# search=driver.find_element(By.NAME, value="search")
# search.send_keys("Python",Keys.ENTER)

driver.get("http://secure-retreat-92358.herokuapp.com/")

f_name=driver.find_element(By.NAME, value="fName")
f_name.send_keys("bruna",Keys.TAB)

l_name=driver.find_element(By.NAME,  value="lName")
l_name.send_keys("teste",Keys.TAB)

email=driver.find_element(By.NAME,  value="email")
email.send_keys("bruna.teste@gmail.com",Keys.ENTER)
driver.quit()