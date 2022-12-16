from selenium import webdriver
import time 
import chromedriver_autoinstaller
from pyvirtualdisplay import Display


chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

browser = webdriver.Chrome()

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
