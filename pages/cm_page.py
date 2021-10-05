import time

from pages.base_page import BasePage
from pages.locators import CMPageLocators



class CMPage(BasePage):
    def should_be_cm_mini_landing(self):
        time.sleep(1)
        assert self.is_element_present(*CMPageLocators.CM_LANDING), "No landing("


    def should_be_cm_list(self):
       time.sleep(1)
       assert self.is_element_present(*CMPageLocators.CM_LIST), "Have no campaign or it's not cm"

