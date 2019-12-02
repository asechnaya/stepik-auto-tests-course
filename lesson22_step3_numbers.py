
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/selects2.html"

try:
    chromedriver = "D:\chromedriver_win32\chromedriver.exe"
    browser = webdriver.Chrome(chromedriver)
    browser.get(link)

    num1 = browser.find_element_by_id("num1").text
    num2 = browser.find_element_by_id("num2").text

    print(f'num1 = {num1}, num2 ={num2}')

# выбираем ответ из выпадающего меню
    y = str(int(num1) + int(num2))
    print(y)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(y)


    button = browser.find_element_by_css_selector('.btn')
    button.click()


    # проверяем значение атрибута disabled у кнопки Submit после таймаута
    time.sleep(10)


finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла