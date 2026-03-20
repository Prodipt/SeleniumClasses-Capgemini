from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

o=ChromeOptions()
o.add_experimental_option('detach',True)
driver = Chrome(options=o)

driver.implicitly_wait(15)
driver.get("https://www.amazon.in/")
driver.maximize_window()

driver.find_element(By.ID, 'twotabsearchtextbox').send_keys("Shoes for men")

sleep(2)
options = driver.find_elements(By.XPATH, "//div[@class='s-suggestion-container']")

for i in options:
    print(i.text)

# driver.find_element(By.XPATH, "(//div[@class='s-suggestion-container'])[10]").click()
options[9].click()

sleep(10)
driver.quit()