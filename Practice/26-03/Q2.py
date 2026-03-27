from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.support.select import Select

o = ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import os
import time

driver.get("https://www.lenskart.com/")
driver.maximize_window()

driver.implicitly_wait(15)
driver.find_element(By.LINK_TEXT, "EYEGLASSES").click()

expected = "https://www.lenskart.com/eyeglasses.html"

actual = driver.current_url

assert expected == actual , "Not on the right URL"

# driver.move_to_element(By.ID, "sortByDropdown")

ll = driver.find_element(By.ID, "sortByDropdown")

s = Select(ll)

s.select_by_value("popular")

folder = os.path.join(os.getcwd(), 'screenshot')
os.makedirs(folder, exist_ok=True)

timestamp = time.strftime("%Y%m%d-%H%M%S")
driver.save_screenshot(f'{folder}/screenshot_page_{timestamp}.png')

sleep(3)
driver.quit()