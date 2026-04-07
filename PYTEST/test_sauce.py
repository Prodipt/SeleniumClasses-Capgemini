import pytest
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

o = ChromeOptions()

o.add_experimental_option('detach', True)
driver = Chrome(options=o)

driver.get("https://www.saucedemo.com/")
driver.maximize_window()
driver.implicitly_wait(30)

wait = WebDriverWait(driver, 30)




@pytest.mark.parametrize("u, p, e",[
    ('standard_user', 'secret_sauce', 'Products'),
    ('Wrong_user', 'secret_sauce','Products'),
    ('standard_user', 'secret_sauce', 'Products'),
    ('standard_user', 'secret   sauce', 'Products')
])
def test_01(u, p, e):

    u1 = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder = 'Username']")))
    u1.send_keys(u)
    p1 = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder = 'Password']")))
    p1.send_keys(p)

    driver.find_element(By.ID, "login-button").click()

    page = driver.page_source

    assert e in page , driver.refresh()
    driver.back()

def test_close():
    driver.close()