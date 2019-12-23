import unittest
from selenium import webdriver

class TestRegistration(unittest.TestCase):
    def setUp(self):
        browser = webdriver.Chrome(executable_path="C:\\chromedriver\\chromedriver.exe")
        # ждем загрузки страницы
        browser.implicitly_wait(5)
        self.browser = browser

    def fill_form(self, link):
        self.browser.get(link)

        input1 = self.browser.find_element_by_css_selector(".first_block > .first_class > .form-control")
        input1.send_keys("Ivan")
        input2 = self.browser.find_element_by_css_selector(".first_block > .second_class > .form-control")
        input2.send_keys("Petrov")
        input3 = self.browser.find_element_by_css_selector('.third')
        input3.send_keys("Petrov@test.ru")

        # Отправляем заполненную форму
        button = self.browser.find_element_by_css_selector("button.btn")
        button.click()

        # находим элемент, содержащий текст
        welcome_text_elt = self.browser.find_element_by_tag_name("h1")

        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        return welcome_text

    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"
        registration_result = self.fill_form(link)

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", registration_result, "registration is failed")

    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"  # -- вторая ссылка, падает NoSuchElementException
        registration_result = self.fill_form(link)

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", registration_result, "registration is failed")

    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()