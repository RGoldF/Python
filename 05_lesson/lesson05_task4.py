from selenium import webdriver
import time
from selenium.webdriver.common.by import By
browser = webdriver.Firefox()
browser.get("http://the-internet.herokuapp.com/login")
username = browser.find_element(By.NAME, "username")
username.send_keys("tomsmith")
time.sleep(1)
password = browser.find_element(By.ID, "password")
password.send_keys("SuperSecretPassword!")
time.sleep(1)
login_button = browser.find_element(By.CSS_SELECTOR, "button.radius").click()
time.sleep(1)
need_text = browser.find_element(By.ID, "flash")
print(need_text.text)
browser.quit()
