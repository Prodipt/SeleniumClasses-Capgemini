from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.get("https://www.facebook.com/")
driver.maximize_window()

driver.implicitly_wait(15)

login = driver.find_element(By.XPATH, "//div[@aria-label= 'Log in']")

print("Login Button Displayed:", login.is_displayed())
print("Login Button Enabled:", login.is_enabled())

submit = driver.find_element(By.XPATH, "//input[@type= 'submit']")

print("Submit Button Displayed:", submit.is_displayed())
print("Submit Button Enabled:", submit.is_enabled())