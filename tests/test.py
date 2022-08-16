
# batch를 위한 테스트
from datetime import date

from ..domain.models.orderline import OrderLine
from ..domain.models.batch import Batch


def test_할당시_사용가능한_양_감소():
    batch = Batch("batch-001", "SMALL-TABLE", qty=20, eta=date.today())
    line = OrderLine('order-ref', 'SMALL-TABLE', 2)

    batch.allocate(line)

    assert batch.available_quantity == 18