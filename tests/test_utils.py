from decimal import Decimal
import ledger.utils as utils


def test_format_amount_zero():
    assert utils.format_amount(Decimal("0.00")) == "§0.00"


def test_format_amount_positive():
    assert utils.format_amount(Decimal("20.00")) == "§20.00"


def test_format_amount_negative():
    assert utils.format_amount(Decimal("-10.00")) == "§-10.00"
