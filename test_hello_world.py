import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

import main
import unittest
import WebDriver

class TestHelloWorld(unittest.TestCase):

    def setUp(self):
        self.app = main.app.test_client()
        self.app.testing = True
        self.options = webdriver.ChromeOptions()

        self.options.add_argument('--disable-extensions')
        self.options.add_argument('--headless')
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--no-sandbox')

        self.options.add_experimental_option(
            'prefs', {
                'download.default_directory': self.DOWNLOAD_DIR,
                'download.prompt_for_download': False,
                'download.directory_upgrade': True,
                'safebrowsing.enabled': True
            }
        )



    def test_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.driver = webdriver.Chrome(chrome_options=self.options)
        self.driver.implicitly_wait(10)

    def test_greeting_message(self):
        greeting = 'Welcome to CI/CD'
        self.assertEqual(main.greet(), greeting)


if __name__ == '__main__':
    unittest.main()