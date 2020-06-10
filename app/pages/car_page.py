from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


from .base import BasePage


class CarDetailsPage(BasePage):
    def __init__(self, driver: WebDriver):
        super(CarDetailsPage, self).__init__(driver)

        WebDriverWait(self.driver, 10).until(
            lambda d: d.find_element(By.XPATH, "//div[@class='info']")
        )
        
    def get_url(self) -> str:
        return self.driver.current_url

    def get_mark_model(self):
        info_div: WebElement = self.driver.find_element(By.XPATH, "//div[@class='info']")
        return info_div.text.strip()