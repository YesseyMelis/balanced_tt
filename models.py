from datetime import date
from decimal import Decimal

from pydantic import BaseModel


class Transaction(BaseModel):
    date: date
    first_name: str
    last_name: str
    transaction_id: int
    amount: Decimal
    currency: str
