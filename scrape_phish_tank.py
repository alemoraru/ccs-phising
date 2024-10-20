from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get('https://phishtank.com/phish_archive.php')

links = driver.find_elements(By.CLASS_NAME, 'small')

print(len(links))

# for link in links:
#     if link.text == 'See all reviews':
#         link.click()
#         print(link.text)
# WebDriverWait(driver, 10).until(ES.visibility_of_element_located((By.CSS_SELECTOR, "div.odk6He")))
# # time.sleep(2)
# container = driver.find_element(By.CSS_SELECTOR, "div.odk6He")
# # driver.execute_script("document.querySelector('div.odk6He').scrollTop = 1000")
#
# counter = 0
#
# styles = driver.find_elements(By.XPATH, '//tr[@style="background: #ffffff;"]')
#
# for style in styles:
#     for i in range(2):
#         a = style.find_element(By.XPATH, '//td[@class="value"]/a').get_attribute("href")
#         b = style.find_element(By.XPATH, '//td[@class="value"]').text
#
#         with open('Data.csv', 'a', encoding='UTF-8', newline='') as f:
#             csv.writer(f).writerow([a, b])
#
#         print(a)
#
# actions = ActionChains(driver)
# actions.move_to_element(contaner_elements[-1:][0]).perform()
# input()
