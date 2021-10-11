from .base_page import BasePage
from locators import SettingsPageLocators


class SettingsPage(BasePage):

    def should_be_settings_page(self):
        assert self.is_element_present(*SettingsPageLocators.SETTINGS_HEADER), "wrong"

    def should_be_free_account(self):
        assert self.is_element_present(*SettingsPageLocators.PLAN_INFO_FREE), "is not free"