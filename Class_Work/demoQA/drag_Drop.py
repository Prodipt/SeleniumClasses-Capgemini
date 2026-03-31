from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)

driver = Chrome(options=o)

driver.implicitly_wait(10)

driver.get("https://demoqa.com/droppable")
driver.maximize_window()

actions = ActionChains(driver)


dragElement = driver.find_element(By.ID, "draggable")


dropElement = driver.find_element(By.ID, "droppable")


actions.pause(3).drag_and_drop(dragElement, dropElement).perform()
