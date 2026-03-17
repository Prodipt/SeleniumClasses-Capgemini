from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

# driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

driver.get("https://www.decathlon.in/")
driver.maximize_window()
driver.implicitly_wait(10)
# driver.find_element(By.XPATH, '//button').click()
driver.find_element(By.XPATH, "//a[contains(@href, 'https://www.decathlon.in/shop/Winter-Collection')]").click()

driver.find_element(By.XPATH, "//a[contains(@href, 'https://www.decathlon.in/c/beanies-headbands-828581')]").click()

# message = driver.find_element(By.XPATH, "//div[@id='finish']/h4")

# print(message.text)

