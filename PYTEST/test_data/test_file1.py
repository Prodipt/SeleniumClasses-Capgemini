
import pytest
from sheet02 import get_test_data


from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.parametrize("u, p, e", get_test_data())
def test_01(u, p, e, setup):
    driver = setup
    wait = WebDriverWait(driver, 30)
    u1 = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder = 'Username']")))
    u1.send_keys(u)
    p1 = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder = 'Password']")))
    p1.send_keys(p)

    driver.find_element(By.ID, "login-button").click()

    page = driver.page_source

    assert e in page , driver.refresh()
    driver.back()

# def test_close():
#     driver.close()