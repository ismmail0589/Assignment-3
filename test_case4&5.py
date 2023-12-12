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



#test case 4 login for admin

driver.get('http://3.110.191.61/admin/login.php')
driver.maximize_window()

driver.find_element(By.XPATH, '//input[@name="admin_username"]').send_keys('admin@gmail.com')

driver.find_element(By.XPATH, '//input[@name="password"]').send_keys('123456789')
time.sleep(3)
driver.find_element(By.XPATH, '//input[@id="signin"]').click()

time.sleep(10)


#test case 5 delete user
driver.find_element(By.XPATH, '//a[@href="manageuser.php"]').click()
time.sleep(10)

driver.find_element(By.XPATH, '//a[@href="manageuser.php?user_id=1&action=delete"]').click()
