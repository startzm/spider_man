import platform

from selenium import webdriver

from spider_man.crawler import get_root_path
from spider_man.custom_settings import CHROME_FILEPATH


__all__ = ['SeleniumDriver']


class SeleniumDriver():
    driver = None

    def _get_driver_path(self):
        if platform.system() == 'Darwin':
            return f'{CHROME_FILEPATH}_mac'
        if platform.system() == 'Windows':
            return f'{CHROME_FILEPATH}.exe'
        return f'{CHROME_FILEPATH}_linux'

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--profile-directory=Default')
        chrome_options.add_argument('--incognito')
        chrome_options.add_argument('--disable-plugins-discovery')
        chrome_options.add_argument('--start-maximized')
        chrome_options.add_argument('--disable-logging')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-setuid-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('-–single-process')
        prefs = {'profile.managed_default_content_settings.images': 2}

        chrome_options.add_experimental_option('prefs', prefs)

        filepath = get_root_path() + self._get_driver_path()
        self.driver = webdriver.Chrome(executable_path=filepath, chrome_options=chrome_options)
        self.driver.set_page_load_timeout(10)
        self.driver.set_script_timeout(10)
        self.driver.implicitly_wait(10)

    def get_driver(self):
        return self.driver