from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.get("https://www.flipkart.com/")
driver.maximize_window()

sleep(2)
# driver.find_element(By.CLASS_NAME, "b3wTlE").click()
# sleep(2)
#
# # driver.find_element(By.XPATH, "//input[contains(@placeholder, 'Search for Products, Brands and More')]").click()
# driver.find_element(By.XPATH, "//input[@placeholder]").send_keys("Gym Equipment")
# sleep(2)
# driver.find_element(By.XPATH, "//button[@aria-label ]").click()
sleep(3)

# driver.close()