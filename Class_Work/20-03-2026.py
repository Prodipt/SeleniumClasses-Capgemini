#  DROPDOWN

'''

    ->SELECT <SELECT>
    ->CUSTOM <DIV> <LI>

Single Select No deselect here

MultiSelect  deselect

Select_by_visible_text  As per given in the dropdown....
Select_by_value  attribute
Select_by_index     0,1,2,3...

'''
from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

o=ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)

driver.get("file:///C:/Users/praso/Downloads/E22_Dropdowns.html")
driver.maximize_window()

# dropdown = driver.find_element(By.ID, "state")
# option = Select(dropdown)
#
# # option.select_by_visible_text("Maharastra")
#
# option.select_by_value("MH")
# sleep(5)
# option.select_by_index(0)


dropdown = driver.find_element(By.ID, "hobby")
option = Select(dropdown)

option.select_by_index(0)
option.select_by_index(1)
option.select_by_value("badminton")

sleep(5)
# option.deselect_by_index(0)
#
# sleep(2)
# option.deselect_by_visible_text("Badminton")

option.deselect_all()

#  Custom Dropdown -> div, li