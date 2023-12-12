from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Chrome Options
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Initialize Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# test case 1 signup for user 
driver.get('http://3.110.191.61/signup_form.php')
driver.maximize_window()

driver.find_element(By.XPATH, '//input[@name="f_name"]').send_keys('aa')
driver.find_element(By.XPATH, '//input[@name="l_name"]').send_keys('bb')
driver.find_element(By.XPATH, '//input[@name="email"]').send_keys('abc@gmail.com')
driver.find_element(By.XPATH, '//input[@name="mobile"]').send_keys('12345678900')
driver.find_element(By.XPATH, '//input[@name="password"]').send_keys('!abc12345')
driver.find_element(By.XPATH, '//input[@name="repassword"]').send_keys('!abc12345')
driver.find_element(By.XPATH, '//input[@name="address1"]').send_keys('h#234')
driver.find_element(By.XPATH, '//input[@name="address2"]').send_keys('RWP')
driver.find_element(By.XPATH, '//label[@class="label-checkbox100"]').click()
time.sleep(3)
driver.find_element(By.XPATH, '//button[@class="login100-form-btn"]').click()










