"""
Open demowebshop application
Scroll to Facebook link (bottom of page)
Click and enter username and password
Click on login
"""
from time import sleep

from selenium.webdriver import Chrome, ChromeOptions

from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains


o=ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)

driver.implicitly_wait(15)
driver.get("https://demowebshop.tricentis.com")

driver.maximize_window()
action = ActionChains(driver)
element1 = driver.find_element(By.XPATH, "//a[text()='Facebook']")
action.scroll_to_element(element1).perform()

element1.click()

driver.switch_to.window(driver.window_handles[1])

driver.find_element(By.XPATH, "//span[text()='Email address or phone number']/following::input").send_keys("monaisha@gmail.com")

driver.find_element(By.XPATH, "//span[text()='Password']/following::input").send_keys("hello world")

driver.find_element(By.XPATH, "(//span[text()='Log in'])[3]").click()

sleep(4)
driver.close()