import io
import typing
import datetime
import ledger.utils as utils
from decimal import Decimal
from ledger.account import Account
from ledger.transaction import Transaction

_TXN_FILE = "data/transactions.csv"


class AcountNotFoundError(Exception):
    ...


class Ledger:
    def __init__(self, txn_file: str = _TXN_FILE) -> None:
        self._txn_file = txn_file
        self._accounts = {}

    def load_transactions(self) -> None:  # pragma: no cover
        """
        Parse and process the CSV file, loading all accounts
        and their transactions in memory
        """
        try:
            with open(self._txn_file) as csv_file:
                self._process_file(csv_file)
        except IOError:
            raise Exception(f"There was an error opening {self._txn_file}")

    def get_current_balance(self, name: str) -> Decimal:
        """Get the current balance of an account"""
        account = self._get_account(name)
        amount = account.get_current_balance()
        amount = utils.format_amount(amount)

        return amount

    def get_balance_at(self, txn_date: datetime.date, name: str) -> Decimal:
        """Get the current balance of an account, at a specific date"""
        account = self._get_account(name)
        amount = account.get_balance_at(txn_date)
        amount = utils.format_amount(amount)

        return amount

    def _process_file(self, csv_file: io.IOBase) -> None:  # pragma: no cover
        """Process the transactions of a CSV file

        This is a wrapper arround `_process_transactions`, so as to decouple the
        CSV file from the input of the actual processing. Also provides an
        easier-to-test interface, to `_process_transactions`.
        """
        # `parse_csv` sorts the transactions from older to newer
        sorted_transactions = utils.parse_csv(csv_file)
        self._process_transactions(sorted_transactions)

    from collections.abc import Sequence

    def _process_transactions(
        self, transactions: typing.Sequence[typing.Tuple[str]]
    ) -> None:
        """
        Process a list of transactions

        Each transaction is a list of string values, like:
        (date, sender_name, receiver_name, amount)
        """

        for txn_date, sender_name, receiver_name, amount in transactions:
            amount = Decimal(amount)
            # Convert date string of format YYYY-MM-DD to a datetime.date object
            txn_date = datetime.datetime.strptime(txn_date, "%Y-%m-%d").date()

            sender = self._get_or_create_account(sender_name)
            receiver = self._get_or_create_account(receiver_name)
            transaction = Transaction(txn_date, sender_name, receiver_name, amount)

            sender.debit(transaction)
            receiver.credit(transaction)

    def _get_account(self, name: str) -> Account:
        try:
            account = self._accounts[name]
        except KeyError:
            raise AcountNotFoundError(f"Account `{name}` not found")

        return account

    def _get_or_create_account(self, name: str) -> Account:
        try:
            account = self._accounts[name]
        except KeyError:
            account = Account(name)
            self._accounts[name] = account

        return account
