from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_stealth import stealth
import undetected_chromedriver as uc
from seleniumbase import Driver
import time

# Writes to initialize Chrome with user-data-dir and a specific profile
def get_chrome_driver_with_profile(user_data_dir):
    # Creates Chrome options
    chrome_options = uc.ChromeOptions()

    # Sets the user data directory (where your session data will be stored)
    chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

    # Initializes the Chrome driver with WebDriver Manager
    # driver = uc.Chrome(headless=False, use_subprocess=False, options=chrome_options)

    # create a Driver instance with undetected_chromedriver (uc) and headless mode
    driver = Driver(uc=True, headless=False)

    # driver = webdriver.Chrome(
    #     service=Service(ChromeDriverManager().install()),
    #     options=chrome_options
    # )

    # stealth(driver,
    #         languages=["en-US", "en"],
    #         vendor="Google Inc.",
    #         platform="Win32",
    #         webgl_vendor="Intel Inc.",
    #         renderer="Intel Iris OpenGL Engine",
    #         fix_hairline=True,
    # )

    return driver


# Usage: Pass the path to the directory where Chrome should store the session data
driver = get_chrome_driver_with_profile("/home/amoraru/Documents/GitHub/CCS/session")


# navigate to the specified URL
driver.get("https://phishtank.org/phish_archive.php")

# pause execution for 20 seconds
driver.sleep(20)

# take a screenshot of the current page and save it
driver.save_screenshot("datacamp.png")

# close the browser and end the session
driver.quit()

# Now you can open websites, and the session data will persist across executions.

# driver.get("https://phishtank.org/phish_archive.php")
# time.sleep(1000)
# driver.quit()
