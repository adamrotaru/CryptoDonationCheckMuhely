import btc_checker
import eth_checker
import payment
import payment_result
import mailer
import config
import requests
import json
import time


#print('cur time', time.timezone)
cur_time = int(time.time()) + 600
print('cur time', cur_time)
time0 = 1514000000

# test1
#btc_address = '19M3CezEbdiv9EZKryi89is5KcM3QzStkL'  # test1 1521148506 1520130638 1514346984
#paymentRes = btc_checker.BTCCheck(btc_address, time0, cur_time)
#CheckAddress(btc_address, time0, 1514346990, cur_block_height)
#CheckAddress(btc_address, 1514346990, 1520130650, cur_block_height)
#CheckAddress(btc_address, 1520130650, cur_time, cur_block_height)
# test2
#btc_address = '39du52dRqNHCcErFuoFCqhHQs2fczQUqBL'
#CheckAddress(btc_address, time0, cur_time, cur_block_height)

payments = []
btc_address = config.get()["btc_address"]
if len(btc_address) > 0:
    btc_p = btc_checker.BTCCheck(btc_address, time0, cur_time)
    payments.extend(btc_p)

eth_address = config.get()["eth_address"]
if len(eth_address) > 0:
    eth_p = eth_checker.ETHCheck(eth_address, time0, cur_time)
    payments.extend(eth_p)

paymentRes = payment_result.PaymentResult(time0, cur_time, payments)
paymentRes.print()
if (paymentRes.count() > 0):
    mailer.send_payments(paymentRes)
else:
    print("No new payments to send")
