from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

o=ChromeOptions()
o.add_experimental_option('detach',True)
driver = Chrome(options=o)

driver.get("https://www.bmrc.co.in/")
driver.maximize_window()

driver.implicitly_wait(15)

driver.find_element(By.XPATH, "//span[. ='English']").click()

first = driver.find_element(By.XPATH, "(//select[@class= 'form-control select fare-selects'])[1]")

d = Select(first)
d.select_by_index(5)

second = driver.find_element(By.XPATH, "(//select[@class= 'form-control select fare-selects'])[2]")

s = Select(second)
s.select_by_index(2)

driver.find_element(By.XPATH, "//button[@class='app-btn-box']").click()

# sleep(10)
# driver.quit()