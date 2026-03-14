from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.get("https://www.myntra.com/")
sleep(1)
driver.maximize_window()

sleep(2)

driver.find_element(By.CLASS_NAME, "desktop-searchBar").send_keys("Shoes")
sleep(1)
driver.find_element(By.CLASS_NAME, "desktop-submit").click()

sleep(2)
driver.quit()