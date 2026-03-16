from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.get("https://demoqa.com/text-box/")
driver.maximize_window()

sleep(2)

driver.find_element(By.XPATH, '//input[@placeholder="Full Name"]').send_keys("Pradipt Prasoon")

driver.find_element(By.XPATH, '//input[@placeholder="name@example.com"]').send_keys("qwerty@gmail.com")

driver.find_element(By.XPATH, '//textarea[@placeholder="Current Address"]').send_keys("JECRC University")

driver.find_element(By.XPATH, '//textarea[@id="permanentAddress"]').send_keys("God")


# driver.find_element(By.XPATH, '//button[text()="Submit"]').click()
driver.find_element(By.XPATH, '//button[.="Submit"]').click()


sleep(3)
driver.quit()