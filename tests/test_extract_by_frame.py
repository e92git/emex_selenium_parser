import pytest

from app.extractor import Extractor


def test_extract_by_frame1():
    extractor = Extractor()
    mapping = extractor.extract_by_framenum('BJ5W', '212063')

    mapping.pop('url')

    assert mapping == {
        'date': '04.1998',
        'engine': 'ｶﾞｿﾘﾝ',
        'mark': 'MAZDA',
        'model': 'Familia',
        'many_url': False,
    }

    extractor.close()


def test_extract_by_frame2():
    extractor = Extractor()
    mapping = extractor.extract_by_framenum('RF1', '1527314')

    mapping.pop('url')

    assert mapping == {
        'engine': 'B20B',
        'mark': 'HONDA',
        'model': 'STEP WGN',
        'option': 'Кондиционер с ручным управлением, Складывающиеся сидения, 3-спицевый руль',
        'many_url': True,
    }

    extractor.close()
