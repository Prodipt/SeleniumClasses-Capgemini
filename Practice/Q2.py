from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.get("https://www.example.com")
sleep(5)
URL = driver.current_url
print(URL)

driver.close()