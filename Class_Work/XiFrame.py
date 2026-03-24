from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)

driver = Chrome(options=o)

driver.implicitly_wait(10)
driver.get("https://x.com/")
driver.maximize_window()

# wait for iframe
iframe = driver.find_element(By.XPATH, "//iframe")
driver.switch_to.frame(iframe)

driver.find_element(By.XPATH, "//span[text()='Sign up with Google']").click()

sleep(10)
driver.quit()