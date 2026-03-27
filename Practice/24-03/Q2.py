from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)

driver = Chrome(options=o)

driver.implicitly_wait(10)
driver.get("https://www.zomato.com/jaipur/restaurants")
driver.maximize_window()

# wait for iframe
driver.find_element(By.LINK_TEXT, "Log in").click()

iframe = driver.find_element(By.ID, "auth-login-ui")
driver.switch_to.frame(iframe)

driver.find_element(By.XPATH, "//span[text()='Send One Time Password']").click()

sleep(10)
driver.quit()