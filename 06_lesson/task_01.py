from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)

driver.get("http://uitestingplayground.com/ajax")
driver.find_element(By.ID, "ajaxButton").click()

success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "p.bg-success")))
print(success.text)

driver.quit()
