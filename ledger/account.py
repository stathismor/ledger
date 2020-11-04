import typing
import datetime
from decimal import Decimal
from ledger.transaction import Transaction


class Account:
    def __init__(self, name: str):
        self._name = name
        self._transactions = []
        # NOTE: Optimisation to get the current balance at all times,
        # instead of calculating for all transactions.
        self._current_balance = 0

    def credit(self, transaction: Transaction) -> typing.List[Transaction]:
        """
        Credit the account with the amount of the transaction

        Used when money are coming into the account.
        """
        self._transactions.append(transaction)
        # We are receiving money, therefore we subtract
        self._current_balance += transaction.amount

        return self._transactions

    def debit(self, transaction: Transaction) -> typing.List[Transaction]:
        """
        Debit the account with the amount of the transaction

        Used when money are going out of the account.
        """
        self._transactions.append(transaction)
        # We are paying money, therefore we subtract
        self._current_balance -= transaction.amount

        return self._transactions

    def get_current_balance(self) -> Decimal:
        return self._current_balance

    def get_balance_at(self, txn_date: datetime.date) -> Decimal:
        amount = 0
        for txn in self._transactions:
            if txn.txn_date <= txn_date:
                # Check if this account is the receiver. If yes,
                # the amount is credited, otherwise debited.
                if txn.receiver_name == self._name:
                    amount += txn.amount
                else:
                    amount -= txn.amount

        return amount
