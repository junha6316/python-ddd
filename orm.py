from msilib import Table
from sqlalchemy.orm import mapper, relationship
from sqlalchemy import MetaData, Table, Column, Integer,String

from domain import models

metadata = MetaData()

order_lines = Table(
 'order_lines', metadata,
 Column('id', Integer, primary_key=True, autoincrement=True),
 Column('sku', String,(255),
 Column('qty', Integer, nullable=False),
 Column('orderId', String(255))
 )
)

def start_mappers():
    lines_mapper = mapper(models.OrderLine, order_lines)

