'''
Open Wikipedia
Refresh
Fetch Title
Open Amazon
Fetch title
Go back
close
'''
from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.get("https://www.wikipedia.org/")

driver.refresh()
sleep(5)
title = driver.title
print(title)
sleep(3)

driver.get("https://www.amazon.in")
sleep(4)
title = driver.title
print(title)


driver.back()
sleep(2)
driver.close()