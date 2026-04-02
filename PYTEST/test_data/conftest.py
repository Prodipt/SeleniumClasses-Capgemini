import pytest
from selenium.webdriver import Chrome, ChromeOptions
o = ChromeOptions()
o.add_experimental_option("detach", True)

driver = Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

@pytest.fixture(autouse=True)
def setup():
    o.add_argument("--disable-notiifications")
    yield driver
    # driver.close()