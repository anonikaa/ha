from pages.home_page import HomePage
from pages.discovery_page import DiscoveryPage
from pages.login_page import LoginPage
from pages.settings_page import SettingsPage
from credentials import Links
import time

def test_it_is_free_account(browser):
    link = Links.login_link
    page = LoginPage(browser, link)
    page.open_page()
    page.login_free_account()
    time.sleep(2)
    home_page = HomePage(browser, browser.current_url)
    home_page.go_to_account_settings()
    settings_page = SettingsPage(browser, browser.current_url)
    time.sleep(2)
    # settings_page.should_be_settings_page()
    settings_page.should_be_free_account()

def test_basic_paywall(browser):
    link = Links.login_link
    page = LoginPage(browser, link)
    page.open_page()
    page.login_free_account()
    time.sleep(1)
    home_page = HomePage(browser, browser.current_url)
    home_page.go_to_discovery()
    discovery_page = DiscoveryPage(browser, browser.current_url)
    # discovery_page.should_be_discovery_page()
    discovery_page.click_filters_button()
    discovery_page.choose_category_filter_ig()
    time.sleep(5)


def test_basic_and_pro_paywall_ig(browser):
    link = Links.login_link
    page = LoginPage(browser, link)
    page.open_page()
    page.login_free_account()
    time.sleep(1)
    home_page = HomePage(browser, browser.current_url)
    home_page.go_to_discovery()
    discovery_page = DiscoveryPage(browser, browser.current_url)
    # discovery_page.should_be_discovery_page()
    discovery_page.click_filters_button()
    discovery_page.choose_influencer_location_filter_ig()
    discovery_page.click_show_results_button()
    time.sleep(1)
    discovery_page.should_be_subscribe_button_on_free_account()
    discovery_page.click_on_subscribe_basic_button()
    time.sleep(1)
    discovery_page.basic_and_pro_paywall()






