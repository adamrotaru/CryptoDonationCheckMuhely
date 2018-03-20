import btc_checker
import eth_checker
import payment
import mailer

import requests
import json
import time

#print('cur time', time.timezone)
cur_time = int(time.time()) + 600
print('cur time', cur_time)
time0 = 1514000000

# BLMűh
#btc_address = '12QpKTP3KnHg7ZqEAEyJTq6pGX7xjWTvGG'
#btc_checker.BTCCheck(btc_address, time0, cur_time)

# test1
#btc_address = '19M3CezEbdiv9EZKryi89is5KcM3QzStkL'  # test1 1521148506 1520130638 1514346984
#btc_checker.BTCCheck(btc_address, time0, cur_time)
#CheckAddress(btc_address, time0, 1514346990, cur_block_height)
#CheckAddress(btc_address, 1514346990, 1520130650, cur_block_height)
#CheckAddress(btc_address, 1520130650, cur_time, cur_block_height)

# test2
#btc_address = '39du52dRqNHCcErFuoFCqhHQs2fczQUqBL'
#CheckAddress(btc_address, time0, cur_time, cur_block_height)

# test1
eth_address = '0x84b14bdfa2eb6b03c78e36b528675396ef40de0a'  
# BLMuh
#eth_address = '0x0197F32CdccE55A8c34a2c000AdD1adFdAf97f14'

payments = eth_checker.ETHCheck(eth_address)

mailer.send_payments(payments)

