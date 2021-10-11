import time
from pages.main_page import MainPage
from pages.login_page import LoginPage
from locators import BasePageLocators
from credentials import Links

def test_should_be_logo(browser):
    link = Links.landing_link
    dashboard_page = MainPage(browser, link)
    dashboard_page.open_page()
    assert dashboard_page.is_element_present(*BasePageLocators.LOGO), "Logo is not presented" #если не найдёт лого, напишет


def test_go_to_login_page_from_dashboard(browser):
    link = Links.landing_link
    dashboard_page = MainPage(browser, link)
    dashboard_page.open_page()
    login_button = browser.find_element(*BasePageLocators.LOGIN_BUTTON)
    login_button.click()
    time.sleep(3)
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()





