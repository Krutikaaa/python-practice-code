# Python + Selenium Interview Problem Statements with Solutions

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import requests

# *******1. Login Automation
def login_automation():
    driver = webdriver.Chrome()
    driver.get("https://example.com/login")
    driver.find_element(By.ID, "username").send_keys("myuser")
    driver.find_element(By.ID, "password").send_keys("mypassword")
    driver.find_element(By.ID, "login-btn").click()
    assert "dashboard" in driver.current_url
    driver.quit()

# 2. Dynamic Table Data Extraction
def table_data_extraction():
    driver = webdriver.Chrome()
    driver.get("https://example.com/table")
    rows = driver.find_elements(By.XPATH, "//table[@id='data']//tr")
    for row in rows:
        cols = row.find_elements(By.TAG_NAME, "td")
        for col in cols:
            print(col.text)
    cell = driver.find_element(By.XPATH, "//table[@id='data']/tbody/tr[3]/td[2]")
    print("Specific cell:", cell.text)
    driver.quit()

# 3. Handle Multiple Windows/Tabs*******
def handle_multiple_windows():
    driver = webdriver.Chrome()
    driver.get("https://example.com")
    driver.find_element(By.LINK_TEXT, "Open New").click()
    windows = driver.window_handles
    driver.switch_to.window(windows[1])
    print("New Tab Title:", driver.title)
    driver.switch_to.window(windows[0])
    print("Back to Main:", driver.title)
    driver.quit()

# 4. Waits and Synchronization*****
def wait_example():
    driver = webdriver.Chrome()
    driver.get("https://example.com/delay")
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.visibility_of_element_located((By.ID, "delayed-content")))
    print("Content:", element.text)
    driver.quit()

# 5. File Upload********* 

def file_upload():
    driver = webdriver.Chrome()
    driver.get("https://example.com/upload")
    file_path = os.path.abspath("sample_file.txt")
    driver.find_element(By.ID, "file-upload").send_keys(file_path)
    driver.find_element(By.ID, "upload-btn").click()
    print("File uploaded!")
    driver.quit()

# 6. Search and Validate
def search_validation():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium automation")
    search_box.submit()
    driver.implicitly_wait(5)
    results = driver.find_elements(By.XPATH, "//h3")
    assert any("Selenium" in r.text for r in results)
    driver.quit()

# 7. Form Submission*&+*****
def form_submission():
    driver = webdriver.Chrome()
    driver.get("https://example.com/form")
   

    driver.find_element(By.NAME, "name").send_keys("John")
    driver.find_element(By.NAME, "email").send_keys("john@example.com")
    driver.find_element(By.ID, "submit").click()
    message = driver.find_element(By.ID, "success").text
    title2=driver.getTitle()
    title="Home Page"
    assert title2.equals(title)

    assert "Thank you" in message
    driver.quit()

# 8. Dropdown and Radio Button
def dropdown_radio():
    driver = webdriver.Chrome()
    driver.get("https://example.com/dropdown")
    dropdown = Select(driver.find_element(By.ID, "cars"))
    dropdown.select_by_visible_text("Audi")
    radio = driver.find_element(By.ID, "gender-male")
    radio.click()
    assert radio.is_selected()
    driver.quit()

# 9. Web Table Sorting
def table_sorting():
    driver = webdriver.Chrome()
    driver.get("https://example.com/table")
    driver.find_element(By.XPATH, "//th[text()='Name']").click()
    names = driver.find_elements(By.XPATH, "//tr/td[1]")
    name_list = [n.text for n in names]
    assert name_list == sorted(name_list)
    driver.quit()

# 10. Screenshot on Failure**************
def screenshot_on_failure():
    driver = webdriver.Chrome()
    driver.get("https://example.com")
    try:
        element = driver.find_element(By.ID, "not-exist")
    except Exception as e:
        driver.save_screenshot("error_screenshot.png")
        print("Screenshot saved due to failure:", e)
    driver.quit()

# 11. Scroll to Element
def scroll_to_element():
    driver = webdriver.Chrome()
    driver.get("https://example.com/scroll")
    target = driver.find_element(By.ID, "footer")
    driver.execute_script("arguments[0].scrollIntoView(true);", target)
    driver.quit()

# 12. Mouse Hover*********
def mouse_hover():
    driver = webdriver.Chrome()
    driver.get("https://example.com/menu")
    menu = driver.find_element(By.ID, "products")
    sub_menu = driver.find_element(By.ID, "new-product")
    ActionChains(driver).move_to_element(menu).click(sub_menu).perform()
    driver.quit()

# 13. Handle Stale Element
def handle_stale_element():
    driver = webdriver.Chrome()
    driver.get("https://example.com/refresh")
    try:
        button = driver.find_element(By.ID, "submit")
        driver.refresh()
        time.sleep(2)
        button.click()
    except:
        button = driver.find_element(By.ID, "submit")
        button.click()
    driver.quit()

# 14. Broken Link Checker
def broken_link_checker():
    driver = webdriver.Chrome()
    driver.get("https://example.com")
    links = driver.find_elements(By.TAG_NAME, "a")
    for link in links:
        url = link.get_attribute("href")
        if url:
            try:
                response = requests.head(url, timeout=5)
                if response.status_code >= 400:
                    print(f"Broken link: {url}")
            except requests.exceptions.RequestException:
                print(f"Error checking: {url}")
    driver.quit()

# 15. Full Page Screenshot
def full_page_screenshot():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get("https://example.com")
    driver.get_screenshot_as_file("full_page.png")
    driver.quit()
