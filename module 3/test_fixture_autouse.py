# В данном примере “@pytest.fixture” — декоратор, указывающий, что функция ниже является фикстурой,
# “scope=’…’” указывает на “очерёдность” выполнения, а “autouse=True” говорит о том,
# что фикстура будет применена для каждого сьюта в тестовом фреймворке

import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.fixture(autouse=True)
def prepare_data():
    print()
    print("preparing some critical data for every test")


class TestMainPage1():
    def test_guest_should_see_login_link(self, browser):
        # не передаём как параметр фикстуру prepare_data, но она все равно выполняется
        browser.get(link)
        assert browser.find_element_by_css_selector("#login_link").text == "Hello"

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")