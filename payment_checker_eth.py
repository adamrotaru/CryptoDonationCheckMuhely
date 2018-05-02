import payment_checker_result
import config

import requests
import datetime

# Checks incoming ETH transactions to a given address, within a time range
# Returns a PaymentResult
def ETHCheck(address_to, time_from, time_to, min_confirmations = 3):
    print("Checking ETH", address_to, "time range", time_from, time_to)
    apiKeyToken = config.get()["etherscan_apiKeyToken"]
    # address balance
    #url = 'https://api.etherscan.io/api?module=account&action=balance&address=' + address_to + '&tag=latest&apikey=' + apiKeyToken
    # transactions
    url = 'https://api.etherscan.io/api?module=account&action=txlist&address=' + address_to + '&startblock=0&endblock=99999999&sort=asc&apikey=' + apiKeyToken
    # page=1&offset=10

    resp = requests.get(url)
    #print(resp.status_code)
    
    data = resp.json()
    #print(data)
    #print(data['status'])
    payments = []
    if resp.status_code != 200 or data is None or data['status'] != '1':
        print("Error retrieving transactions or no transactions", resp.status_code)
        print(data)
        #print(data['status'])
        #print(data['message'])
        return payment_checker_result.PaymentResult('ETH', address_to, time_from, time_to)
    #print(data['result'])
    for tx in data['result']:
        p = __checkTransaction(tx, address_to, time_from, time_to)
        if p is not None:
            payments.append(p)
    # compute sums
    sum_confd = 0
    sum_nonconfd = 0
    for p in payments:
        sum_nonconfd = sum_nonconfd + p.amount
        if (p.no_confirm >= min_confirmations):
            sum_confd = sum_confd + p.amount
    res = payment_checker_result.PaymentResult('ETH', address_to, time_from, time_to, sum_confd, sum_nonconfd, payments)
    res.print()
    return res

def __checkTransaction(tx, address_to, time_from, time_to):
    #print(tx)
    #print('blockNumber', tx['blockNumber'])
    time = int(tx['timeStamp'])
    #print('timeStamp', time)
    if time <= time_from:
        # old transaction, already checked, ignore
        return None
    if time > time_to:
        # future transactrion, already checked, ignore
        return None
    to_addr = tx['to']
    value = int(tx['value']) / 1000000000000000000
    #print('to_addr', to_addr)
    if to_addr.upper() == address_to.upper() and value != 0:
        from_addr = tx['from']
        #print('from', from_addr)
        #print('value', value)
        confirmations = tx['confirmations']
        #print('confirmations', confirmations)
        #print(tx)
        p = payment_checker_result.PaymentInfo(value, time, address_to, from_addr, confirmations)
        return p
    return None
