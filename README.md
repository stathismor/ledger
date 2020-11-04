# Ledger
Process transactions in a ledger

## Setup

**NOTE 1**: Only do steps 1 and 3 if this is the first time running the ledger.

**NOTE 2**: You can of course use your preferred way of managing a virtual env.

1. Create a virtual env:

```
$ python3 -m venv env
```

2. Activate the virtual env:
```
$ source env/bin/activate`
```
3. Install the requirements:
```
$ pip install -r requirements.txt
```

## Generate CSV
To generate new transactions in the CSV file (`data/transactions.csv`), do:
```
$ ./generate_csv.py
```

## Run the ledger
To run the ledger on the generated CSV, and show a couple of values, do:
```
$ ./run_ledger.py
```

## Run the tests
To run the tests and see the coverage, do:
```
$ ./run_tests.sh
```
