import time
from selenium import webdriver
from selenium.webdriver.common.by import By

name = "Krutika"
driver = webdriver.Chrome()
driver.get ("https://google.com")
driver.maximize_window()
time.sleep(2)

driver.get ("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.ID,"alertbtn").click()
time.sleep(2)
# switch to alert mode to read the alert mesage 
alert = driver.switch_to.alert
time.sleep(2)
alert_text = alert.text
print(alert_text)
# can use dismis() to reject the alert or accept() to accept the alert
alert.accept()

assert name in alert_text
driver.close()