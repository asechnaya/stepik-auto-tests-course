from selenium import webdriver
import time 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller
from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 800))  
display.start()

chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

chrome_options = webdriver.ChromeOptions()    
# Add your options as needed    
options = [
  # Define window size here
   "--window-size=1200,1200",
    "--ignore-certificate-errors"
 
    #"--headless",
    #"--disable-gpu",
    #"--window-size=1920,1200",
    #"--ignore-certificate-errors",
    #"--disable-extensions",
    #"--no-sandbox",
    #"--disable-dev-shm-usage",
    #'--remote-debugging-port=9222'
]

for option in options:
    chrome_options.add_argument(option)

    
browser = webdriver.Chrome(options = chrome_options)

link = "http://suninjuly.github.io/simple_form_find_task.html"
browser.get(link)

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
