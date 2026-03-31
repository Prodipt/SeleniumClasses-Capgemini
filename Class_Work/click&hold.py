from time import sleep
from tkinter import Scrollbar

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)

driver = Chrome(options=o)

driver.implicitly_wait(10)

driver.get("https://yonobusiness.sbi.bank.in/yonobusinesslogin")
driver.maximize_window()

actions = ActionChains(driver)

driver.find_element(By.XPATH, "//span[@class='ng-tns-c2785778308-3 icon-cancel']").click()

password = driver.find_element(By.XPATH, "//input[@placeholder= 'Enter your Password']")

password.send_keys("Heyy,_Can_You_See_ME???")

icon = driver.find_element(By.XPATH, "(//img[@class= 'ng-star-inserted'])[1]")

actions.click_and_hold(icon).pause(4).release().perform()

driver.close()