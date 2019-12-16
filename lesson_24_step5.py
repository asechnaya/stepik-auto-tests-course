from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12*math.sin(x))))
try:
    browser = webdriver.Chrome()#(executable_path='C:\chromedriver\chromedriver.exe')

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 12 секунд, пока не будет нужной цены
    price = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    if price == True:
        button = browser.find_element_by_id("book")
        button.click()

        x = browser.find_element_by_id("input_value")
        x_value = int(x.text)
        y = calc(x_value)

        answer = browser.find_element_by_id("answer")
        answer.send_keys(y)
        button = browser.find_element_by_id("solve")
        button.click()

        alert = browser.switch_to.alert
        magic_num = alert.text
        magic_num = magic_num.split(": ")
        magic_num =(magic_num[1])
        alert.accept()

finally:
    browser.quit()
    print(magic_num)