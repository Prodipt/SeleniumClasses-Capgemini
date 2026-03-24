from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

o = ChromeOptions()
o.add_experimental_option("detach", True)

o.add_experimental_option("prefs", {"safebrowsing.enabled": True})
o.add_argument("--disable-notifications")

driver = Chrome(options=o)

driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()

driver.implicitly_wait(15)

driver.find_element(By.ID, "dateOfBirthInput").click()


month = driver.find_element(By.XPATH, "//select[@class = 'react-datepicker__month-select']")

dd= Select(month)
dd.select_by_value("5")

year = driver.find_element(By.XPATH, "//select[@class = 'react-datepicker__year-select']")

yy = Select(year)
yy.select_by_visible_text("2020")

print("Done!!!")