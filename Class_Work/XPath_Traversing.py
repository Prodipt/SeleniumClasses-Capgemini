from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
# o.add_experimental_option("headless")
driver = Chrome(options=o)

driver.get("https://demoqa.com/webtables")
driver.maximize_window()


sleep(2)
salary = driver.find_element(By.XPATH, "//td[text()='Cantrell']/../td[6]")
print(salary.text)
