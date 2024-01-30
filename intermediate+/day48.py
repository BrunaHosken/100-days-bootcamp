from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")

# search_bar = driver.find_element(By.NAME, value="q")
# # By.CLASS_NAME
# print(search_bar.tag_name)
# print(search_bar.get_attribute("placeholder"))
# button=driver.find_element(By.ID, value="submit")
# print(button.size)
# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)
# bug_link= driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

events = {}

for n in range(len(event_times)):
    events[n] = {
        "time":event_times[n].text,
        "name":event_names[n].text
    }

print(events)
# <li>
# <time datetime="2024-01-17T17:00:00+00:00"><span class="say-no-more">2024-</span>01-17</time>
#  <a href="/events/python-user-group/1632/">Python Meeting Düsseldorf</a>
# </li>
                                             
                            

# driver.find_elements(By.CSS_SELECTOR)
# driver.close()
driver.quit()