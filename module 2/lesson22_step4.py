import time

from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/selects1.html"

try:
    chromedriver = "D:\chromedriver_win32\chromedriver.exe"
    browser = webdriver.Chrome(chromedriver)
    browser.get(link)

    browser.execute_script("alert('Robots at work');")
    time.sleep(1)

    browser.execute_script("document.title='Script executing';")
    browser.execute_script('document.getElementsByName("h3")')
    time.sleep(10)

    button = browser.find_element_by_css_selector('.btn')
    button.click()

    # проверяем значение атрибута disabled у кнопки Submit после таймаута
    time.sleep(10)


finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
