from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

o = ChromeOptions()
o.add_experimental_option("detach", True)

o.add_experimental_option("prefs", {"safebrowsing.enabled": True})
o.add_argument("--disable-notifications")

driver = Chrome(options=o)

driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()

driver.implicitly_wait(15)

driver.find_element(By.LINK_TEXT,"JavaScript Alerts").click()

alert1 = driver.find_element(By.XPATH, "//button[text()= 'Click for JS Alert']")
alert1.click()
sleep(3)
alert = driver.switch_to.alert
print(alert.text)
alert.accept()

alert2 = driver.find_element(By.XPATH, "//button[text()= 'Click for JS Confirm']")
alert2.click()
sleep(3)
alert = driver.switch_to.alert
print(alert.text)
alert.accept()

alert3 = driver.find_element(By.XPATH, "//button[text()= 'Click for JS Prompt']")
alert3.click()
sleep(3)
alert = driver.switch_to.alert
alert.send_keys("Papppu")
print(alert.text)
alert.accept()

sleep(2)
driver.quit()