from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.get("https://www.facebook.com/")
sleep(1)
driver.maximize_window()
sleep(2)
driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("@gmail.com")
sleep(3)
driver.find_element(By.CSS_SELECTOR, "input[name='pass']").send_keys("password")
sleep(2)

driver.find_element(By.CSS_SELECTOR, "div[aria-label='Log in']").click()
sleep(4)
driver.quit()