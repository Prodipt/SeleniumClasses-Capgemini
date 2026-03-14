from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.get("https://www.youtube.com/")
sleep(1)
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "input[name='search_query']").send_keys("melody hits")

driver.find_element(By.CSS_SELECTOR, "button[aria-label='Search']").click()

sleep(2)
driver.quit()