#pytest -s  test_fixture2.py --tb=line

import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def mbrowser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    return browser


class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, mbrowser):
        mbrowser.get(link)
        mbrowser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, mbrowser):
        mbrowser.get(link)
        mbrowser.find_element_by_css_selector(".basket-mini .btn-group > a")