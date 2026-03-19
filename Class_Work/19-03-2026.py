from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.get("https://www.google.com")
driver.maximize_window()

driver.implicitly_wait(15)


# driver.find_element(By.TAG_NAME, 'a').click()  ##First a tag clicked
#
# links = driver.find_elements(By.TAG_NAME, 'a')
# print(links)
#
#
# for i in links:
#     print(i.text)

ele = driver.find_element(By.XPATH, '//a[@class= "gb_Z"]')

print(ele.get_attribute('aria-label'))