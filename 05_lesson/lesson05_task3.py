from selenium import webdriver
import time
from selenium.webdriver.common.by import By
browser = webdriver.Firefox()
browser.get("http://the-internet.herokuapp.com/inputs")
search_box = browser.find_element(By.CSS_SELECTOR, "input")
search_box.send_keys("Sky")
time.sleep(1)
search_box.clear()
time.sleep(1)
search_box.send_keys("Pro")
time.sleep(1)
browser.quit()
