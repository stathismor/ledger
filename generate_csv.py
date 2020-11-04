#! /usr/bin/env python

import sys
import csv
import time
import random
import datetime

_DEFAULT_CSV_FILE = "data/transactions.csv"
_DEFALT_ROWS_COUNT = 10
_NAMES = ("john", "mary", "alice", "bob")
_ORGANISATIONS = ("supermarket", "insurance", "restaurant")


def _random_date(years_delta):
    today_date = datetime.datetime.today()

    two_years_ago_date = today_date - datetime.timedelta(days=years_delta * 365)
    two_years_ago_seconds = int(two_years_ago_date.timestamp())

    now_seconds = int(time.time())
    random_date_seconds = random.randint(two_years_ago_seconds, now_seconds)

    return datetime.datetime.fromtimestamp(random_date_seconds).date()


with open(_DEFAULT_CSV_FILE, mode="w") as csv_file:
    txn_writer = csv.writer(csv_file, delimiter=",")

    rows_count = sys.argv[1] if len(sys.argv) > 1 else _DEFALT_ROWS_COUNT

    for i in range(rows_count):
        txn_date = _random_date(2)

        txn_from = random.choice(_NAMES)

        names = tuple(n for n in _NAMES if n != txn_from)
        txn_to = random.choice(names + _ORGANISATIONS)

        txn_amount = "{:.2f}".format(random.randint(1, 500))

        row = [txn_date, txn_from, txn_to, txn_amount]
        print(",".join(str(v) for v in row))

        txn_writer.writerow(row)
