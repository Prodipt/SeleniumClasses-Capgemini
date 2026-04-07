import time
import pytest
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
o = ChromeOptions()
o.add_experimental_option("detach", True)


@pytest.fixture(scope='class')
def setup():
    driver = Chrome(options=o)
    driver.get("https://demowebshop.tricentis.com/register")
    driver.maximize_window()
    yield driver
    driver.quit()

class TestRegister:
    def test_gender(self, setup):
        setup.find_element(By.XPATH, "//input[@id='gender-male']").click()

    def test_name(self, setup):
        setup.find_element(By.XPATH, "//input[@id= 'FirstName']").send_keys("Pradipt ")

    def test_last(self, setup):
        setup.find_element(By.XPATH, "//input[@id= 'LastName']").send_keys(" Prasoon")

    def test_email(self, setup):
        setup.find_element(By.XPATH, "//input[@id= 'Email']").send_keys("xyz@gmail.com")

    def test_password(self, setup):
        setup.find_element(By.XPATH, "//input[@id= 'Password']").send_keys("1234567890")

    def test_confirm(self, setup):
        setup.find_element(By.XPATH, "//input[@id= 'ConfirmPassword']").send_keys("1234567890")
