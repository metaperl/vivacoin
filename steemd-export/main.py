# -*- coding: utf-8 -*-

# Core
import csv
import pprint

# 3rd Party
import argh
from steem import Steem
from steem.amount import Amount
from steem.account import Account

# Local

 

def currency2pair(c):
    if c == 'BTC':
        return "USDT_BTC"
    else:
        return "BTC_"+c

def historical_cost_url(start, currency):
    width = 300 # 5 minute candle
    end = start + 10000
    url =  "https://poloniex.com/public?command=returnChartData&currencyPair={}".format(currency)
    url += "&start={}&end={}&period={}".format(start, end, width)
    return url
            

def _historical_cost_for(currency, date):
    print("Passed-in currency={} date={}".format(currency, date))
    from datetime import datetime
    from time import mktime, strptime
    s = strptime(date, "%Y-%m-%dT%H:%M:%S")
    print("S: {}".format(s))
    start = datetime.fromtimestamp(mktime(s)).timestamp()
    
    import requests

    url = historical_cost_url(start, currency)
    print("Historical Cost URL={}".format(url))
    r = requests.get(url)
    j = r.json()
    print("JSON: {}".format(j))
    return r.json()[0]['close']

def historical_cost_for(currency, date):
    if currency == 'BTC':
        return _historical_cost_for('USDT_BTC', date)
    else:
        return _historical_cost_for('BTC_'+currency, date)    

def amount_to_usd(amount, date):
    usd_per_btc = historical_cost_for('BTC', date)
    if amount.symbol == 'SBD':
        btc_cost = historical_cost_for(amount.symbol, date)
        return sbd_to_usd(amount.amount, btc_cost, usd_per_btc), btc_cost
    if amount.symbol == 'STEEM':
        btc_cost = historical_cost_for(amount.symbol, date)
        return steem_to_usd(amount.amount, btc_cost, usd_per_btc), btc_cost
    
    return "CANT CONVERT", "NOCONV"


def x_to_usd(x, btc_per_x, usd_per_btc):
    x_to_btc = x * btc_per_x
    btc_to_usd = x_to_btc * usd_per_btc
    return btc_to_usd

def steem_to_usd(units_of_steem, btc_per_steem, usd_per_btc):
    return x_to_usd(units_of_steem, btc_per_steem, usd_per_btc)

def sbd_to_usd(units_of_sbd, btc_per_sbd, usd_per_btc):
    return x_to_usd(units_of_sbd, btc_per_sbd, usd_per_btc)


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
    def operation_amount(self):
        return Amount(self.operation_detail['amount'])

    @property
    def transaction_type(self):
        return self.operation[0]

    @property
    def transaction_id(self):
        return self.info['trx_id']

    @property
    def memo(self):
        return self.u + self.operation[1]['memo']

    currency_index = dict(SBD=0, STEEM=1, SP=2, VESTS=3)
    
    def fiatify(self, amount):
        usd, btc = amount_to_usd(amount, self.timestamp)
        return [usd, btc]


    def amount2currencyfields(self, amount_field='amount'):
        amount = Amount(self.operation_detail[amount_field])
        retval = [0, 0, 0, 0]
        retval[self.currency_index[amount.symbol]] = amount.amount
        retval = self.fiatify(amount) + retval
        return retval

    def build(self):
        return [self.timestamp, self.transaction_type] + self.currency_fields + [self.transaction_id, self.memo]

    def reward2currencyfields(self, concat):
        retval = list()
        usd_btc = ['?', '?']
        for t in self.reward_fields:
            print("RC2F reward field="+t)
            if t == 'steem_power':
                retval.append('n/a')
                continue
            l = concat(t)
            a = Amount(self.operation_detail[l])
            m = a.amount
            if m > 0 and ('vest' not in l):
                usd_btc = self.fiatify(a)
            retval.append(m)
            
        retval = usd_btc + retval
        print("RC2F returning:{}".format(retval))
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
        a = Amount(self.operation_detail['deposited'])
        usd_btc = self.fiatify(a)
        return usd_btc + [0, a.amount, 0]

class ClaimRewardBalance(MNoMemo, Transaction):

    @property
    def reward_fields(self):
        return "sbd steem steem_power vests".split()

    @property
    def currency_fields(self):
        return self.reward2currencyfields(lambda t: 'reward_{}'.format(t))

class CurationReward(MNoMemo, Transaction):
    @property
    def currency_fields(self):
        # return [0, 0, 0, Amount(self.operation_detail['reward']).amount]
        return self.amount2currencyfields('reward')

class AuthorReward(MNoMemo, Transaction):
    @property
    def reward_fields(self):
        return "sbd steem steem_power vesting".split()

    @property
    def currency_fields(self):
        return self.reward2currencyfields(lambda t: '{}_payout'.format(t))

class FillOrder(MNoMemo, Transaction):

    def pay_logic(self, label_prefix):

        def get(label_suffix):
            return self.operation_detail["{}_{}".format(label_prefix, label_suffix)]

        owner = get('owner')
        amount = Amount(get('pays')).amount

        return -1*amount if owner == 'tradeqwik' else amount

    @property
    def currency_fields(self):
        return ["Sherry", "Please advise"] + [self.pay_logic('open'), self.pay_logic('current'), 0, 0]

class Interest(MNoMemo, Transaction):

    @property
    def currency_fields(self):
        return ['i?', 'i?'] + [Amount(self.operation_detail[self.op]).amount, 0, 0]

class WithdrawVesting(MNoMemo, Transaction):

    @property
    def currency_fields(self):
        return ['?', '?'] + [0, 0, Amount(self.operation_detail['vesting_shares']).amount]

class TransferToVesting(MNoMemo, Transaction):

    @property
    def currency_fields(self):
        a = self.operation_amount
        print("Attempting to instance: {}".format(a))
        usd_btc = self.fiatify(a)
        return usd_btc + [0, a.amount, 0, 0]


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
    ignore = ['comment_options', 'account_witness_vote',
              'delete_comment', 'account_create', 'custom_json',
              'vote', 'author_reward', 'comment', 'account_witness_proxy',
              'limit_order_create', 'limit_order_cancel'
              ]
    dispatch = dict(
            transfer=Transfer, transfer_to_vesting=TransferToVesting,
            interest=Interest, fill_vesting_withdraw=FillVestingWithdraw,
            claim_reward_balance=ClaimRewardBalance, fill_order=FillOrder,
            author_reward=AuthorReward, withdraw_vesting=WithdrawVesting,
            curation_reward=CurationReward
            )

    if op in dispatch:
        return dispatch[op](r, op)

    if op in ignore:
        return None

    return Unknown(r, op)


def process(acct, index_from, limit):
    ops = set()

    s = Steem()
    
    print(s.get_account(acct))

    top_record = s.get_account_history(acct, index_from=-1, limit=0)
    top_index = top_record[0][0]
    print("TOP INDEX: {}".format(top_index))
    
    with open('sherry3.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(
            "Date TransactionType TotalAsUSD UnitAsBTC SBD Steem SteemPower Vests TransactionID Memo".split())

        for record in s.get_account_history(acct, index_from, limit):
            r = bless_row(record)
            if not r:
                continue
            print(str(r).encode('utf-8'))
            ops.add(r.op)
            writer.writerow(r.build())

        print("OPS:{}".format(ops))

def main(index_from, limit, acct='tradeqwik'):
    process(acct, index_from, limit)

argh.dispatch_command(main)

