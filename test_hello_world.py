import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import main
import unittest


class TestHelloWorld(unittest.TestCase):

    def setUp(self):
        self.app = main.app.test_client()
        self.app.testing = True

    def test_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        workDir = os.path.dirname(os.path.realpath(__file__))
        path_to_driver = workDir + "/" + "chromedriver"
        driver = webdriver.Chrome(path_to_driver)
        #driver.get(workDir+"/html/index.html");
        #button = driver.find_element_by_id("button")
        #button.click();

    def test_greeting_message(self):
        greeting = 'Welcome to CI/CD'
        self.assertEqual(main.greet(), greeting)


if __name__ == '__main__':
    unittest.main()