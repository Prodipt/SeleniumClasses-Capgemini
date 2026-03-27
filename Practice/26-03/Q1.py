from time import sleep

from selenium.webdriver import Chrome, ChromeOptions

o = ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import os
import time
driver.get("https://in.pinterest.com/")

folder = os.path.join(os.getcwd(), 'screenshot')


os.makedirs(folder, exist_ok=True)

timestamp = time.strftime("%Y%m%d-%H%M%S")
driver.save_screenshot(f'{folder}/screenshot_page_{timestamp}.png')

actions = ActionChains(driver)

img = driver.find_element(By.XPATH, "(//img[@class='iFOUS5 ALBw9Q'])[12]")
actions.scroll_to_element(img)

img.screenshot(f'{folder}/element_screenshot.{timestamp}.png')

sleep(3)
driver.quit()