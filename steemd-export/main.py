# -*- coding: utf-8 -*-

import csv

import pprint
from steem import Steem
from steem.amount import Amount


acct = 'tradeqwik'

s = Steem()
# pprint(s.get_account(acct))

top_record = s.get_account_history(acct, index_from=-1, limit=0)

top_index = top_record[0][0]

print(top_index)


class Transaction(object):

    def __init__(self, record, operation):
        self.record = record
        self.op = operation

    def __str__(self):
        return pprint.pformat(self.record)
    
    def __repr__(self):
        return self.__str__()
            
    @property
    def u(self):
        return u''

    @property
    def info(self):
        return self.record[1]

    @property
    def timestamp(self):
        return self.info['timestamp']

    @property
    def operation(self):
        return self.info['op']
    
    @property
    def operation_detail(self):
        return self.operation[1]   

    @property
    def transaction_type(self):
        return self.operation[0]

    @property
    def transaction_id(self):
        return self.info['trx_id']

    @property
    def memo(self):
        return self.u + self.operation[1]['memo']
    
    currency_index = dict(SBD=0, STEEM=1, SP=2)
    
    def amount2currencyfields(self):
        amount = Amount(self.operation_detail['amount'])
        retval = [0, 0, 0, 0]
        retval[self.currency_index[amount.symbol]] = amount.amount
        return retval

    def build(self):
        return [self.timestamp, self.transaction_type] + self.currency_fields + [self.transaction_id, self.memo]
            
    def reward2currencyfields(self, concat):
        retval = list()
        for t in self.reward_fields:
            if t == 'steem_power':
                retval.append('n/a')
                continue
            l = concat(t)
            m = Amount(self.operation_detail[l]).amount
            retval.append(m)
        return retval
    
class MNoMemo(object):
    def build(self):
        return [self.timestamp, self.transaction_type] + self.currency_fields + [self.transaction_id]
            
class Transfer(Transaction):
    @property
    def currency_fields(self):
        return self.amount2currencyfields()
            
class FillVestingWithdraw(MNoMemo, Transaction):

    @property
    def currency_fields(self):
        return [0, self.operation_detail['deposited'], 0]
    
class ClaimRewardBalance(MNoMemo, Transaction):
    
    @property
    def reward_fields(self):
        return "sbd steem steem_power vests".split()

    @property
    def currency_fields(self):
        return self.reward2currencyfields(lambda t: 'reward_{}'.format(t))
    
class AuthorReward(MNoMemo, Transaction):
    @property
    def reward_fields(self):
        return "sbd steem steem_power vesting".split()
    
    @property
    def currency_fields(self):
        return self.reward2currencyfields(lambda t: '{}_payout'.format(t))
    
class FillOrder(MNoMemo, Transaction):

    @property
    def currency_fields(self):
        return ["TODO", self.operation_detail, 0]
     
class Interest(MNoMemo, Transaction):

    @property
    def currency_fields(self):
        return [Amount(self.operation_detail[self.op]).amount, 0, 0]
    
class WithdrawVesting(MNoMemo, Transaction):

    @property
    def currency_fields(self):
        return [0, 0, Amount(self.operation_detail['vesting_shares']).amount]    
            
class TransferToVesting(MNoMemo, Transaction):

    @property
    def currency_fields(self):
        return [0, self.operation[1], 0, 0]


class Unknown(Transaction):
    
    def build(self):
        # currency_fields = [0, 0 , 0, 0]
        info = self.u + pprint.pformat(self.info).replace('\n', ' ')
        return [self.timestamp, self.transaction_type, "TODO", info]   
    
class Ignore(Transaction):
    
    def build(self):
        # currency_fields = [0, 0 , 0, 0]
        info = self.u + pprint.pformat(self.info).replace('\n', ' ')
        return [self.timestamp, self.transaction_type, "IGNORE", info]   
    
def operation(r):
    return r[1]['op'][0]



def bless_row(r):
    op = r[1]['op'][0]
    ignore = ['comment_options', 'account_witness_vote', 'curation_reward', 
              'delete_comment', 'account_create', 'custom_json', 
              'vote', 'author_reward', 'comment', 'account_witness_proxy'
              ]
    dispatch = dict(
            transfer=Transfer, transfer_to_vesting=TransferToVesting,
            interest=Interest, fill_vesting_withdraw=FillVestingWithdraw,
            claim_reward_balance=ClaimRewardBalance, fill_order=FillOrder,
            author_reward=AuthorReward, withdraw_vesting=WithdrawVesting
            )
    
    if op in dispatch:
        return dispatch[op](r, op)
    
    if op in ignore:
        return Ignore(r, op)

    return Unknown(r, op)


ops = set()

with open('out.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(
        "Date TransactionType SBD Steem SteemPower Vests TransactionID Memo".split())

    for record in s.get_account_history(acct, index_from=-1, limit=top_index):
        ops.add(record[1]['op'][0])
        r = bless_row(record)
        print(str(r).encode('utf-8'))
        # print(u'' + MyPP().pformat(r))
        writer.writerow(r.build())
        
    print("OPS:{}".format(ops))
