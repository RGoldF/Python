from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

src = driver.find_element(By.CSS_SELECTOR, '#award').get_attribute("src")

print(src)

driver.quit()
