import pytest
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

o=ChromeOptions()

o.add_experimental_option('detach', True)
driver = Chrome(options=o)

driver.get("https://leetcode.com/problemset/")
driver.maximize_window()
driver.implicitly_wait(30)

wait = WebDriverWait(driver, 30)

actual1 = wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[@class ='ellipsis line-clamp-1'])[1]"))).text
expected1 = "3418. Maximum Amount of Money Robot Can Earn"

@pytest.mark.skip
def test_01():
    assert actual1 == expected1 , "This is a different Q"



# @pytest.mark.skipif(actual1 == expected1, reason="Both are equal")
# def test_02():
