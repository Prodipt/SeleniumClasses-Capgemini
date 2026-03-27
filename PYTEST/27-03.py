from time import sleep
import time

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
import os

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.implicitly_wait(16)
'''
driver.get("https://www.google.com/")

driver.maximize_window()

folder = os.path.join(os.getcwd(), 'screenshots')
# To create a folder
os.makedirs(folder, exist_ok=True)
# To check whether the folder is present or not

driver.save_screenshot(f'{folder}/ss1_page.png')
# To put ss inside the folder

ele = driver.find_element(By.XPATH, "//textarea[@title ='Search']")
# ele.screenshot(f'{folder}/ss1_element.png')

timestamp = time.strftime("%Y%m%d-%H%M%S")
ele.screenshot(f'{folder}/ss1_element_{timestamp}.png')

# print(driver.title)
expected = 'Google'
actual = driver.title

assert expected  == actual , "Title Mismatch"
# # assert , condition , what message should be display if the condition fail
#
# driver.find_element(By.XPATH, "//textarea[@title ='Search']").send_keys(actual)

sleep(2)
driver.close()
'''

'''
driver.get("https://www.amazon.in/")

driver.maximize_window()

# print(driver.title)
driver.find_element(By.LINK_TEXT, "Bestsellers").click()

expected = 'Amazon.in Bestsellers: The most popular items on Amazon'
actual = driver.title


assert expected  == actual , "Title Mismatch"
# assert , condition , what message should be display if the condition fail

print(actual)

sleep(2)
driver.close()
'''

'''
v -> verbocity
'''

driver.get("https://www.saucedemo.com/")

folder = os.path.join(os.getcwd(), 'screenshots')
# To create a folder
os.makedirs(folder, exist_ok=True)

u = driver.find_element(By.XPATH, "//input[@placeholder= 'Username']")
p = driver.find_element(By.XPATH, "//input[@placeholder= 'Password']")

u.send_keys("standard_user")
p.send_keys("2345678")

driver.find_element(By.ID, "login-button").click()

not_login = "Epic sadface: Username and password do not match any user in this service"
actual = driver.find_element(By.XPATH, "//h3[@data-test='error']")

assert not_login == actual, driver.save_screenshot(f'{folder}/login.png')

assert not_login != actual, "Logged In Successfully"

sleep(3)
driver.close()



'''
Pytest is a unit testing framework, the rules for:
        - File should start with test_
        - Function name or method name should also start with test_
        - Class name should start with Test_
   When we follow these rules, pytest will automatically recognize the files,
   functions and classes following the rules so without giving function call we can execute a test function
   and without creating a object we can execute a test class
   -v stands for verbocity: it gives detailed description/explanation of the code
   -s stands for scripting: it will capture all the print statements (pytest captures all output (like print() statements) and only shows it when a test fails)
   * pytest cannot recognize the function which doesn't follow the rule
   * In case of test classes, we need not create object and call the functions, if we do so execution will happen twice
'''