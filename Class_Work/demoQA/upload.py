from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()

driver.implicitly_wait(15)


driver.find_element(By.XPATH, "//input[@placeholder= 'First Name']").send_keys("Pradipt ")


driver.find_element(By.XPATH, "//input[@placeholder= 'Last Name']").send_keys(" Prasoon")


driver.find_element(By.XPATH, "//input[@placeholder= 'name@example.com']").send_keys("xyz@gmail.com")


driver.find_element(By.XPATH, "//input[@value='Male']").click()

driver.find_element(By.XPATH, "//input[@placeholder= 'Mobile Number']").send_keys("1234567890")

driver.find_element(By.CLASS_NAME, "subjects-auto-complete__input").send_keys("Selenium")

driver.find_element(By.ID, "hobbies-checkbox-1").click()

driver.find_element(By.ID, "hobbies-checkbox-2").click()

driver.find_element(By.ID, "dateOfBirthInput").click()

driver.find_element(By.XPATH, "//div[text() = 27]").click()

driver.find_element(By.XPATH, "//textarea[@placeholder= 'Current Address']").send_keys("Jaipur")




d1 = driver.find_element(By.ID, "react-select-3-placeholder")
d1.click()
# driver.find_element(By.XPATH,)
# d1.select_by_visible_text("NCR")

driver.find_element(By.ID, "uploadPicture").send_keys(r"C:\Users\praso\Downloads\20240222_213236.jpg")

# driver.find_element(By.ID, "state").click()
#
# dd = driver.find_element(By.ID, "city")
# dd.click()
# ss = Select(dd)

# ss.select_by_index(2)