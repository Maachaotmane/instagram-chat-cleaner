from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

USERNAME = "your_username"
PASSWORD = "your_password"

def delay(min_=2, max_=4):
    time.sleep(random.uniform(min_, max_))

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=options)

try:
    # ✅ Login
    driver.get("https://www.instagram.com/accounts/login/")
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "username")))
    driver.find_element(By.NAME, "username").send_keys(USERNAME)
    driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)

    # ✅ Go to Inbox
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/direct/inbox/')]"))
    )
    driver.get("https://www.instagram.com/direct/inbox/")

finally:
    driver.quit()
