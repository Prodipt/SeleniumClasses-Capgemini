from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)

driver = Chrome(options=o)

driver.implicitly_wait(10)

driver.get("https://www.amazon.in/")
driver.maximize_window()

# ele = driver.find_element(By.ID, "twotabsearchtextbox")
# ele.send_keys("Watches")
# ele.send_keys(Keys.ENTER)

# driver.find_element(By.ID, "nav-search-submit-button").click()


# driver.quit()


# sleep(2)
div1 = driver.find_element(By.XPATH, "(//div[contains(@class,'a-cardui _quad-multi-asin-card-v2_fluid_fluidCard')])[1]")
actions = ActionChains(driver)

# To Pause the execution between two actions - Good to use  pause whenever required!!!
actions.scroll_to_element(div1).perform()
sleep(5)

# How much you want to scroll on the screen using x and y values
actions.scroll_by_amount(0,400).perform()

actions.scroll_by_amount(0,400).perform()
