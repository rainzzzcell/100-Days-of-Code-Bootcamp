from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Access the article count element and print the text
article_count = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
print(f"Article count: {article_count.text}")

# Find the "Content portals" link and click it (optional)
all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
all_portals.click()  # Click the link to navigate to the content portals

# Perform a search for "Python"
search = driver.find_element(By.NAME, value="search")
search.send_keys("Python", Keys.ENTER)

# driver.quit()  # Uncomment this if you want to close the browser after running the script
