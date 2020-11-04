import pytest
from datetime import date
from decimal import Decimal
from ledger.ledger import Ledger, AcountNotFoundError
from ledger.transaction import Transaction
from ledger.account import Account


@pytest.fixture
def ledger():
    ledger = Ledger()
    transactions = (
        ("2015-01-16", "john", "mary", "120.50"),
        ("2015-01-17", "john", "supermarket", "20.00"),
        ("2015-01-17", "mary", "insurance", "100.00"),
        ("2015-01-18", "john", "insurance", "50.00"),
    )
    ledger._process_transactions(transactions)

    return ledger


def test_process_transactions(ledger):
    assert len(ledger._accounts) == 4

    expected_transactions = [
        Transaction(date(2015, 1, 16), "john", "mary", Decimal("120.50")),
        Transaction(date(2015, 1, 17), "john", "supermarket", Decimal("20.00")),
        Transaction(date(2015, 1, 18), "john", "insurance", Decimal("50.00")),
    ]
    assert ledger._accounts["john"]._transactions == expected_transactions


def test_get_current_balance(ledger):
    assert ledger.get_current_balance("john") == "§-190.50"
    assert ledger.get_current_balance("mary") == "§20.50"


def test_get_balance_at(ledger):
    assert ledger.get_balance_at(date(2015, 1, 17), "john") == "§-140.50"
    assert ledger.get_balance_at(date(2015, 1, 17), "mary") == "§20.50"


def test_get_account_existing(ledger):
    account = ledger._get_account("john")

    assert account._name == "john"


def test_get_account_non_existent(ledger):
    with pytest.raises(AcountNotFoundError):
        account = ledger._get_account("i_do_not_exist")


def test_get_or_create_account_existing(ledger):
    account = ledger._get_account("john")

    assert account._name == "john"


def test_get_or_create_account_non_existent(ledger):
    account = ledger._get_or_create_account("i_do_not_exist")

    assert account._name == "i_do_not_exist"
