from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.get("https://demoqa.com/webtables")
driver.maximize_window()

# driver.implcitly_wait(10)
wait = WebDriverWait(driver, 10)

wait.until(
    EC.visibility_of_element_located((By.ID,'addNewRecordButton'))).click()



wait.until(
    EC.visibility_of_element_located((By.XPATH, "//input[@placeholder= 'First Name']"))).send_keys("Why Should I tell you.")


wait.until(
    EC.visibility_of_element_located((By.XPATH, "//input[@placeholder= 'Last Name']"))).send_keys("IDontKnow")


wait.until(
    EC.visibility_of_element_located((By.XPATH, "//input[@placeholder= 'name@example.com']"))).send_keys("IDKIDK@gmail.com")


wait.until(
    EC.visibility_of_element_located((By.XPATH, "//input[@placeholder= 'Age']"))).send_keys("32")


wait.until(
    EC.visibility_of_element_located((By.XPATH, "//input[@placeholder= 'Salary']"))).send_keys("200000")

wait.until(
    EC.visibility_of_element_located((By.XPATH, "//input[@placeholder= 'Department']"))).send_keys("Testing")

wait.until(
    EC.visibility_of_element_located((By.XPATH, "//button[@id= 'submit']"))).click()


Info = wait.until(
    EC.visibility_of_all_elements_located((By.XPATH, "//tr[4]/td[position()=1 or position()=6]"))
)

print(Info[0].text, Info[1].text)


driver.close()
