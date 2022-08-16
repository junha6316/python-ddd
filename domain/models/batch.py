from datetime import date
from typing import Optional

from .orderline import OrderLine


class Batch:
    def __init__(self, ref:str, sku: str, qty: int, eta: Optional[date]):
        self.reference = ref
        self.sku = sku
        self.sta = eta
        self.available_quantity = qty

    def allocate(self, line: "OrderLine"):
        self.available_quantity -= line.qty