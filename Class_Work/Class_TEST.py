from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.support.ui import Select

o = ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.amazon.in")
driver.maximize_window()
sleep(2)
driver.find_element(By.ID,"twotabsearchtextbox").send_keys("shoes")
sleep(2)
driver.find_element(By.XPATH,"(//span[@class='s-heavy'])[1]").click()
