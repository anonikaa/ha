import time
from selenium.webdriver.common.action_chains import ActionChains
from .base_page import BasePage
from .locators import HomePageLocators

class HomePage(BasePage):

    def should_be_home_page(self):
        time.sleep(1)
        assert self.is_element_present(*HomePageLocators.SIDE_BAR_LOGO), "NOOO"

    def go_to_account_settings(self):
        avatar = self.browser.find_element(*HomePageLocators.ACCOUNT_ICON)
        account_settings = self.browser.find_element(*HomePageLocators.SETTINGS_DROPDOWN)
        # create action chain object
        action = ActionChains(self.browser)
        # perform the operation
        action.move_to_element(avatar).click().perform()
        time.sleep(1)
        action.move_to_element(account_settings).click().perform()

    def go_to_discovery(self):
        discovery_menu = self.browser.find_element(*HomePageLocators.DISCOVERY_MENU)
        discovery_menu.click()


    def go_to_cm_page(self):
        cm_menu = self.browser.find_element(*HomePageLocators.CM_MENU)
        cm_menu.click()
