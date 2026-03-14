from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.get("https://www.naukri.com/")
sleep(1)
driver.maximize_window()

driver.find_element(By.LINK_TEXT, "Register").click()
sleep(2)

driver.find_element(By.ID, "name").send_keys("Pradipt Prasoon")
sleep(1)
driver.find_element(By.ID, "email").send_keys("prasoon22@gmail.com")
sleep(1)
driver.find_element(By.ID, "password").send_keys("PP@1234pp")

sleep(2)
driver.quit()