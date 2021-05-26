import os

from selenium import webdriver


import main
import unittest

class TestHelloWorld(unittest.TestCase):
    DOWNLOAD_DIR = '/tmp'

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
        self.driver = webdriver.Chrome(chrome_options=self.options)
        self.driver.implicitly_wait(10)
        workDir = os.path.dirname(os.path.realpath(__file__))
        self.driver.get(host='0.0.0.0')

        button = self.driver.find_element_by_id("button")
        button.click();
        text = self.driver.find_element_by_id("demo")


    def test_greeting_message(self):
        greeting = 'Welcome to CI/CD'
        self.assertEqual(main.greet(), greeting)


if __name__ == '__main__':
    unittest.main()