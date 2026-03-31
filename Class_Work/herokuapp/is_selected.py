from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.get("https://the-internet.herokuapp.com/checkboxes")
driver.maximize_window()

driver.implicitly_wait(15)


checkbox1 = driver.find_element(By.XPATH, "//input[@type='checkbox'][1]")

print("CheckBox 1:", checkbox1.is_selected())

checkbox2 = driver.find_element(By.XPATH, "//input[@type='checkbox'][2]")

print("CheckBox 2:", checkbox2.is_selected())


driver.close()