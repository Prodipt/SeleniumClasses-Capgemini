from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.get("https://www.amazon.in/")
driver.maximize_window()

sleep(2)


# driver.find_element(By.LINK_TEXT, "Mobiles").click()

driver.find_element(By.PARTIAL_LINK_TEXT, "Releases").click()

# sleep(2)

driver.back()
sleep(1)
search = driver.find_element(By.ID, "twotabsearchtextbox")
search.send_keys('Shirt')

sleep(1)

searchButton = driver.find_element(By.ID, "nav-search-submit-button")
searchButton.click()
sleep(1)

driver.quit()
