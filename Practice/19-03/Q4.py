
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By


o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

driver.implicitly_wait(15)


driver.find_element(By.ID, "singleFileInput").send_keys(r"C:\Users\praso\Downloads\20240222_213236.jpg")

driver.find_element(By.ID, "multipleFilesInput").send_keys("C://Users//praso//Downloads//20240222_213236.jpg\n", "C://Users//praso//Downloads//ChatGPT Image Mar 7, 2026, 11_58_35 PM.png")
