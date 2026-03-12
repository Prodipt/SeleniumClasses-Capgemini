from time import sleep

# from selenium.webdriver import Chrome
# driver = Chrome()
#
# # sleep(5)
'''
from selenium.webdriver import Edge
driver = Edge()

sleep(5)
'''

from selenium.webdriver import Chrome,ChromeOptions
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

'''
Python Script
     │
     ▼
Import Selenium WebDriver
     │
     ▼
Create ChromeOptions object
     │
     ▼
Add setting → detach = True
     │
     ▼
Launch Chrome browser with those settings
'''

# Open a URL or local files
# Return# of get() is noneś
# driver.get("https://www.google.com")

# To Maximize it'
# driver.maximize_window()

# driver.fullscreen_window()

# To fetch the title
# Title, URL are the PROPERTY
# title = driver.title
# print(title)
#
# print(driver.current_url)
# print(driver.page_source)

driver.get("https://amazon.in")
driver.fullscreen_window()
title = driver.title
print(title)

print(driver.name)
sleep(3)
# For backward
driver.back()
sleep(3)
# For forward
driver.forward()
sleep(3)
# To Refresh
driver.refresh()
sleep(3)
driver.close()  #Just for the Tab
driver.quit() #For the entire brower window