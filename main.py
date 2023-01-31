from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

DRIVER_PATH = "path/to/chrome/driver"
SIMILAR_ACCOUNT = "buzzfeedtasty"
USERNAME = "your_username"
PASSWORD = "your_password"

def wait_until_clickable(driver, selector):
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
    except:
        return False
    return True

def follow_instagram_followers():
    driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(5)
    
    # Login to Instagram
    username = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")
    username.send_keys(USERNAME)
    password.send_keys(PASSWORD)
    password.send_keys(Keys.ENTER)
    time.sleep(5)
    
    # Go to similar account's followers
    driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")
    time.sleep(2)
    followers_link = driver.find_element_by_css_selector("a[href$='followers/']")
    followers_link.click()
    time.sleep(2)
    
    # Scroll through followers modal
    modal = driver.find_element_by_css_selector("div[role='dialog']")
    for i in range(10):
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
        time.sleep(2)
    
    # Follow followers
    follow_buttons = driver.find_elements_by_css_selector("button[type='button']")
    for button in follow_buttons:
        if button.text == "Follow":
            if wait_until_clickable(driver, "button[type='button']"):
                button.click()
                time.sleep(1)
    
    driver.close()

follow_instagram_followers()