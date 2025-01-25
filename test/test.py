import logging
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

chrome_options = Options()
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get('https://vk.com/')
driver.find_element(By.ID, 'index_email').send_keys('tkondrashin@icloud.com')
sleep(2)
driver.find_elements(By.CLASS_NAME, 'FlatButton__in')[-2].click()
# WebDriverWait(driver, 100).until(
#     ec.presence_of_element_located((By.CLASS_NAME, "ChatSettingsMembersWidget__more"))
# )
input()

driver.get('https://vk.com/im')
ca = []
for chat in driver.find_elements(By.CLASS_NAME, 'nim-dialog')[0:10]:
    chat.click()
    sleep(1)
    driver.find_element(By.CLASS_NAME, 'im-page--aside-photo').click()
    WebDriverWait(driver, 100).until(
        ec.presence_of_element_located((By.CLASS_NAME, "ChatSettingsMembersWidget__more"))
    )
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    driver.find_element(By.CLASS_NAME, 'ChatSettingsMembersWidget__more').click()


    ca_chat = []
    for people in driver.find_elements(By.CLASS_NAME, 'Entity__title')[1:-1]:
        href = people.find_element(By.TAG_NAME, 'a')
        print(href)
        name = people.find_element(By.TAG_NAME, 'a')
        print(name)
        ca_chat.append([href, name])
    ca.append(ca_chat)
print(ca)
