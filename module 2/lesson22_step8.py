from selenium import webdriver
import math
import time
import os

current_dir = os.path.abspath(os.path.dirname(r'D:\stscheck\temp'))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')                      # добавляем к этому пути имя файла
element.send_keys(file_path)
print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    chromedriver = "D:\chromedriver_win32\chromedriver.exe"
    browser = webdriver.Chrome(executable_path=chromedriver)
    link = "http://suninjuly.github.io/execute_script.html"

    browser.get(link)

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    browser.execute_script("window.scrollBy(0, 100);")

    y_element = browser.find_element_by_id('answer')
    y_element.send_keys(y)

    option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    option1.click()

    option1 = browser.find_element_by_css_selector("[for='robotsRule']")
    option1.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
