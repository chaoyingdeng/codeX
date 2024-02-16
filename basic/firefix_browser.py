from basic.browser import Browser
from selenium.webdriver.firefox.webdriver import WebDriver as Firefox
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from pathlib import Path


class FireFixBrowser(Browser):
    DRIVERS_PATH = Path(__file__).parent.parent / 'drivers'
    FIREFOX_PATH = str(DRIVERS_PATH / 'geckodriver.exe')
    HEADLESS = True  # 将 HEADLESS 属性设置为 True
    START_MAX = '--start-maximized'
    EXP = {
        'excludeSwitches': ['enable-automation']
    }

    def __init__(self):
        super().__init__(Firefox, FirefoxOptions, FirefoxService, self.FIREFOX_PATH)

    @property
    def options(self):
        firefox_option = self._option()
        firefox_option.headless = self.HEADLESS
        # firefox_option.add_argument(self.START_MAX)
        # firefox_option.set_preference('dom.webdriver.enabled', False)
        # firefox_option.set_preference('useAutomationExtension', False)
        return firefox_option

    @property
    def browser(self):
        firefox = self._browser(service=self._service, options=self.options)
        firefox.implicitly_wait(self.IMP_TIME)
        firefox.set_script_timeout(self.SCRIPT_TIME_OUT)
        firefox.set_page_load_timeout(self.PAGE_LOAD_TIME)

        return firefox
