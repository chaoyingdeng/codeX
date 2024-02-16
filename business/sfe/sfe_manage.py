from utils.file_read import YamlReader
from utils.times import Times
from pathlib import Path
from utils.decorators import Decorator
from basic.page import Page


class SFeManage(Page):
    url = 'https://test.pharmaos.com/static/cem-sales-pc/'

    @property
    def locators(self):
        return YamlReader(Path(__file__).parent / 'sfe_locators.yaml')

    @Decorator.obs_exceptions
    def open_affiliated_tab(self):
        self.get()
        self.element(self.locators.affiliation_tab).click()
        self.element(self.locators.affiliation_manage_tab).click()
        self.element(self.locators.affiliation_institution_input).send_keys('太美')

    @Decorator.obs_exceptions
    def open_flow_tab(self):
        self.get()
        self.element(self.locators.flow_tab).click()
        self.element(self.locators.flow_manage_tab).click()
        self.element(self.locators.month_final).click()
        self.element(self.locators.month_flow_period).click()
        self.select(self.locators.month_period_select, Times().pre_period).click()
        return self.element(self.locators.month_res)
