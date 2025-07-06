import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get ("https://github.com/Krutikaaa/")
driver.maximize_window()
time.sleep(2)
print (driver.title)
print(driver.current_url)


# service -  for connecting to a driver that is older or using VPN 
# install it manumally with service class
# sevice_obj = Service("path for downloaded deriver")
# webdriver/chrome(service = sevice_obj)