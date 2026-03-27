
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

o=ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)

driver.implicitly_wait(15)
driver.get("https://www.amazon.in")
driver.maximize_window()

driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('Shoes')

driver.find_element(By.XPATH, "//div[@aria-rowindex='4']").click()
driver.find_element(By.XPATH, "//span[text()='Sort by:']").click()
driver.find_element(By.XPATH, "//a[text() = 'Newest Arrivals']").click()

driver.find_element(By.XPATH, "(//i[@class='a-icon a-icon-checkbox'])[3]").click()

name = driver.find_element(By.XPATH, "(//a[@class='a-link-normal s-line-clamp-2 puis-line-clamp-3-for-col-4-and-8 s-link-style a-text-normal'])[1]")
price = driver.find_element(By.XPATH, "//div[@data-cy='asin-faceout-container']//div[@class='a-row']//span[@class='a-price-whole']")

print(f"First product {name.text} with price is: {price.text}")

sleep(2)
# driver.quit()