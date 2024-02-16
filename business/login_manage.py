from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from setting import *


class LoginManager:
    _instance = None

    def __new__(cls, driver):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.driver = driver
            cls._instance.login()
        return cls._instance

    @classmethod
    def login(cls):
        cls._instance.driver.get(PHARMAOS_URL)
        username_locator = ('id', 'account')
        password_locator = ('id', 'password')
        login_btn_locator = ('xpath', '//*[@id="rc-tabs-0-panel-password"]/form/div[3]/div/div/div/div/button')
        cls._instance.driver.find_element(*username_locator).send_keys(USERNAME)
        cls._instance.driver.find_element(*password_locator).send_keys(PASSWORD)
        cls._instance.driver.find_element(*login_btn_locator).click()
        WebDriverWait(cls._instance.driver, 20).until(EC.title_contains('首页'))
