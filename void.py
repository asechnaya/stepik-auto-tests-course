import time 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

chrome_options = Options()
options = [
    "--headless",
    "--disable-gpu",
    "--window-size=1920,1200",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage"
]
for option in options:
    chrome_options.add_argument(option)

browser = webdriver.Chrome(service=chrome_service, options=chrome_options)

link = "http://suninjuly.github.io/simple_form_find_task.html"
browser.get(link)
print(browser.title)
# input1 = browser.find_element_by_tag_name(value1)
# input1.send_keys("Ivan")
# input2 = browser.find_element_by_name(value2)
# input2.send_keys("Petrov")
# input3 = browser.find_element_by_class_name(value3)
# input3.send_keys("Smolensk")
# input4 = browser.find_element_by_id(value4)
# input4.send_keys("Russia")
button = browser.find_element_by_css_selector("button.btn")
button.click()
time.sleep(30)
browser.quit()
