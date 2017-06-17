Export STEEM Transactions

# Installation

pip3 install -r requirements.txt

# Note

This may be done better with [Piston](https://github.com/xeroc/piston-lib)
but all I know is this works.

# Datescan

run this to find the appropriate range of dates you are looking for.
It calls `steem.account.Account` which is incorrectly documented. If you look at the code, you will see that it calls steemd.get_account_history() and
you should use the docs for that to see how to call this.

    python3 datescan.py 8600 3200 | head
    python3 datescan.py 8600 3200 | tail
