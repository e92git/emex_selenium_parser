import time
from typing import List, Optional

from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from .base import BasePage, BaseElement
from .car_page import CarDetailsPage


class Table(BaseElement):
    def get_thead(self):
        thead: WebElement = WebDriverWait(self.element, 10).until(
            lambda e: e.find_element(By.XPATH, ".//thead")
        )

        return TableHead(thead)

    def get_tbody(self):
        tbody: WebElement = WebDriverWait(self.element, 10).until(
            lambda e: e.find_element(By.XPATH, ".//tbody")
        )

        return TableBody(tbody)

    def get_rows(self):
        trs: List[WebElement] = WebDriverWait(self.element, 10).until(
            lambda e: e.find_elements(By.XPATH, ".//tr")
        )

        return trs


class TableHead(Table):
    def get_rows(self):
        return [TableHeadRow(tr) for tr in super().get_rows()]


class TableBody(Table):
    def get_rows(self):
        return [TableBodyRow(tr) for tr in super().get_rows()]


class TableData(BaseElement):
    @property
    def value(self):
        return self.element.text.strip()


class TableRow(BaseElement):
    def get_tds(self) -> List[TableData]:
        tds: List[WebElement] = WebDriverWait(self.element, 10).until(
            lambda e: e.find_elements(By.XPATH, ".//td")
        )

        return [TableData(td) for td in tds]


class TableBodyRow(TableRow):
    def get_car_page(self):
        self.element.click()

        return CarDetailsPage(self.driver)


class TableHeadRow(TableRow):
    def get_tds(self) -> List[TableData]:
        ths: List[WebElement] = WebDriverWait(self.element, 10).until(
            lambda e: e.find_elements(By.XPATH, ".//th")
        )

        return [TableData(th) for th in ths]


class CarTablePage(BasePage):
    def __init__(self, driver: WebDriver):
        super(CarTablePage, self).__init__(driver)

    def get_table(self) -> Optional[Table]:
        timeout = 10
        t1 = time.time()
        while time.time() < t1 + timeout:
            try:
                table = self.driver.find_element(By.XPATH, "//table[@class='modifications']")

            except:
                try:
                    self.driver.find_element(By.XPATH, "//div[@class='emptyresult']")

                except:
                    pass

                else:
                    return None

            else:
                return Table(table)
