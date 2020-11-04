from collections import namedtuple

Transaction = namedtuple(
    "Transaction", ["txn_date", "sender_name", "receiver_name", "amount"]
)
