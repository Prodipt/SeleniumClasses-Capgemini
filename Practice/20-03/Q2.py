from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

o=ChromeOptions()
o.add_experimental_option('detach',True)
driver = Chrome(options=o)

driver.implicitly_wait(15)
driver.get("https://www.zomato.com/jaipur/restaurants")
driver.maximize_window()

search = driver.find_element(By.XPATH, "//input[@placeholder = 'Search for restaurant, cuisine or a dish']")
search.send_keys("Laddu")

search.click()

sleep(2)
options = driver.find_elements(By.XPATH, "//p[@class='sc-1hez2tp-0 sc-gFXMyG jkvifB']")

for i in options:
    print(i.text)

options[1].click()

sleep(10)
driver.quit()