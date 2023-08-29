from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

url = ''

## This part is for logging in the website
username = ''
password = ''

## Initiate the webdriver
chrome_driver_path = ''
driver = webdriver.Chrome(service=ChromeService(chrome_driver_path))
driver.get(url)
driver.find_element(By.NAME, "username").send_keys(username)
driver.find_element(By.NAME, "password").send_keys(password)
           
## Navigate and click the submit button
driver.find_element(By.CSS_SELECTOR, "div[class='blue_button ']").click()


## Get the webpage
driver.get(url)    
