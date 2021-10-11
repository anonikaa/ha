import time
from pages.base_page import BasePage
from locators import DiscoveryPageLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class DiscoveryPage(BasePage):

    def should_be_discovery_page(self):
        assert self.is_element_present(*DiscoveryPageLocators.DISCOVERY_HEADER), "it is not discovery page"

    def click_filters_button(self):
        filters_button = self.browser.find_element(*DiscoveryPageLocators.FILTERS_BUTTON)
        filters_button.click()

    def choose_category_filter_ig(self):
        category_ig_field = self.browser.find_element(*DiscoveryPageLocators.CATEGORY_IG_FILTER)
        category_ig_field.click
        alcohol_category_ig = self.browser.find_element(*DiscoveryPageLocators.AlCOHOL_CATEGORY_IG)
        action = ActionChains(self.browser)
        action.move_to_element(alcohol_category_ig).click().perform()



    def choose_influencer_location_filter_ig(self):
        influencer_location_ig_field = self.browser.find_element(*DiscoveryPageLocators.INFLUENCER_LOCATION_FILTER)
        time.sleep(1)
        influencer_location_ig_field.click()
        influencer_location_ig_field.send_keys("usa")
        time.sleep(1)
        usa_influencer_location_ig = self.browser.find_element(*DiscoveryPageLocators.USA_INFLUENCER_LOCATION_IG)
        action = ActionChains(self.browser)
        action.move_to_element(usa_influencer_location_ig).click().perform()

    def click_show_results_button(self):
        show_results_button = self.browser.find_element(*DiscoveryPageLocators.SHOW_RESULTS_BUTTON)
        show_results_button.click()

    def should_be_subscribe_button_on_free_account(self):
        assert self.is_element_present(*DiscoveryPageLocators.SUBSCRIBE_BASIC_BUTTON), "subscribe button is not present"

    def click_on_subscribe_basic_button(self):
        subscribe_button = self.browser.find_element(*DiscoveryPageLocators.SUBSCRIBE_BASIC_BUTTON)
        subscribe_button.click()

    def basic_and_pro_paywall(self):
        assert self.is_element_present(*DiscoveryPageLocators.BASIC_AND_PRO_PAYWALL), "basic+pro paywall doesn't show"




