import argh
from steem.steemd import Steemd


def process(acct, index_from, limit):
    ops = set()

    s = Steemd()

    for record in s.get_account_history(acct, index_from, limit):
        print(record)

def main(start, limit, acct='tradeqwik'):
    process(acct, start, limit)


argh.dispatch_command(main)
