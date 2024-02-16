from basic.browser import Browser


class ChromeBrowser(Browser):
    HEADLESS = True
    METHOD_MARK = True
    START_MAX = '--start-maximized'
    EXP = {
        'excludeSwitches': ['enable-automation'],
        'prefs': {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        }
    }

    @property
    def options(self):
        chrome_option = self._option()
        # chrome_option.add_argument(self.START_MAX)
        for k, v in self.EXP.items():
            chrome_option.add_experimental_option(k, v)
        chrome_option.headless = self.HEADLESS

        return chrome_option

    @property
    def browser(self):
        chrome = self._browser(service=self._service, options=self.options)
        if self.METHOD_MARK:
            chrome.implicitly_wait(self.IMP_TIME)
            chrome.set_script_timeout(self.SCRIPT_TIME_OUT)
            chrome.set_page_load_timeout(self.PAGE_LOAD_TIME)

        return chrome
