from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.implicitly_wait(10)

driver.get("http://uitestingplayground.com/textinput")
input = driver.find_element(By.ID, "newButtonName")
input.send_keys("SkyPro")

driver.find_element(By.ID, "updatingButton").click()

txt = driver.find_element(By.ID, "updatingButton").text
print(txt)

driver.quit()
