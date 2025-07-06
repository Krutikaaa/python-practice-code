import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get ("https://google.com")
driver.maximize_window()
time.sleep(2)

driver.get ("https://rahulshettyacademy.com/AutomationPractice/")
radiobutton = driver.find_elements( By.CSS_SELECTOR, ".radioButton")
radiobutton[2].click()
time.sleep(2)
print(radiobutton[2])
assert radiobutton[2].is_selected()


assert driver.find_element(By.ID,"displayed-text").is_displayed()
driver.find_element(By.ID,"hide-textbox").click()
assert not driver.find_element(By.ID,"displayed-text").is_displayed()
driver.quit()