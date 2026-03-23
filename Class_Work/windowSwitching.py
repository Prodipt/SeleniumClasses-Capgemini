from time import sleep
from tkinter import Scrollbar

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)

driver = Chrome(options=o)

driver.implicitly_wait(10)

driver.get("https://www.google.com/?zx=1774263324961&no_sw_cr=1")
driver.maximize_window()

actions = ActionChains(driver)

sleep(5)

# Manually open 3 tabs
print("----------------------------------------")

print("Before : ")
print(driver.current_window_handle)

print(driver.title)

driver.switch_to.new_window()
driver.get("https://www.amazon.in/")
sleep(3)
print(driver.window_handles)

print("-----------------------------------")
print("After : ")
print(driver.title)
print(driver.current_window_handle)

driver.switch_to.window(driver.window_handles[0])
sleep(3)
driver.find_element(By.LINK_TEXT, "About").click()