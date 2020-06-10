from datetime import date
from typing import Optional
from .base import BaseObject


class TableRow(BaseObject):
    date: Optional[date]
    url: str
    many_url: bool
    model: str
    option: str
    mark: str


