from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.get("https://www.pexels.com/")
driver.maximize_window()

sleep(2)

driver.find_element(By.ID, "search").send_keys("Wedding")
driver.find_element(By.XPATH, '//button[@type="submit"]').click()
sleep(3)
# driver.find_element(By.XPATH, '//input[contains(@type, "checkbox")]').click()


sleep(2)