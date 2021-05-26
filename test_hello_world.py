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



    def test_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        with WebDriver() as driver:
            driver.login()

    def test_greeting_message(self):
        greeting = 'Welcome to CI/CD'
        self.assertEqual(main.greet(), greeting)


if __name__ == '__main__':
    unittest.main()