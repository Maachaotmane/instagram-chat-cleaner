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

    # ✅ Function to scroll inside the chat
    def scroll_all_chats():
        scroll_box = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Chats' and @role='list']"))
        )
        last_height = 0
        while True:
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_box)
            delay(1, 2)
            new_height = driver.execute_script("return arguments[0].scrollTop", scroll_box)
            if new_height == last_height:
                break
            last_height = new_height

    scroll_all_chats()

    # ✅ Loop through chats
    while True:
        chats = driver.find_elements(By.XPATH, "//div[@aria-label='Chats']//div[@role='presentation']")
        if not chats:
            print("✅ No more chats to delete.")
            break

        for chat in chats:
            try:
                chat.click()

                # We will add it asap

                break

            except Exception as e:
                print(f"⚠️ Error deleting chat: {e}")
                break

finally:
    driver.quit()
