from pprint import pprint
from steem import Steem


s = Steem()
pprint(s.get_account('supreme'))

top_record = s.get_account_history('supreme', index_from=-1, limit=0)

top_index = top_record[0][0]

print(top_index)

pprint(s.get_account_history('supreme', index_from=-1, limit=top_index))
