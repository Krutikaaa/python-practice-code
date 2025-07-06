import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get ("https://google.com")
driver.maximize_window()
time.sleep(2)

driver.get ("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID,"autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")
print(len(countries))

for country in countries:
    if country.text == "India":
        time.sleep(2)
        country.click()
        
        break

assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"
time.sleep(2)

driver.quit()