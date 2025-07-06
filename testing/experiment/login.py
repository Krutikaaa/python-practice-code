""" Locaters  - ID, Xpath, CSSSelector, classname, name, linktext
     to identify elements on the page 
     inspect>> 
     Xpath = //tagname[@attribute='value']
     eg: //input[@type= 'submit]
     CSSSELECTOR = tagname[attribute='value']

     selectorshub - add that plugin it will automatically suggets epaths and cssselector
"""


import time
from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://github.com/login")
time.sleep(2)
driver.find_element(By.NAME, "login").send_keys("krutikabhise.427@gmail.com")
time.sleep(2)
driver.find_element(By.ID, "password").send_keys("Github@0427")
time.sleep(2)
submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
submit_button.click()
time.sleep(2)
print("login is sucessfull")

driver.quit()
'''
to verify success message popup 
message = driver.find_element(By.CLASS_NAME, '-------').text
print(message)
'''