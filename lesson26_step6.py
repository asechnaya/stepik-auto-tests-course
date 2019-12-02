from selenium import webdriver
import time

try:
    chromedriver = "D:\chromedriver_win32\chromedriver.exe"
    browser = webdriver.Chrome(chromedriver)
    browser.get("http://suninjuly.github.io/registration1.html")
    elements = browser.find_elements_by_tag_name("input")
    for element in elements:
       element.send_keys("Мой ответ")
    button = browser.find_element_by_xpath('//button[text()="Submit"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла