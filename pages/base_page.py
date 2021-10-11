#описали базовые методы веб-страницы, которые можно использовать в других классах
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from locators import BasePageLocators
from locators import HomePageLocators

class BasePage:

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

#открытие страницы
    def open_page(self):
        self.browser.get(self.url)


#проверка на то, что элемент есть
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

#закрываем nps скор, чтобы он не перекрывал элементы
    def close_nps(self): #здесь надо переписать на то, что если элемент покажется - закрыть его, если нет, то просто скип
        nps_close = self.browser.find_element(*HomePageLocators.NPS_CLOSE)
        nps_close.click()


    # def ourIP_on(self):




