import time
from pages.login_page import LoginPage
from pages.home_page import HomePage


def test_is_this_login_page(browser):
    link = "https://hypeauditor.com/login/"
    page = LoginPage(browser, link)
    page.open_page()
    page.should_be_login_page()

def test_login(browser):
    link = "https://hypeauditor.com/login/"
    page = LoginPage(browser, link)
    page.open_page()
    page.input_correct_login()
    page.input_correct_password()
    page.click_login_button()
    time.sleep(2)
    home_page = HomePage(browser, browser.current_url)
    home_page.should_be_home_page()

def test_wrong_email(browser):
    link = "https://hypeauditor.com/login/"
    page = LoginPage(browser, link)
    page.open_page()
    page.input_wrong_email()
    page.input_correct_password()
    page.click_login_button()
    page.should_be_wrong_pass_warning()

def test_wrong_password(browser):
    link = "https://hypeauditor.com/login/"
    page = LoginPage(browser, link)
    page.open_page()
    page.input_correct_login()
    page.input_wrong_password()
    page.click_login_button()
    page.should_be_wrong_pass_warning()









