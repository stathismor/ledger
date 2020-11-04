import io
import csv
import typing
import operator
from decimal import Decimal

_CURRENCY_SYMBOL = "§"


def parse_csv(
    csv_file: io.IOBase,
) -> typing.Tuple[typing.Tuple[str]]:  # pragma: no cover
    """Parse and sort (from older to newer) all the transaction from a CSV file."""
    csv_reader = csv.reader(csv_file)
    sorted_transactions = sorted(csv_reader, key=operator.itemgetter(0))

    return sorted_transactions


def format_amount(amount: Decimal) -> str:
    """Format an amount with to a human-readable text"""
    return f"{_CURRENCY_SYMBOL}{amount:.2f}"
