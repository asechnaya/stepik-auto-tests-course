import time 
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)


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
