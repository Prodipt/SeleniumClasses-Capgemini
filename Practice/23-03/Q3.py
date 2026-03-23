from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)

driver = Chrome(options=o)

driver.implicitly_wait(10)

driver.get("https://www.flipkart.com/")
driver.maximize_window()

action = ActionChains(driver)

driver.find_element(By.XPATH, "//span[@class='b3wTlE']").click()

# sleep(3)
footer = driver.find_element(By.XPATH, "//div[@class='x3q9HG']")
action.scroll_to_element(footer).perform()


myntru = driver.find_element(By.XPATH, "((//div[@class='ykJuJZ'])[2]/following::a)[1]")
action.click(myntru).perform()

cleartripi = driver.find_element(By.XPATH, "((//div[@class='ykJuJZ'])[2]/following::a)[2]")
action.click(cleartripi).perform()

shopufu = driver.find_element(By.XPATH, "((//div[@class='ykJuJZ'])[2]/following::a)[3]")
action.click(shopufu).perform()

for i in range(4):
    driver.switch_to.window(driver.window_handles[i])
    print(driver.title)
    print(driver.current_window_handle)
    print(driver.current_url)
    print("---------------------------------------------------------------------------------------------------\n")

sleep(1)

driver.close()