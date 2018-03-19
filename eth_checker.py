import payment

import requests

# etherscan API key
apiKeyToken = 'C5I42D9TYVZZGVQZKY6KU8TEUBY912STGF' 

def ETHCheck(address):
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
    if resp.status_code != 200 or data is None or data['status'] != '1':
        print("Error", resp.status_code)
        print(data['status'])
        print(data['message'])
        return None
    #print(data['result'])
    payments = []
    for tx in data['result']:
        #print(tx)
        #print('blockNumber', tx['blockNumber'])
        timeStamp = tx['timeStamp']
        #print('timeStamp', timeStamp)
        to_addr = tx['to']
        value = int(tx['value']) / 1000000000000000000
        #print('to_addr', to_addr)
        if to_addr.upper() == address.upper() and value != 0:
            from_addr = tx['from']
            print('from', from_addr)
            print('value', value)
            confirmations = tx['confirmations']
            print('confirmations', confirmations)
            #print(tx)
            p = payment.Payment(value, 'ETH', timeStamp, address, from_addr, confirmations)
            payments.append(p)
    return payments


