
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.get("https://demowebshop.tricentis.com/register")
driver.maximize_window()

driver.implicitly_wait(15)


def test_fname1():
    expected = "Pradipt"
    ele = driver.find_element(By.XPATH, "//input[@id= 'FirstName']")
    ele.send_keys("Pradipt")
    actual = ele.get_attribute('value')
    assert expected == actual, 'Mismatch'



def test_fname2():
    expected = " Prasoon"
    ele = driver.find_element(By.XPATH, "//input[@id= 'LastName']")
    ele.send_keys(" Prasoon")
    actual = ele.get_attribute('value')
    assert expected == actual, 'Not Equal'
#
# def test_fname3():
#     expected = "xyz@gmail.com"
#     actual = driver.find_element(By.XPATH, "//input[@id= 'Email']").send_keys("xyz@gmail.com")
#     assert expected == actual , 'Not Equal'
#
# def test_fname4():
#     expected = "1234567890"
#     actual = driver.find_element(By.XPATH, "//input[@id= 'Password']").send_keys("1234567890")
#     assert expected == actual , 'Not Equal'
#
# def test_fname5():
#     expected = "1234567890"
#     actual = driver.find_element(By.XPATH, "//input[@id= 'ConfirmPassword']").send_keys("1234567890")
#     assert expected == actual , 'Not Equal'

# driver.close()
