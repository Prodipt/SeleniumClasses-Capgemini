from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
o.add_experimental_option("prefs", {"safebrowsing.enabled": True})
o.add_argument("--disable-notifications")
driver = Chrome(options=o)


# driver.get("https://demoqa.com/upload-download")

# driver.get("https://www.python.org/downloads/")

driver.get("https://www.easemytrip.com/flights.html?utm_campaign=788997081&utm_source=g_c&utm_medium=cpc&utm_term=e_easemytrip&adgroupid=39319940377&gad_source=1&gad_campaignid=788997081&gbraid=0AAAAADo_0-h3QJ-p11y-Kv-NZh2sT2JIk&gclid=Cj0KCQjw7IjOBhDyARIsAFzrWQwzmeh6W3gCycWFa5ibvUVgUgshL7zTZOcCwTyJh_0V-JJT5en6u6kaAnAREALw_wcB")
driver.maximize_window()

driver.implicitly_wait(15)

# driver.find_element(By.LINK_TEXT, "Download Python install manager").click()
# sleep(2)
# driver.find_element(By.ID, "uploadFile").send_keys(r"C:\Users\praso\Downloads\20240222_213236.jpg")

print("Done!!!")