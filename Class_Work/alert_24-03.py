from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

o = ChromeOptions()
o.add_experimental_option("detach", True)

driver = Chrome(options=o)

driver.implicitly_wait(19)
driver.get("https://testautomationpractice.blogspot.com/")

driver.maximize_window()

actions = ActionChains(driver)
#
# alert1= driver.find_element(By.ID, "alertBtn")
# alert1.click()
# sleep(3)
# alert = driver.switch_to.alert
# alert.accept()


# alert2 = driver.find_element(By.ID, "confirmBtn")
# alert2.click()
# sleep(3)
# alert = driver.switch_to.alert
# # alert.accept()
# alert.dismiss()

alert3 = driver.find_element(By.ID, "promptBtn")
alert3.click()
sleep(3)
alert = driver.switch_to.alert

alert.send_keys("XYZ")
alert.accept()

print("Done!!!!")
