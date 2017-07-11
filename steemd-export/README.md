Export STEEM Transactions

# Usage

## Auxilliary Tool: Datescan

You may wish to export transactions for a date range, instead of all
transactions. If this is so, then you need to get the indexes for the
items that bound the date range your are interested in.

In other words, each transaction for an account has a numerical index. Since
you may only be interested in a certain range, you need to find out
the indexes for your range.

The tool `datescan.py` can be used for this purpose. It defaults to
providing data for the steem account `tradeqwik` if you do not supply
this argument.

Let's see a run of this tool, which shows the 2 earliest transactions
for this account and then a run which shows the 2 most recent
transactions for this account:

```
schemelab@metta:~/prg/vivacoin/steemd-export$ python3 datescan.py 1 1
[0, {'trx_id': 'f18d71eb1e1f17348e86875fe55905cc07e4bf19', 'block': 6797654, 'trx_in_block': 5, 'op_in_trx': 0, 'virtual_op': 0, 'timestamp': '2016-11-17T08:19:54', 'op': ['account_create', {'fee': '40.000 STEEM', 'creator': 'anonsteem', 'new_account_name': 'tradeqwik', 'owner': {'weight_threshold': 1, 'account_auths': [], 'key_auths': [['STM7B88m1tw22y4EJ9F6UxTteGaVTw6iZwtKMJ3zQuJaTvZuBjZAu', 1]]}, 'active': {'weight_threshold': 1, 'account_auths': [], 'key_auths': [['STM55MGbkqxbpU7eU4UXiBCfEUm92aL96syCuCw2tnvAzxR9BHuC6', 1]]}, 'posting': {'weight_threshold': 1, 'account_auths': [], 'key_auths': [['STM8HfDR8LyJMyT8KKambnfbNK5szAXmgVrMbLoKh3qzNnqJcAM9n', 1]]}, 'memo_key': 'STM8hN8Zs7Wj4cVTSfZNEQzi5bBxeZzmHpqVxbfSaz3ADgsSDRQem', 'json_metadata': ''}]}]
[1, {'trx_id': '4132632f1b09d0a58f9ab6694f150dab58d20442', 'block': 6803245, 'trx_in_block': 2, 'op_in_trx': 0, 'virtual_op': 0, 'timestamp': '2016-11-17T12:59:27', 'op': ['custom_json', {'required_auths': [], 'required_posting_auths': ['tradeqwik'], 'id': 'follow', 'json': '["reblog",{"account":"tradeqwik","author":"williambanks","permlink":"introduction-to-viva-a-price-stable-crypto-currency-with-basic-income-that-s-not-hypothetical"}]'}]}]
schemelab@metta:~/prg/vivacoin/steemd-export$ python3 datescan.py -1 1
[15595, {'trx_id': '350b9fe17e912c23d987b40fc2da5c9d2be00809', 'block': 13591406, 'trx_in_block': 27, 'op_in_trx': 0, 'virtual_op': 0, 'timestamp': '2017-07-11T14:09:42', 'op': ['vote', {'voter': 'tradeqwik', 'author': 'tyler-fletcher', 'permlink': 'crypto-war-saving-private-ryan-parody', 'weight': 2500}]}]
[15596, {'trx_id': '5b8b4edc73462d35395d333ca9c21ed2c5bd07e4', 'block': 13591500, 'trx_in_block': 13, 'op_in_trx': 0, 'virtual_op': 0, 'timestamp': '2017-07-11T14:14:27', 'op': ['vote', {'voter': 'tradeqwik', 'author': 'wiser', 'permlink': 'did-streemian-have-a-hiccup-last-night', 'weight': 2500}]}]
schemelab@metta:~/prg/vivacoin/steemd-export$
```

### Finding a particular date range

Now, let's say we want to find all transactions from May 1 to May
31. Let's repeatedly use datescan to find them.

```
schemelab@metta:~/prg/vivacoin/steemd-export$ python3 datescan.py 4730 1
[4729, {'trx_id': '5be6ea51fad4d59859567051db99a0c330cd66ea', 'block': 11530981, 'trx_in_block': 0, 'op_in_trx': 0, 'virtual_op': 0, 'timestamp': '2017-04-30T22:56:27', 'op': ['vote', {'voter': 'tradeqwik', 'author': 'hilarski', 'permlink': 'simon-dixon-of-bank-to-the-future-interviewed-by-jeff-berwick', 'weight': 10000}]}]
[4730, {'trx_id': '0000000000000000000000000000000000000000', 'block': 11531363, 'trx_in_block': 2, 'op_in_trx': 1, 'virtual_op': 0, 'timestamp': '2017-04-30T23:15:36', 'op': ['curation_reward', {'curator': 'tradeqwik', 'reward': '307.186200 VESTS', 'comment_author': 'stephenkendal', 'comment_permlink': 'blockchain-european-commission-to-tender-offers-for-a-service-contract-to-establish-a-european-union-blockchain-observatory-in'}]}]
schemelab@metta:~/prg/vivacoin/steemd-export$
```

Ok, it looks like the start of the range has index 4730 (I like to
include a transaction from just before the period so the consumer of
the data is confident nothing was left out).

```
schemelab@metta:~/prg/vivacoin/steemd-export$ python3 datescan.py 8530 1
[8529, {'trx_id': '2c260f91ab13c742ef340b03871ed7349f28e96f', 'block': 12426342, 'trx_in_block': 2, 'op_in_trx': 0, 'virtual_op': 0, 'timestamp': '2017-06-01T01:44:57', 'op': ['vote', {'voter': 'tradeqwik', 'author': 'wideopen.world', 'permlink': 'work-1-5th-as-much-for-the-same-quality-of-life', 'weight': 10000}]}]
[8530, {'trx_id': '0000000000000000000000000000000000000000', 'block': 12426497, 'trx_in_block': 9, 'op_in_trx': 1, 'virtual_op': 0, 'timestamp': '2017-06-01T01:52:45', 'op': ['curation_reward', {'curator': 'tradeqwik', 'reward': '642.369006 VESTS', 'comment_author': 'aunt-deb', 'comment_permlink': 'steemit-story-slam-competition-two-days-til-deadline-eleven-entries-so-far'}]}]
```

Ok and 8530 ends our range (again with a few extra transactions to
ensure we did not leave any out).

## Main tool

Ok, now that we have the indexes, let's run the main tool. Note that
we have to supply the *end index* and provide the amount of entries we
want moving backwards from that point.

In other words, our chosen range was 4730 to 8530. So we need to
subtract these numbers to see how many entries we want and supply 8530
and our index to move backwards from:

```
schemelab@metta:~/prg/vivacoin/steemd-export$ python3 -i
Python 3.5.3 (default, Jan 19 2017, 14:11:04)
[GCC 6.3.0 20170118] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 8530 - 4730
3800
```

and now run main:

schemelab@metta:~/prg/vivacoin/steemd-export$ python3 main.py tradeqwik 8530 3800



# Installation

pip3 install -r requirements.txt

# Note

This may be done better with [Piston](https://github.com/xeroc/piston-lib)
but all I know is this works.
