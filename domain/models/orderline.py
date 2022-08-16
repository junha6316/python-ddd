from dataclasses import dataclass


@dataclass(frozen=True)
class OrderLine:
    orderId: str
    sku: str
    qty: int

