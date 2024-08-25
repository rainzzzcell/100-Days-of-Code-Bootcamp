from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")

# Correct CSS selectors
widget_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
widget_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

widget = {}

for n in range(len(widget_times)):
    widget[n] = {
        "time": widget_times[n].text,
        "name": widget_names[n].text,
    }

print(widget)

# driver.quit()  # Uncomment this if you want to close the browser after running the script
