from basic.browser import Browser
from selenium.webdriver.edge.webdriver import WebDriver as Edge
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from pathlib import Path


class EdgeBrowser(Browser):
    Driver_PATH = str(Path(__file__).parent.parent / 'drivers' / 'msedgedriver.exe')

    HEADLESS = True  # 将 HEADLESS 属性设置为 True
    START_MAX = '--start-maximized'
    EXP = {
        'excludeSwitches': ['enable-automation']
    }

    def __init__(self):
        super().__init__(Edge, EdgeOptions, EdgeService, self.Driver_PATH)

    @property
    def options(self):
        edge_option = self._option()
        edge_option.add_argument(self.START_MAX)
        for k, v in self.EXP.items():
            edge_option.add_experimental_option(k, v)
        edge_option.headless = self.HEADLESS
        return edge_option

    @property
    def browser(self):
        edge = self._browser(service=self._service, options=self.options)
        edge.implicitly_wait(self.IMP_TIME)
        edge.set_script_timeout(self.SCRIPT_TIME_OUT)
        edge.set_page_load_timeout(self.PAGE_LOAD_TIME)

        return edge
