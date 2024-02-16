from utils.file_read import YamlReader
from pathlib import Path
from utils.decorators import Decorator
from basic.page import Page


class MdmManage(Page):
    url = 'https://test.pharmaos.com/static/mdm-enterprise/'

    @property
    def locators(self):
        return YamlReader(Path(__file__).parent / 'mdm_locators.yaml')

    @Decorator.obs_exceptions
    def hospital_search(self):
        self.get()
        self.element(self.locators.hospital_search_Btn).click()
