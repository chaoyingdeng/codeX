from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from selenium.webdriver.edge.webdriver import WebDriver as Edge
from selenium.webdriver.firefox.webdriver import WebDriver as Firefox
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from typing import Type, Union
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from basic.exceptions import BrowserTypeError
from setting import *


class Browser:
    WINDOWS_SIZE = (768, 768)
    IMP_TIME = 60
    PAGE_LOAD_TIME = 20
    SCRIPT_TIME_OUT = 20
    HEADLESS = False

    def __init__(self, browser_type: Type[Union[Chrome, Edge, Firefox]] = Chrome,
                 option_type: Type[Union[ChromeOptions, EdgeOptions, FirefoxOptions]] = ChromeOptions,
                 browser_service: Type[Union[ChromeService, EdgeService, FirefoxService]] = ChromeService,
                 driver_path: str = CHROME_DRIVE_PATH):
        if not issubclass(browser_type, (Chrome, Edge, Firefox)):
            raise BrowserTypeError(browser_type)
        if not issubclass(option_type, (ChromeOptions, EdgeOptions, FirefoxOptions)):
            raise BrowserTypeError(option_type)
        if not isinstance(driver_path, str):
            raise TypeError(f'{type(driver_path)}')

        self._path = driver_path
        self._browser = browser_type
        self._option = option_type
        self._service = browser_service(executable_path=driver_path)

    @property
    def options(self):
        return

    @property
    def browser(self):
        return
