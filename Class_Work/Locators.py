from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.get("https://demoqa.com/text-box")
driver.maximize_window()




# driver.find_element(By.ID, "userName").send_keys('PRADIPT')
sleep(1)
username = driver.find_element(By.ID, "userName")
username.send_keys('Prasoon')

sleep(1)

useremail = driver.find_element(By.ID, "userEmail")
useremail.send_keys('pp@gmail.com')
sleep(1)
currAddress = driver.find_element(By.ID, "currentAddress")
currAddress.send_keys('Jaipur')


sleep(1)
perAddress = driver.find_element(By.ID, "permanentAddress")
perAddress.send_keys('Mars')

sleep(1)
perAddress = driver.find_element(By.TAG_NAME, "INPUT")
perAddress.send_keys(' GADBAD TAG ')


sleep(2)
driver.find_element(By.ID, "submit").click()
sleep(3)
driver.quit()