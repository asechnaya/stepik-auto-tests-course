from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    chromedriver = "C:\chromedriver\chromedriver.exe"
    browser = webdriver.Chrome(executable_path=chromedriver)
    link = "http://suninjuly.github.io/wait1.html"
    # browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)


    button = browser.find_element_by_id("verify")
    button.click()
    message = browser.find_element_by_id("verify_message")

    assert "successful" in message.text

    # Отправляем заполненную форму


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
