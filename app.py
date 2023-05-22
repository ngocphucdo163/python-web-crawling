from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode (without GUI)

# Path to the chromedriver executable
chromedriver_path = "./chrome-driver/chromedriver"

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)

# URL of the website to crawl
url = "https://example.com"

# Open the website
driver.get(url)

# Wait for the page to load completely
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

# Capture network traffic responses
entries = driver.execute_script("return window.performance.getEntries()")

# Print the network traffic responses
for entry in entries:
    print(entry["name"])

# Close the browser
driver.quit()