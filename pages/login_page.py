import time
from .base_page import BasePage
from .home_page import HomePage
from locators import LoginPageLocators, HomePageLocators
from credentials import Credentionals


class LoginPage(BasePage):

    def login_empty_cm_mp(self):
        login_field = self.browser.find_element(*LoginPageLocators.LOGIN_FIELD)
        login_field.click()
        login_field.send_keys(Credentionals.login_empty_cm)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password_field.click()
        password_field.send_keys(Credentionals.password_empty_cm)
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON_IN_LOGIN_PAGE)
        time.sleep(1)
        login_button.click()
        return HomePage(browser=self.browser, url=self.browser.current_url)

    def login_free_account(self):
        login_field = self.browser.find_element(*LoginPageLocators.LOGIN_FIELD)
        login_field.click()
        login_field.send_keys(Credentionals.login_free)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password_field.click()
        password_field.send_keys(Credentionals.password_free)
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON_IN_LOGIN_PAGE)
        time.sleep(1)
        login_button.click()
        return HomePage(browser=self.browser, url=self.browser.current_url)


    def should_be_login_page(self):
        time.sleep(1)
        assert self.is_element_present(*LoginPageLocators.LOGIN_HEADER), "This is not login page"

    def input_correct_login(self):
        login_field = self.browser.find_element(*LoginPageLocators.LOGIN_FIELD)
        login_field.click()
        login_field.send_keys(Credentionals.login_free)

    def input_correct_password(self):
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password_field.click()
        password_field.send_keys(Credentionals.password_free)
        time.sleep(1)

    def click_login_button(self):
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON_IN_LOGIN_PAGE)
        login_button.click()
        return HomePage(browser=self.browser, url=self.browser.current_url)

    def should_be_home_page(self):
        time.sleep(1)
        assert self.is_element_present(*HomePageLocators.SIDE_BAR_LOGO), "NOOO"

    def input_wrong_email(self):
        login_field = self.browser.find_element(*LoginPageLocators.LOGIN_FIELD)
        login_field.click()
        login_field.send_keys(Credentionals.wrong_login)

    def input_wrong_password(self):
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password_field.click()
        password_field.send_keys(Credentionals.wrong_password)
        time.sleep(1)

    def should_be_wrong_pass_warning(self):
        time.sleep(1)
        assert self.is_element_present(*LoginPageLocators.WRONG_EMAIL_OR_PASSWORD), "warning doesn't show"







