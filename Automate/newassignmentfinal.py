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

# Verifying that the search results page has loaded
assert "prime deals" in driver.title

# Selecting a belt from the search results
belt_link = driver.find_element("xpath","/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/span/a/div")
# belt_link = driver.find_element("By.CSS_SELECTOR","span[data-component-type='s-product-image'] a")
belt_link.click()
time.sleep(4)





#size_element = driver.find_element("id""waist 28-34")
#driver.find_element("xpath","//html/body/div[2]/div[2]/div[5]/div[1]/div[1]/div[2]/div[2]/div/div/div[1]/d#iv[19]/div[1]/div[2]/form/div[1]/span/span/select")
#size_element.click()


# click on the baby link
baby_link = driver.find_element("xpath","/html/body/div[1]/header/div/div[6]/div/a[7]/span")
# belt_link = driver.find_element("By.CSS_SELECTOR","span[data-component-type='s-product-image'] a")
baby_link.click()
time.sleep(4)

epic_link = driver.find_element("xpath","/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/div/div/div/div/div/div/a/img")
# belt_link = driver.find_element("By.CSS_SELECTOR","span[data-component-type='s-product-image'] a")
epic_link.click()
time.sleep(3)

tryprime = driver.find_element("xpath","/html/body/div[1]/div[2]/div[9]/div/div/button/span/span/div")
# belt_link = driver.find_element("By.CSS_SELECTOR","span[data-component-type='s-product-image'] a")
tryprime.click()
time.sleep(3)




# Selecting free returns 
#free_returns = driver.find_element("xpath","/html/body/div[1]/header/div/div[6]/div/a[10]/span/img")
# belt_link = driver.find_element("By.CSS_SELECTOR","span[data-component-type='s-product-image'] a")
#free_returns.click()



#clothingaccessorieslink = driver.find_element("xpath","/html/body/div[1]/div[2]/div[2]/div[3]/div/div/div/div/div/div/div/div/div/p[1]/a[1]")
# clothing_link = driver.find_element("By.CSS_SELECTOR","span[data-component-type='s-product-image'] a")
#clothingaccessorieslink.click()







# Waiting for the cart to update
time.sleep(5)

# Clicking on no thanks button
#no_thanks_button= #driver.find_element("xpath","/html/body/div[9]/div[3]/div[1]/div/div/div[2]/div[2]/div/div/div[3]/div/span#[2]/span/input")
#no_thanks_button.click()



#try prime = #driver.find_element("xpath","/html/body/div[2]/div[2]/div[5]/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/di#v[3]/div/div[1]/div/div[1]/div/div/div[1]/div/div[2]/div[9]/section/div/div/div[3]/span/span/a")
#try prime.click()
#time.sleep(5)





# Verifying that the laptop has been added to the cart
# cart_count = driver.find_element("id","nav-cart-count")
# assert cart_count.text == "1"
# cart_count.click()

# Closing the webdriver
driver.close()
