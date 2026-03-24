from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)

o.add_experimental_option("prefs", {"safebrowsing.enabled": True})
o.add_argument("--disable-notifications")

driver = Chrome(options=o)

driver.get("https://www.irctc.co.in/nget/train-search")
driver.maximize_window()

driver.implicitly_wait(15)

driver.find_element(By.XPATH, "//span[@class='ng-tns-c69-9 ui-calendar']").click()


driver.find_element(By.XPATH, "//span[@class='ui-datepicker-next-icon pi pi-chevron-right ng-tns-c69-9']").click()

driver.find_element(By.LINK_TEXT, "19").click()



print("Done!!!")