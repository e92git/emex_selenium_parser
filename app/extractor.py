from typing import Optional, Dict

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from .constants import CHROME_DRIVER
from .pages.car_table import CarTablePage, TableBodyRow, TableHeadRow


def map_th_tr(thr: TableHeadRow, tbr: TableBodyRow):
    ret = {}
    for th, td in zip(thr.get_tds(), tbr.get_tds()):
        ret[th.value] = td.value

    return ret


class Extractor:
    def __init__(self, proxy: Optional[str] = None):
        options = ChromeOptions()
        options.add_argument('--disable-notifications')
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")

        if proxy is not None:
            options.add_argument(f"--proxy-server={proxy}")

        self.driver: Chrome = Chrome(executable_path=str(CHROME_DRIVER), options=options)

    def extract_table_info(self) -> Dict[str, str]:
        car_details_page = CarTablePage(self.driver)

        table = car_details_page.get_table()

        if table is None:
            return {}

        thead = table.get_thead()
        tbody = table.get_tbody()

        thead_row = thead.get_rows()[0]

        tbody_rows = tbody.get_rows()
        needed_row = tbody_rows[0]

        mapped = map_th_tr(thead_row, needed_row)

        car_page = needed_row.get_car_page()
        model = mapped.get('Наименование')
        mark_model = car_page.get_mark_model()

        mark = mark_model.rstrip(model).strip()

        date = mapped.get('date') or mapped.get('Модификация выпускается с')
        option = mapped.get('Опции')

        ret = {
            'url': car_page.get_url(),
            'many_url': str(int(len(tbody_rows) > 1)),
            'model': model,
            'mark': mark,
            'engine': mapped.get('Модификация') or mapped.get('Двигатель'),
        }

        if date:
            ret['date'] = date

        if option:
            ret['option'] = option

        return ret

    def extract_by_vin(self, vin: str) -> Dict[str, str]:
        self.driver.get(f"https://emex.ru/catalogs/original/?screen=modifications&vin={vin}")

        return self.extract_table_info()

    def extract_by_framenum(self, frame: str, framenum: str) -> Dict[str, str]:
        self.driver.get(f"https://emex.ru/catalogs/original/?screen=modifications&frame={frame}&framenum={framenum}")

        return self.extract_table_info()

    def close(self):
        try:
            self.driver.close()

        except:
            pass

    def __del__(self):
        self.close()
