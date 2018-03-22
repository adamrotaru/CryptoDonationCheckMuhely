import payment
import payment_result

import requests
import json
import datetime

# Checks incoming BTC transactions to a given address, within a time range
# Returns an array of Payments
def BTCCheck(address, time_from, time_to):
    cur_block_height = __getBlockHeight()
    print("Checking BTC", address, "time range", time_from, time_to.__str__(), cur_block_height)
    url = 'https://blockchain.info/en/rawaddr/' + address
    response = requests.get(url)
    #print(response)
    #print(response.status_code)
    payments = []
    if response.status_code != 200:
        print("Error", response.status_code, "cont", response.content)
        return payments
    #print(response.content)
    #data = json.load(response.content)
    data = response.json()
    #print data
    #print("final balance:", data['final_balance'])
    spent_sum = 0
    recd_sum = 0
    #print(len(data['txs']))
    for tx in data['txs']:   #reversed(data['txs']):
        p = __checkTransaction(tx, address, time_from, time_to, cur_block_height)
        if p is not None:
            payments.append(p)
    if len(payments) > 0:
        print("Found", len(payments), "payments")
    return payments

def __checkTransaction(tx, address, time_from, time_to, cur_block_height):
    #print(tx)
    no_confirm = 0
    if 'block_height' in tx:
        block = tx['block_height']
        #print('block_height:', block)
        no_confirm = cur_block_height - block + 1
    time = tx['time']
    #print('time:', time)
    if time <= time_from:
        # old transaction, already checked, ignore
        return None
    if time > time_to:
        # future transactrion, already checked, ignore
        return None
    from_addr = None
    
    #print("spent")
    for inp in tx['inputs']:
        #print inp['prev_out']['spent']
        if inp['prev_out']['spent']:
            from_addr = inp['prev_out']['addr']
            #print(from_addr)
            if from_addr == address:
                #print(inp)
                value = inp['prev_out']['value']
                #spent_sum = spent_sum + value/100000000
                #print('spent value:', value, 'spent total', spent_sum)
    #print("received")
    is_in_out = False
    out_amount = 0
    for out in tx['out']:
        #print(out['spent'])
        #print(out['addr'])
        if out['addr'] == address:
            is_in_out = True
            #print(out)
            value = out['value']
            out_amount = value
            #recd_sum = recd_sum + value/100000000
            #print('recd value:', value, 'recd total', recd_sum)
    #print('result:', tx['result'], 'spent total', spent_sum, 'recd total', recd_sum)
    if is_in_out:
        return payment.Payment(out_amount/100000000, 'BTC', time, address, from_addr, no_confirm)
    return None
    
def __getBlockHeight():
    url = 'https://blockchain.info/en/q/getblockcount'
    return int(requests.get(url).content)

