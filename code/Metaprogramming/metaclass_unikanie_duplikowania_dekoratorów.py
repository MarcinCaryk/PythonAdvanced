import attr
import datetime
from uuid import UUID
from decimal import Decimal
from currencies import Currency


@attr.s(frozen=True, auto_attribs=True)
class Event:
    created_at: datetime


@attr.s(frozen=True, auto_attribs=True)
class InvoiceIssued(Event):
    invoice_uuid: UUID
    customer_uuid: UUID
    total_amount: Decimal
    total_amount_currency: Currency
    due_date: datetime


@attr.s(frozen=True, auto_attribs=True)
class InvoiceOverdue(Event):
    invoice_uuid: UUID
    customer_uuid: UUID
