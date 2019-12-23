from selenium import webdriver
import time

try:
    # chromedriver = "C:\chromedriver\chromedriver.exe" -- у меня не прописывается в переменные среды гуглхром
    # (не известно почему, поэтому я просто оставила закомменченную ссылку
    # browser = webdriver.Chrome(executable_path=chromedriver)
    # link = "http://suninjuly.github.io/registration1.html"   # -- первоначальная ссылка
    link = "http://suninjuly.github.io/registration2.html"  # -- вторая ссылка, падает NoSuchElementException
    browser = webdriver.Chrome()

    browser.get(link)

    input1 = browser.find_element_by_css_selector(".first_block > .first_class > .form-control")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector(".first_block > .second_class > .form-control")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector('.third')
    input3.send_keys("Petrov@test.ru")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()