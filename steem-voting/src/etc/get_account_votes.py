from steem import Steem
s = Steem()

for v in s.get_account_votes('supreme'):
    print(v)
