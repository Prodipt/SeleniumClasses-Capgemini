from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
# o.add_argument("headless")
driver = Chrome(options=o)

driver.get("https://the-internet.herokuapp.com/tables")
driver.maximize_window()

# Fetching Dynamic Element
# sleep(2)
salary = driver.find_element(By.XPATH, "//td[text()='Bach']/../td[4]")
print(salary.text)

# Sibling
sleep(2)
Due = driver.find_element(By.XPATH, "(//td[text()='Tim'])[1]//following-sibling::td[2]")
print(Due.text)


driver.close()
