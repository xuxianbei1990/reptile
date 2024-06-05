from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import platform


class SystemWebUtil:
    def __init__(self):
        options = Options()
        # 无头模式
        os_name = platform.system()
        if os_name == 'Windows':
            options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'  # 替换为你的Firefox路径
            service = Service(r'../firefox/geckodriver.exe')
        if os_name == 'Linux':
            options.add_argument('--headless')
            service = Service(r'./geckodriver')
        self.browser = webdriver.Firefox(service=service, options=options)

    def get_browser(self) -> webdriver.Firefox:
        return self.browser

    def close_browser(self):
        self.browser.quit()