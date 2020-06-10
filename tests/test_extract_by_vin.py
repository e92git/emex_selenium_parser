import pytest

from app.extractor import Extractor


def test_extract_by_vin_mitsubishi_outlander():
    extractor = Extractor()
    mapping = extractor.extract_by_vin('JMBXTGF3WDZ007092')

    mapping.pop('url')

    assert mapping == {
        'date': '10.2012',
        'engine': '2400 - INSTYLE(4WD/5P),CVT LHD',
        'mark': 'MITSUBISHI',
        'model': 'OUTLANDER',
        'many_url': False,
        'option': 'S05: SIZE-UP TIRE; AUDIO SYSTEM (5); LEATHER SEAT & ROOM TRIM; CARGO FLOOR BOX; PRIVACY GLASS; R/CONT MIRROR (WITH FOLDING CONTROL); TEL COMMUNICATION SYSTEM; TEL COMMUNICATION SYSTEM (B); ONE TOUCH START SYSTEM; ONE TOUCH START SYSTEM; RR HARNESS (OTHER OPTION)'
    }
    extractor.close()


def test_extract_by_vin_nissan_teana():
    extractor = Extractor()
    mapping = extractor.extract_by_vin('Z8NBCWJ32BS020772')

    mapping.pop('url')

    assert mapping == {
        'date': '06.2011',
        'engine': 'QR25DE',
        'mark': 'NISSAN',
        'model': 'TEANA',
        'many_url': False,
        'option': 'Привод:4WD'
    }

    extractor.close()


def test_extract_by_vin_not_existing():
    extractor = Extractor()
    mapping = extractor.extract_by_vin('ae1013078659')

    assert mapping == {}

    extractor.close()


def test_extract_by_vin_mitsubishi_montero():
    extractor = Extractor()
    mapping = extractor.extract_by_vin('JA4MW51RX1J019722')

    mapping.pop('url')

    assert mapping == {
        'date': '08.2000',
        'engine': '3500/LONG WAGON<01M-> - LTD(NSS4),S5FA/T FED',
        'mark': 'MITSUBISHI',
        'model': 'MONTERO',
        'many_url': True,
        'option': "A01: RR HEATER + H/DUTY HEATER; DUAL AUTO A/C; HMSL + DOOR LOCK; AUTO A/C + OTHER OPTION; A/C + RR HEATER; A/C + RR HEATER; DUAL A/C + RR HEATER; DUAL A/C + RR HEATER; AUTO A/C + OTHER OPTION; RR HEATER + DUAL A/C; RR HEATER + DUAL COOLER",
    }

    extractor.close()