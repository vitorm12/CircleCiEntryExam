import logging
import os

from selenium import webdriver

def test_on_click_output():

    workDir = os.path.dirname(os.path.realpath(__file__))
    #print(workDir)
    path_to_driver = workDir+"/Test/"+"chromedriver"
    driver = webdriver.Chrome(path_to_driver);
    #driver.get(workDir+"/html/index.html");
    #button = driver.find_element_by_id("button")
   # button.click();
    #text = driver.find_element_by_id("demo")
    return "Hi"


if __name__ == '__main__':
    test_on_click_output()