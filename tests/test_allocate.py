from datetime import date, timedelta
import pytest
from domain.models.batch import Batch
from domain.models.orderline import OrderLine


today = date.today()
tomorrow = date.today() + timedelta(days=1)
later = date.today() + timedelta(days=2)

def test_inStock되어_있는_배치를_먼저설정한다():
    in_stock_batch = Batch("in-stock-batch", "retro-clock", 100, eta=None)
    shipment_batch = Batch("shipment-batch", "retro-clock", 100, eta=date.today()+ timedelta(days=1))
    line = OrderLine("oref", "retro-clock", 10)

    Batch.auto_allocate(line, [in_stock_batch, shipment_batch])

    assert in_stock_batch.available_quantity == 90
    assert shipment_batch.available_quantity == 100

def test_더_빠른_배치를_선호():
    earliest = Batch("speedy-batch", "MINIMALIST-SPOON", 100, eta=today)
    medium = Batch("normal-batch", "MINIMALIST-SPOON", 100, eta=tomorrow)
    latest = Batch("slow-batch", "MINIMALIST-SPOON", 100, eta=later)
    line = OrderLine("order1", "MINIMALIST-SPOON", 10)

    Batch.auto_allocate(line, [medium, earliest, latest])

    assert earliest.available_quantity == 90
    assert medium.available_quantity == 100
    assert latest.available_quantity == 100

def test_할당된_배치의_ref를_반환():
    in_stock_batch = Batch("in-stock-batch-ref", "HIGHBROW-POSTER", 100, eta=None)
    shipment_batch = Batch("shipment-batch-ref", "HIGHBROW-POSTER", 100)

    line = OrderLine("oref", "HIGHBROW-POSTER", 10)

    allocation = Batch.auto_allocate(line, [in_stock_batch, shipment_batch])
    assert allocation == in_stock_batch.reference