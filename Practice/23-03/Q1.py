from time import sleep
from tkinter import Scrollbar

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)

driver = Chrome(options=o)

driver.implicitly_wait(10)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

action = ActionChains(driver)

action.scroll_by_amount(0, 1200).perform()

element1 = driver.find_element(By.XPATH, "//button[@class='dropbtn']")
action.move_to_element(element1).pause(3).perform()

sleep(3)
element2 = driver.find_element(By.XPATH, "//button[text()= 'Copy Text']")
action.double_click(element2).perform()


drag = driver.find_element(By.ID, "draggable")

drop= driver.find_element(By.ID, "droppable")

action.pause(3).drag_and_drop(drag, drop).perform()


driver.close()