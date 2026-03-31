from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

o = ChromeOptions()
o.add_experimental_option("detach", True)

driver = Chrome(options=o)

driver.implicitly_wait(19)
driver.get("file:///C:/Users/praso/OneDrive/Documents/GenAI/Python/Capgemini-Selenium_Python/html%20file/page1.html")

# driver.maximize_window()

actions = ActionChains(driver)

# Using indexing

'''
driver.find_element(By.ID, "inp1").send_keys("First")
driver.switch_to.frame(0)
driver.find_element(By.ID, "inp2").send_keys("Second")
driver.switch_to.frame(0)
driver.find_element(By.ID, "inp3").send_keys("Third")
'''

# Using id

inp1= driver.find_element(By.ID, "inp1")
inp1.send_keys("First")
driver.switch_to.frame("frame2")

inp2= driver.find_element(By.ID, "inp2")
inp2.send_keys("Second")
driver.switch_to.frame("frame3")

inp3 =driver.find_element(By.ID, "inp3")
inp3.send_keys("Third")

# driver.switch_to.parent_frame()
# inp2.clear()
# inp2.send_keys("I am PARENT of page 3")
#
# driver.switch_to.parent_frame()
# inp1.clear()
# inp1.send_keys("I am PARENT of Page 2 ")

driver.switch_to.default_content()
inp1.send_keys("I have reached the DEFAULT CONTENT")


# Using name

'''
driver.find_element(By.ID, "inp1").send_keys("First")
driver.switch_to.frame("f2")
driver.find_element(By.ID, "inp2").send_keys("Second")
driver.switch_to.frame("f3")
driver.find_element(By.ID, "inp3").send_keys("Third")
'''