from typing import Union
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from basic.exceptions import ElementNotExistsError
from business.login_manage import LoginManager


class Page:
    url = None
    driver = None

    def __init__(self, driver):
        self.driver = driver
        LoginManager(self.driver)

    def get(self):
        self.driver.get(self.url)

    def element(self, loc):
        """ 如果没有返回任何参数， 就返回一个None """
        try:
            return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(loc))
        except TimeoutException as e:
            raise ElementNotExistsError(e)

    def elements(self, loc):
        """ 如果没有返回任何参数列表， 就返回一个None"""
        try:
            return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(loc))
        except TimeoutException as e:
            raise ElementNotExistsError(e)

    def select(self, loc: tuple, params: Union[int, str], max_index: int = 10):
        """  模仿select组件 """
        if isinstance(params, int):
            return self.elements(loc)[min(params, max_index)]

        elements = self._select_by_text(loc)
        if params not in elements.keys():
            raise ElementNotExistsError(params)
        return elements.get(params)

    def _select_by_text(self, loc):
        elements = self.elements(loc)
        return {inner_ele.get_attribute('innerText'): inner_ele for inner_ele in elements} if elements else None
