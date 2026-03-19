from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.get("https://www.naukri.com/registration/createAccount?othersrcp=23531&utm_source=google&utm_medium=cpc&utm_campaign=Search_Brand_FORGE&gclsrc=aw.ds&gad_source=1&gad_campaignid=22529405481&gbraid=0AAAAADLp3cFtIlNti7ZPj3LCQqe3UBETC&gclid=EAIaIQobChMI45CBqrSrkwMVICCDAx2MYxelEAAYASAAEgLDRvD_BwE")
driver.maximize_window()

driver.implicitly_wait(15)


register = driver.find_element(By.XPATH, "//button[@type= 'submit']")

print("Register Button Displayed:", register.is_displayed())
print("Register Button Enabled:", register.is_enabled())