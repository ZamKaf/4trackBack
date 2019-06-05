import time

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def selenium_test2():
    driver = webdriver.Firefox()
    #driver.get("http://www.python.org")
    driver.get("http://localhost:3000/login")
    #assert "Python" in driver.title
    elem = driver.find_element_by_name("loginInput")
    elem.send_keys("pycon")
    time.sleep(5)
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    driver.quit()
