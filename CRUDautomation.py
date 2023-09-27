from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)

print("Navigating to the website...")
driver.get("https://emonkumardas.github.io/Todo-list/")
print("Website loaded successfully.")

wait = WebDriverWait(driver, 10)
input_element = wait.until(EC.presence_of_element_located((By.ID, "input-todo")))
input_element.send_keys("emon")

add_button_element = driver.find_element(By.ID, "add-todo")
add_button_element.click()
time.sleep(2)

edit_button_element = driver.find_element(By.XPATH, "//button[contains(text(),'Edit')]")
edit_button_element.click()

alert = wait.until(EC.alert_is_present())

new_text =  " Emon kumar"
alert.send_keys(new_text)
alert.accept()
time.sleep(5)

delete_button_element = driver.find_element(By.XPATH, "//button[contains(text(),'Delete')]")
delete_button_element.click()

input("Press Enter to close the browser...")

driver.quit()
