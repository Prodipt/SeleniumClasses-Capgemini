from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.get("https://www.amazon.in/")
driver.maximize_window()

sleep(2)

driver.find_element(By.ID, "twotabsearchtextbox").send_keys("Mobile")

driver.find_element(By.ID, "nav-search-submit-button").click()
# driver.find_element(By.XPATH, "(//span[contains(text(), 'iPhone 16 Plus')])[1]").click()

price = driver.find_element(By.XPATH, "(//span[text()='₹'])[4]//following-sibling::span")
print(price.text)
sleep(3)
