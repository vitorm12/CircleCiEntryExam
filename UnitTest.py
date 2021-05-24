from selenium import webdriver;
import unittest;

from main import test_on_click_output;


def test_on_click():
    text = test_on_click_output()
    assert "Hello World" == text.text


if __name__ == '__main__':
    test_on_click()
