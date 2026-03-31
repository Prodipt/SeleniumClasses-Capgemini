from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.get("https://www.amazon.in/")
driver.maximize_window()

driver.implicitly_wait(15)

search = driver.find_element(By.ID, "twotabsearchtextbox")
search.send_keys('Witch')

searchButton = driver.find_element(By.ID, "nav-search-submit-button")
searchButton.click()

products = driver.find_elements(By.XPATH, '//h2[@class="a-size-medium a-spacing-none a-color-base a-text-normal"]')
print(len(products))

# print(products[5].text)

ele = driver.find_elements(By.XPATH, "//a[@class='nav-a  ']")


for i in ele:
    print(i.get_attribute('href'))

