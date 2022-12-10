import time
import math
import pytest
from selenium import webdriver



links_list = ['https://stepik.org/lesson/236895/step/1',
              'https://stepik.org/lesson/236896/step/1',
              'https://stepik.org/lesson/236897/step/1',
              'https://stepik.org/lesson/236898/step/1',
              'https://stepik.org/lesson/236899/step/1',
              'https://stepik.org/lesson/236903/step/1',
              'https://stepik.org/lesson/236904/step/1',
              'https://stepik.org/lesson/236905/step/1']

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link', links_list)
def test_guest_should_see_login_link(browser, link):
    print(f'{link}')
    url = link
    browser.get(url)
    answer = str(math.log(int(time.time())))
    print(answer)
    input1 = browser.find_element_by_css_selector(".textarea")
    input1.send_keys(answer)
    btn = browser.find_element_by_tag_name("button")
    btn.click()
    msg = browser.find_element_by_class_name("smart-hints__hint").text
    assert msg == 'Correct!'
