from steem.post import Post

p = Post('@awarenessraiser/recognize-how-far-u-have-come-are-you-ready-for-what-it-is-you-want')

p.upvote(voter='supreme')

'''
HERES WHAT HAPPENS IF YOU VOTE ON SOMETHING YOU ALREADY VOTED ON:
schemelab@metta:~/prg/vivacoin/steem-voting/src/etc$ python3 upvote.py
Traceback (most recent call last):
  File "upvote.py", line 5, in <module>
    p.upvote(voter='supreme')
  File "/home/schemelab/install/miniconda3/lib/python3.6/site-packages/steem/post.py", line 234, in upvote
    return self.vote(weight, voter=voter)
  File "/home/schemelab/install/miniconda3/lib/python3.6/site-packages/steem/post.py", line 254, in vote
    return self.commit.vote(self.identifier, weight, account=voter)
  File "/home/schemelab/install/miniconda3/lib/python3.6/site-packages/steem/commit.py", line 358, in vote
    return self.finalizeOp(op, account, "posting")
  File "/home/schemelab/install/miniconda3/lib/python3.6/site-packages/steem/commit.py", line 126, in finalizeOp
    return tx.broadcast()
  File "/home/schemelab/install/miniconda3/lib/python3.6/site-packages/steem/transactionbuilder.py", line 117, in broadcast
    raise e
  File "/home/schemelab/install/miniconda3/lib/python3.6/site-packages/steem/transactionbuilder.py", line 115, in broadcast
    self.steemd.broadcast_transaction(self.json())
  File "/home/schemelab/install/miniconda3/lib/python3.6/site-packages/steem/steemd.py", line 767, in broadcast_transaction
    return self.exec('broadcast_transaction', signed_transaction, api='network_broadcast_api')
  File "/home/schemelab/install/miniconda3/lib/python3.6/site-packages/steembase/http_client.py", line 185, in exec
    return_with_args=return_with_args)
  File "/home/schemelab/install/miniconda3/lib/python3.6/site-packages/steembase/http_client.py", line 205, in _return
    raise RPCError(error_message)
steembase.exceptions.RPCError: 10 assert_exception: Assert Exception
itr->vote_percent != o.weight: You have already voted in a similar way.
    {}
    th_a  steem_evaluator.cpp:1438 do_apply

    {"o":{"voter":"supreme","author":"awarenessraiser","permlink":"vlog-13-introduced-high-level-music-ceo-to-steemit-luxury-clips-inside","weight":10000}}
    th_a  steem_evaluator.cpp:1543 do_apply

    {"op":["vote",{"voter":"supreme","author":"awarenessraiser","permlink":"vlog-13-introduced-high-level-music-ceo-to-steemit-luxury-clips-inside","weight":10000}]}
    th_a  database.cpp:2879 _apply_transaction

    {"trx":{"ref_block_num":45163,"ref_block_prefix":827888289,"expiration":"2017-08-15T11:11:32","operations":[["vote",{"voter":"supreme","author":"awarenessraiser","permlink":"vlog-13-introduced-high-level-music-ceo-to-steemit-luxury-clips-inside","weight":10000}]],"extensions":[],"signatures":["205d9b79b54429049ada218d0595cc1cc0f748e2c7337fe3396ca7a5fcc670a43339b120990762b52f5d9e15c299c00f733cf348761326e5b6ca87702f048d6b15"]}}
    th_a  database.cpp:2883 _apply_transaction

    {"trx":{"ref_block_num":45163,"ref_block_prefix":827888289,"expiration":"2017-08-15T11:11:32","operations":[["vote",{"voter":"supreme","author":"awarenessraiser","permlink":"vlog-13-introduced-high-level-music-ceo-to-steemit-luxury-clips-inside","weight":10000}]],"extensions":[],"signatures":["205d9b79b54429049ada218d0595cc1cc0f748e2c7337fe3396ca7a5fcc670a43339b120990762b52f5d9e15c299c00f733cf348761326e5b6ca87702f048d6b15"]}}
    th_a  database.cpp:660 push_transaction

    {"call.method":"call","call.params":["network_broadcast_api","broadcast_transaction",[{"ref_block_num":45163,"ref_block_prefix":827888289,"expiration":"2017-08-15T11:11:32","operations":[["vote",{"voter":"supreme","author":"awarenessraiser","permlink":"vlog-13-introduced-high-level-music-ceo-to-steemit-luxury-clips-inside","weight":10000}]],"extensions":[],"signatures":["205d9b79b54429049ada218d0595cc1cc0f748e2c7337fe3396ca7a5fcc670a43339b120990762b52f5d9e15c299c00f733cf348761326e5b6ca87702f048d6b15"]}]]}
    th_a  websocket_api.cpp:124 on_message
You have new mail in /var/mail/schemelab
schemelab@metta:~/prg/vivacoin/steem-voting/src/etc$
'''
