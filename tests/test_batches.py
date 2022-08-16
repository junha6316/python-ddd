
# batch를 위한 테스트
import pytest
from datetime import date

from domain.models.orderline import OrderLine
from domain.models.batch import Batch

def make_batch_and_line(sku, batch_qty, line_qty):
    batch = Batch("batch-001", sku, qty=batch_qty, eta=date.today())
    line = OrderLine('order-ref', sku, line_qty)
    return batch, line

def test_할당시_사용가능한_양_감소():
    batch, line = make_batch_and_line('batch-001', 20, 2)

    batch.allocate(line)

    assert batch.available_quantity == 18

def test_라인_할당량보다_많이_남아있을_때_할당_가능():
    large_batch, small_line = make_batch_and_line("ELEGANT-LAMP", 20, 2)
    assert large_batch.can_allocate(small_line)

def test_라인_할당량이_배치보다_클때_할당_불가능():
    small_batch, large_line = make_batch_and_line("ELEGANT-LAMP", 2, 20)
    assert small_batch.can_allocate(large_line) is False

def test_라인_할당량과_배치가_동일할_때_가능():
    batch, line = make_batch_and_line("ELEGANT-LAMP", 20, 20)
    assert batch.can_allocate(line)

def test_sku가_동일하지_않으면_할당_불가능():
    batch = Batch("batch-001", "TEST_BATCH_SKU", 100, eta=None)
    different_sku_line = OrderLine("order-123", "OTHER_SKU", 10)
    assert batch.can_allocate(different_sku_line) is False
