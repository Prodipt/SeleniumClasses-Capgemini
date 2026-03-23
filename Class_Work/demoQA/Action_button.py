from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

o = ChromeOptions()
o.add_experimental_option("detach", True)

driver = Chrome(options=o)

driver.implicitly_wait(19)
driver.get("https://demoqa.com/buttons")

driver.maximize_window()

actions = ActionChains(driver)


sleep(2)
ele1 = driver.find_element(By.XPATH, "//button[text() = 'Double Click Me']")
actions.double_click(ele1).perform()

# ele2 = driver.find_element(By.XPATH, "(//button[@class = 'btn btn-primary'])[2]")
# ele2.click()

# sleep(3)
ele3 = driver.find_element(By.XPATH, "(//button[@class = 'btn btn-primary'])[3]")
actions.click(ele3).perform()

