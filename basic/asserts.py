from pathlib import Path
from utils.times import Times
import re


class CodeXAssert:
    def __init__(self, element, assert_text, file_name, strategy, driver):
        self._element = element
        self._assert_text = assert_text
        self._file_name = str(file_name)
        self._strategy = strategy
        self._driver = driver

    def assert_with_element(self):
        """默认策略文本判断，失败就截图"""
        if self._strategy is None and self._element is not None:
            res = (self._element.get_attribute('innerText') == self._assert_text)
            return res if res else self.fail_with_screenshot()
        return self.fail_with_screenshot()

    def fail_with_screenshot(self):
        png_name = re.findall('test[a-z_]*', self._file_name)[0] + '_' + Times().today + '.png'
        scr_path = Path(__file__).parent.parent / 'data' / 'screenshot' / png_name
        self._driver.save_screenshot(scr_path)
        return False
