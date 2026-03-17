from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

o = ChromeOptions()
o.add_experimental_option("detach", True)

driver = Chrome(options=o)

driver.get("https://www.flipkart.com/")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "b3wTlE"))).click()

wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//input[@placeholder='Search for Products, Brands and More']")
    )
).send_keys("Gym Equipment")

wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

prices = wait.until(
    EC.presence_of_all_elements_located((By.XPATH, "(//div[@class='Ldgg5w'])/span"))
)

print(prices[0].text)

driver.close()