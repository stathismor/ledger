import pytest
from datetime import date
from decimal import Decimal
from ledger.account import Account
from ledger.transaction import Transaction


@pytest.fixture
def account():
    return Account("Hypo")


def test_create(account):
    assert account._name == "Hypo"
    assert account._transactions == []
    assert account._current_balance == 0


def test_credit_one_transaction(account):
    txn = Transaction(date(2020, 11, 4), "Thesis", "Hypo", Decimal("10.00"))

    txn = account.credit(txn)

    assert len(account._transactions) == 1
    assert account._current_balance == Decimal("10")


def test_credit_one_transaction(account):
    txn = Transaction(date(2020, 11, 4), "Hypo", "Thesis", Decimal("10.00"))

    txn = account.debit(txn)

    assert len(account._transactions) == 1
    assert account._current_balance == Decimal("-10")


def test_credit_multiple_transactions(account):
    txn1 = Transaction(date(2020, 11, 4), "A", "Hypo", Decimal("10.00"))
    txn2 = Transaction(date(2020, 11, 5), "B", "Hypo", Decimal("20.00"))
    txn3 = Transaction(date(2020, 11, 6), "C", "Hypo", Decimal("30.00"))

    account.credit(txn1)
    account.credit(txn2)
    account.credit(txn3)

    assert len(account._transactions) == 3
    assert account._transactions[0] == txn1
    assert account._transactions[1] == txn2
    assert account._transactions[2] == txn3


def test_debit_multiple_transactions(account):
    txn1 = Transaction(date(2020, 11, 4), "Hypo", "A", Decimal("10.00"))
    txn2 = Transaction(date(2020, 11, 5), "Hypo", "B", Decimal("20.00"))
    txn3 = Transaction(date(2020, 11, 6), "Hypo", "C", Decimal("30.00"))

    account.debit(txn1)
    account.debit(txn2)
    account.debit(txn3)

    assert len(account._transactions) == 3
    assert account._transactions[0] == txn1
    assert account._transactions[1] == txn2
    assert account._transactions[2] == txn3


def test_get_current_balance(account):
    account.credit(Transaction(date(2020, 11, 4), "A", "Hypo", Decimal("100.5")))
    account.debit(Transaction(date(2020, 11, 5), "Hypo", "B", Decimal("50.20")))
    account.credit(Transaction(date(2020, 11, 6), "C", "Hypo", Decimal("20.00")))
    account.credit(Transaction(date(2020, 11, 6), "D", "Hypo", Decimal("10.00")))

    assert account.get_current_balance() == Decimal("80.30")


def test_get_balance_at(account):
    account.credit(Transaction(date(2020, 11, 4), "A", "Hypo", Decimal("100.50")))
    account.debit(Transaction(date(2020, 11, 5), "Hypo", "B", Decimal("50.20")))
    account.credit(Transaction(date(2020, 11, 6), "C", "Hypo", Decimal("20.00")))
    account.credit(Transaction(date(2020, 11, 6), "D", "Hypo", Decimal("10.00")))

    assert account.get_balance_at(date(2020, 11, 5)) == Decimal("50.30")
