import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
    # self.driver.find_element(By.XPATH, "//form/div[contains(@tag, 'button')]/button[text()='Submit']").click()


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_xpath_form")
    browser.find_element(By.XPATH, "//input[@name=\'first_name\']").send_keys("ivan")
    browser.find_element(By.XPATH, "//input[@name=\'last_name\']").send_keys("petrov")
    browser.find_element(By.XPATH, "//div[3]/input").send_keys("Novgorod")
    browser.find_element(By.XPATH, "//input[@id=\'country\']").send_keys("rus")
    button = browser.find_element_by_xpath('//button[text()="Submit"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла