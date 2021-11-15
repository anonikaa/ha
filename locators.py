from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGO = (By.XPATH, "//a[@class='logo flex-shrink-0 header-logo']")
    LOGIN_BUTTON = (By.XPATH, "//a[contains(text(), 'Log in')]")


class LoginPageLocators:
    LOGIN_HEADER = (By.XPATH, "//h2[contains(text(), 'Log in to HypeAuditor')]")
    LOGIN_FIELD = (By.ID, "email")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON_IN_LOGIN_PAGE = (By.XPATH, "//div//button[@type='submit'][@class='button button-big button-block js-btn-loader'][@style='opacity: 1;']")
    WRONG_EMAIL_OR_PASSWORD = (By.XPATH, "//label[@class='hype-login-error fas-before']")

class HomePageLocators:
    SIDE_BAR_LOGO = (By.CLASS_NAME, "sidebar__logo-text")
    NPS_CLOSE = (By.CLASS_NAME, "g2__close")
    CM_MENU = (By.XPATH, "//a[@href='/campaign-management/']")
    DISCOVERY_MENU = (By.XPATH, "//div[text()='Influencer Discovery']")
    ACCOUNT_ICON = (By.CLASS_NAME, "profile__content")
    SETTINGS_DROPDOWN = (By.XPATH, "//a[@href='/settings']")


class SettingsPageLocators:
    SETTINGS_HEADER = (By.XPATH, "//h1[contains(text(), 'Settings')]")
    PLAN_INFO = (By.CLASS_NAME, "plan_info")
    PLAN_INFO_FREE = (By.XPATH, "//h3[contains(text(), 'Free plan')]")

class DiscoveryPageLocators:
    DISCOVERY_HEADER = (By.CLASS_NAME, "discovery-title")
    FILTERS_BUTTON = (By.ID, "discovery-filters--title")
    INFLUENCER_LOCATION_FILTER = (By.XPATH, "//input[@data-group-name='influencer_location']")
    CATEGORY_IG_FILTER = (By.XPATH, "///div[@class='select select-none select-multiple select--focus']//i[@class='far fa-angle-down select-arrow']")
    AlCOHOL_CATEGORY_IG = (By.XPATH, "//select[@id='influencer_category']//option[@value='1001']")
    USA_INFLUENCER_LOCATION_IG = (By.XPATH, "//li[contains(text(), 'United States')]")
    SHOW_RESULTS_BUTTON = (By.XPATH, "//button[@class='discovery__search-btn button button-big js-search-total']")
    SUBSCRIBE_BASIC_BUTTON = (By.XPATH, "//div[contains(text(), 'Subscribe')]")
    BASIC_AND_PRO_PAYWALL = (By.XPATH, "//div[contains(text(), 'Basic Plan + Instagram Discovery Pro')]")

class CMPageLocators:
    CM_LANDING = (By.CLASS_NAME, "container__content")
    CM_LIST = (By.CLASS_NAME, "mt-24")