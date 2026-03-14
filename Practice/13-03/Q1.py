from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.get("https://Selenium.dev/")

driver.maximize_window()
driver.find_element(By.LINK_TEXT, "Downloads").click()
sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT, "other languages exist").click()
sleep(2)
print(driver.title)

driver.quit()