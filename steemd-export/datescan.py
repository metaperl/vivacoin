import argh
from steem.account import Account


def process(acct, start, limit):
    ops = set()

    a = Account(acct)

    for record in a.get_account_history(start, limit):
        print(record['timestamp'])

def main(start, limit, acct='tradeqwik'):
    process(acct, start, limit)


argh.dispatch_command(main)
