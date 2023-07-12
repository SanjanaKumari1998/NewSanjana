# Test Case
# 1) Open Web Browser(Chrome/firefox/edge).
# 2) Open URL https://github.com/login/.
# 3) Enter the Username (sharmasulika@gmail.com)
# 4) Enter the password(Sulika@1995)
# 5) Click on Sign in.
# 6) Click on the Following.
# 7) Click on the Explore GitHub.
# 8) close browser


# Importing required libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Git hub website homepage
driver.get("https://github.com/login")
time.sleep(4)

# fill the username and password afterwards click.
driver.find_element("id", "login_field").send_keys("sharmasulika@gmail.com")
driver.find_element("id", "password").send_keys("Sulika@1995")
driver.find_element("name", "commit").click()
time.sleep(4)

# click on the following and explore github show
driver.find_element("id", "feed-original").click()
driver.find_element("xpath","/html/body/div[1]/div[6]/div/div/div/div/div/div/main/div/div/div/feed-container/turbo-frame/tab-container/div[3]/div[1]/a").click()
time.sleep(4)

# # Closing the webdriver
driver.close()
