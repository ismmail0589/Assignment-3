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


# test case 2 signin for user
driver.get('http://3.110.191.61/signin_form.php')
driver.maximize_window()

driver.find_element(By.XPATH, '//input[@name="email"]').send_keys('abc@gmail.com')

driver.find_element(By.XPATH, '//input[@name="password"]').send_keys('!abc12345')
driver.find_element(By.XPATH, '//label[@class="label-checkbox100"]').click()
time.sleep(3)
driver.find_element(By.XPATH, '//button[@class="login100-form-btn"]').click()
time.sleep(2)

#test case 3 add to cart

driver.find_element(By.XPATH, '//a[@href="products.php?cat_id=1"]').click()
time.sleep(5)

driver.find_element(By.XPATH, '//div[@class="product-img"]').click()
time.sleep(2)

driver.find_element(By.XPATH, '//button[@class="add-to-cart-btn"]').click()
