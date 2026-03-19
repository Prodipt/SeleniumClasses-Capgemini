from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.get("https://demowebshop.tricentis.com/register")
driver.maximize_window()

driver.implicitly_wait(15)

driver.find_element(By.XPATH, "//input[@id='gender-male']").click()

driver.find_element(By.XPATH, "//input[@id= 'FirstName']").send_keys("Pradipt ")


driver.find_element(By.XPATH, "//input[@id= 'LastName']").send_keys(" Prasoon")


driver.find_element(By.XPATH, "//input[@id= 'Email']").send_keys("xyz@gmail.com")



driver.find_element(By.XPATH, "//input[@id= 'Password']").send_keys("1234567890")

driver.find_element(By.XPATH, "//input[@id= 'ConfirmPassword']").send_keys("1234567890")

driver.find_element(By.ID, "register-button").click()

driver.close()
