
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os


#current_dir = os.path.abspath(os.path.dirname(r'D:\stscheck\temp'))
current_dir = os.path.abspath((r'D:\stscheck\temp')) #получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
# element.send_keys(file_path)
print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))

link = 'http://suninjuly.github.io/file_input.html'
try:
    chromedriver = "D:\chromedriver_win32\chromedriver.exe"
    browser = webdriver.Chrome(chromedriver)
    browser.get(link)

    first_name = browser.find_element_by_name("firstname")
    first_name.send_keys('ivan')
    last_name = browser.find_element_by_name("lastname")
    last_name.send_keys('pertov')
    email = browser.find_element_by_name("email")
    email.send_keys('ivan@email.com')

    myfile = browser.find_element_by_name('file')
    myfile.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    time.sleep(10)


finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

