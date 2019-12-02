
from selenium import webdriver
import math, time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    chromedriver = "D:\chromedriver_win32\chromedriver.exe"
    browser = webdriver.Chrome(chromedriver)
    browser.get(link)

#ищем сокровище
    treasure = browser.find_element_by_id("treasure")
    x_element = treasure.get_attribute("valuex")
    print("value of x: ", x_element)
    assert x_element is not None, "People radio is not selected by default"

    x = x_element
    y = calc(x)

    y_element = browser.find_element_by_id('answer')
    y_element.send_keys(y)


    # проверяем значение атрибута checked у robots_radio
    robots_radio = browser.find_element_by_id("robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    print("value of robots_radio: ", robots_checked)
    assert robots_checked is None
    robots_radio.click()

    time.sleep(2)

    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()

    # проверяем значение атрибута disabled у кнопки Submit
    button = browser.find_element_by_css_selector('.btn')
    button.click()


    # проверяем значение атрибута disabled у кнопки Submit после таймаута
    time.sleep(10)


finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла