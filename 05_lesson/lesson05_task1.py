from selenium import webdriver
import time
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
browser.get("http://uitestingplayground.com/classattr")
browser.find_element(By.CLASS_NAME, "btn-primary").click()
time.sleep(3)
browser.quit()
