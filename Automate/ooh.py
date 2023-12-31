# Importing required libraries

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Amazon.ca homepage
driver.get("https://www.amazon.ca")
time.sleep(5)

# Finding the search bar and entering text
# search_bar = driver.find_element_by_id("id","twotabsearchtextbox") old syntax
search_bar = driver.find_element("id","twotabsearchtextbox")
search_bar.send_keys("prime deals")

# Submitting the search query
search_bar.send_keys(Keys.RETURN)

# Waiting for the search results page to load
time.sleep(5)




# Selecting a picture 
picture_link = driver.find_element("xpath","/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/span/a")
# picture_link = driver.find_element("By.CSS_SELECTOR","span[data-component-type='s-product-image'] a")
picture_link.click()
time.sleep(4)


# Clicking on Best seller button
Best_seller_button= driver.find_element("xpath","/html/body/div[2]/div[2]/div[5]/div[4]/div[4]/div[7]/div/a/i")
Best_seller_button.click()
time.sleep(3)


# Selecting a Home 
Home_link = driver.find_element("xpath","/html/body/div[1]/header/div/div[4]/div[2]/div[2]/div/a[5]")
# picture_link = driver.find_element("By.CSS_SELECTOR","span[data-component-type='s-product-image'] a")
Home_link.click()
time.sleep(4)

driver.close()




