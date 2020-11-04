#! /usr/bin/env python

import datetime
from ledger.ledger import Ledger


ledger = Ledger()
ledger.load_transactions()

current_balance = ledger.get_current_balance("john")

one_month_ago = datetime.date.today() - datetime.timedelta(days=60)
two_month_ago_balance = ledger.get_balance_at(one_month_ago, "john")

print("Current balance:", current_balance)
print("Balance one month ago:", two_month_ago_balance)
