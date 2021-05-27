from selenium import webdriver
import unittest


class TestHtml(unittest.TestCase):
    DOWNLOAD_DIR = '/tmp'

    def setUp(self):
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

    def test_button(self):
        f = open("index.html", "r")
        html_content = f.read()
        self.driver = webdriver.Chrome(chrome_options=self.options)
        self.driver.implicitly_wait(10)
        self.driver.get("data:text/html;charset=utf-8,{html_content}".format(html_content=html_content))
        button = self.driver.find_element_by_id("button")
        button.click();
        text = self.driver.find_element_by_id("demo").text
        self.assertEqual("Hello World", text)
