import payment
import payment_result
import config

import requests
import datetime

def ETHCheck(address, time_from, time_to):
    print("Checking ETH", address, "time range", time_from, time_to)
    apiKeyToken = config.get()["etherscan_apiKeyToken"]
    # address balance
    #url = 'https://api.etherscan.io/api?module=account&action=balance&address=' + address + '&tag=latest&apikey=' + apiKeyToken
    # transactions
    url = 'https://api.etherscan.io/api?module=account&action=txlist&address=' + address + '&startblock=0&endblock=99999999&sort=asc&apikey=' + apiKeyToken
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
        return payments
    #print(data['result'])
    for tx in data['result']:
        p = __checkTransaction(tx, address, time_from, time_to)
        if p is not None:
            payments.append(p)
    if len(payments) > 0:
        print("Found", len(payments), "payments")
    return payments

def __checkTransaction(tx, address, time_from, time_to):
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
    if to_addr.upper() == address.upper() and value != 0:
        from_addr = tx['from']
        #print('from', from_addr)
        #print('value', value)
        confirmations = tx['confirmations']
        #print('confirmations', confirmations)
        #print(tx)
        p = payment.Payment(value, 'ETH', time, address, from_addr, confirmations)
        return p
    return None
