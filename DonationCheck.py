import btc_checker
import payment

import requests
import json
import time

#print('cur time', time.timezone)
cur_time = int(time.time()) + 600
print('cur time', cur_time)
time0 = 1514000000

# BLMűh
address = '12QpKTP3KnHg7ZqEAEyJTq6pGX7xjWTvGG'
btc_checker.checkBTC(address, time0, cur_time)

# test1
address = '19M3CezEbdiv9EZKryi89is5KcM3QzStkL'  # test1 1521148506 1520130638 1514346984
btc_checker.checkBTC(address, time0, cur_time)
#CheckAddress(address, time0, 1514346990, cur_block_height)
#CheckAddress(address, 1514346990, 1520130650, cur_block_height)
#CheckAddress(address, 1520130650, cur_time, cur_block_height)

# test2
#address = '39du52dRqNHCcErFuoFCqhHQs2fczQUqBL'
#CheckAddress(address, time0, cur_time, cur_block_height)
