from steem import Steem
s = Steem()

for v in s.get_blog_entries('awarenessraiser', -1, 5):
    print (v)

'''
schemelab@metta:~/prg/vivacoin/steem-voting/src/etc$ python3 get_blog_entries.py
[{'author': 'awarenessraiser', 'permlink': 'vlog-13-introduced-high-level-music-ceo-to-steemit-luxury-clips-inside', 'blog': 'awarenessraiser', 'reblog_on': '1970-01-01T00:00:00', 'entry_id': 41}]
schemelab@metta:~/prg/vivacoin/steem-voting/src/etc$
'''
