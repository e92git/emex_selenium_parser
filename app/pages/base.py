from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver


class BaseElement:
    def __init__(self, element: WebElement):
        self.element = element

        self.driver = element._parent
