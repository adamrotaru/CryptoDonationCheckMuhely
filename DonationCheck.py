import payment_checker_btc
import payment_checker_eth
import payment
import payment_result_multi
import mailer
import config

import requests
import json
import time
import datetime


def DonationCheckTime(time_from, time_to):
    print("Checking payments, time range", datetime.datetime.fromtimestamp(time_from).__str__(), "-", datetime.datetime.fromtimestamp(time_to).__str__(), " UTC")
    res = payment_result_multi.PaymentResultMulti(time_from, time_to, [])
    btc_address = config.get()["btc_address"]
    if len(btc_address) > 0:
        btc_p = payment_checker_btc.BTCCheck(btc_address, time_from, time_to, config.get()["btc_min_confirmations"])
        for p in btc_p.payments:
            res.add(p.amount, btc_p.currency, p.timestamp, p.to_addr, p.from_addr, p.no_confirm)

    eth_address = config.get()["eth_address"]
    if len(eth_address) > 0:
        eth_p = payment_checker_eth.ETHCheck(eth_address, time_from, time_to)
        for p in eth_p.payments:
            res.add(p.amount, eth_p.currency, p.timestamp, p.to_addr, p.from_addr, p.no_confirm)

    return res
    

def DonationCheckAndMail():
    state = config.get_state()
    lastcheck = int(state["lastcheck"])
    # current UTC time
    cur_time = int(time.time()) # + time.timezone
    paymentRes = DonationCheckTime(lastcheck, cur_time)
    try:
        state["lastcheck"] = cur_time
        config.save_state(state)
    except:
        pass
    paymentRes.print()
    if (paymentRes.count() > 0):
        mailer.send_payments(paymentRes)
    else:
        print("No new payments to send")
    
def DonationCheckLoop():
    periodMin = float(config.get()["checkPeriodMins"])
    periodSec = int(periodMin * 60)
    while True:
        DonationCheckAndMail()
        print("Waiting for", periodMin, "minutes ...")
        time.sleep(periodSec)



config.get()
config.get_state()

DonationCheckLoop()




# test1
#btc_address = '19M3CezEbdiv9EZKryi89is5KcM3QzStkL'  # test1 1521148506 1520130638 1514346984
#paymentRes = payment_checker_btc.BTCCheck(btc_address, time0, cur_time)
#CheckAddress(btc_address, time0, 1514346990, cur_block_height)
#CheckAddress(btc_address, 1514346990, 1520130650, cur_block_height)
#CheckAddress(btc_address, 1520130650, cur_time, cur_block_height)
# test2
#btc_address = '39du52dRqNHCcErFuoFCqhHQs2fczQUqBL'
#CheckAddress(btc_address, time0, cur_time, cur_block_height)
