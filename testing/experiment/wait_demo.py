''' write a testcase that will hit the given site search a word in search bar and 
will add all the result in card then apply the discount and place the order
'''


import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get ("https://google.com")
driver.maximize_window()
time.sleep(2)

driver.get ("https://rahulshettyacademy.com/seleniumPractise/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)

results = driver.find_elements(By.XPATH, "//div[@class='products']/div")    
count = len(results)
assert count > 0
assert count == 3
#  chnaining of the web elements
for result in results:
    result.find_element(By.XPATH, "div/button").click()
    time.sleep(2)

driver.close()