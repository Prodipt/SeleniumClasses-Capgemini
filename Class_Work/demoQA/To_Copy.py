from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

o = ChromeOptions()
o.add_experimental_option("detach", True)

driver = Chrome(options=o)

driver.implicitly_wait(10)
driver.get("https://demoqa.com/text-box")

ele1 = driver.find_element(By.XPATH, "//textarea[@placeholder= 'Current Address']")
ele1.send_keys("Jaipur")
ele1.send_keys(Keys.CONTROL + 'A')
ele1.send_keys(Keys.CONTROL + 'C')


ele2 = driver.find_element(By.ID, "permanentAddress")
ele2.send_keys(Keys.CONTROL+'V')
