from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create ChromeOptions object
chrome_options = webdriver.ChromeOptions()
# Comment out headless mode
# chrome_options.add_argument("--headless")

# Initialize the ChromeDriver with options
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the website
print("Navigating to the website...")
driver.get("https://www.facebook.com")
print("Website loaded successfully.")

# Wait for the element with name "email" to be present
wait = WebDriverWait(driver, 10)
input_element = wait.until(EC.presence_of_element_located((By.NAME, "email")))
input_element.send_keys("em@gmail.com")
input_element = wait.until(EC.presence_of_element_located((By.NAME, "pass")))
input_element.send_keys("1234567")

# # Find and click the button element
form_element = driver.find_element(By.XPATH, "//form")  # You can adjust the XPath to locate the form element

# Use JavaScript to submit the form
driver.execute_script("arguments[0].submit();", form_element)

# Wait for your confirmation to close
input("Press Enter to close the browser...")

# Close the browser
driver.quit()
