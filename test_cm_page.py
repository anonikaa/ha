import time

from pages.cm_page import CMPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from credentials import Links

def test_show_mini_landing_cm(browser):
    link = Links.login_link
    page = LoginPage(browser, link)
    page.open_page()
    page.login_empty_cm_mp()
    home_page = HomePage(browser, browser.current_url)
    time.sleep(1) #здесь надо переписать на явное ожидание
    home_page.close_nps()
    home_page.go_to_cm_page()
    cm_page = CMPage(browser, browser.current_url)
    cm_page.should_be_cm_mini_landing()

def test_show_lists_of_campaings(browser):
    link = Links.login_link
    page = LoginPage(browser, link)
    page.open_page()
    page.login_free_account()
    home_page = HomePage(browser, browser.current_url)
    time.sleep(1)
    home_page.go_to_cm_page()
    cm_page = CMPage(browser, browser.current_url)
    time.sleep(1)
    cm_page.should_be_cm_list()


