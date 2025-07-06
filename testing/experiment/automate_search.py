# This will automate search on google.com
'''
search a word retrive all the elements in the dropdown  use a for loop to iterate and it will 
select the element that matches the search word and click on it
create a common cssselector for all the dropdown options
check lect no 42
'''
import time
from selenium import webdriver
# from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get ("https://google.com")
driver.maximize_window()
time.sleep(2)
search_box = driver.find_element(By.NAME,"q").send_keys("spotify")
time.sleep(5)

search_box.send_keys(Keys.RETURN)
assert "spotify" in driver.title, "Test Failed: Title does not contain 'spotify'"
time.sleep(10)
print("Test Passed: Wikipedia search is working correctly")
driver.quit()