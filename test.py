import time
import logging

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

# Настройки драйвера
chrome_options = Options()
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--headless")

chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("--use-fake-ui-for-media-stream") # адская тема радар включает на вебке
# chrome_options.add_argument("--use-fake-device-for-media-stream") # и звук радара на микро
chrome_options.add_argument("--disable-notification")
chrome_options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 2,
    "profile.default_content_setting_values.media_stream_camera": 2,
    "profile.default_content_setting_values.geolocation": 2,
    "profile.default_content_setting_values.notifications": 2
  })

chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.get('https://my.mts-link.ru/19570345/376475802')
WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CLASS_NAME, "modal-content")))
window = driver.find_element(By.CLASS_NAME, 'modal-content')
window.find_element(By.CLASS_NAME, 'input-field').click()
window.find_element(By.ID, 'name').send_keys('')
window.find_element(By.CLASS_NAME, 'btn-important').click()
WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, "prepare-vcs")))
window = driver.find_element(By.ID, 'prepare-vcs')
window.find_element(By.CLASS_NAME, 'btn_material').click()
time.sleep(5400)