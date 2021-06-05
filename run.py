import sys
import requests
import socket
import urllib3
import config_bybit
import config_binance
import trade_bybit
import trade_binance
from termcolor import colored
from binance.exceptions import BinanceAPIException
from apscheduler.schedulers.blocking import BlockingScheduler

bybit   = sys.argv[-1].upper() == "BYBIT"
binance = sys.argv[-1].upper() == "BINANCE"

def run_binance():
    if config_binance.live_trade: print(colored("LIVE TRADE IS ENABLED\n", "green"))
    else: print(colored("THIS IS BACKTESTING\n", "red"))

    def making_money_from_binance():
        for i in range(len(config_binance.coin)):
            trade_binance.lets_make_some_money(i)

    if config_binance.enable_scheduler:
        scheduler = BlockingScheduler()
        scheduler.add_job(making_money_from_binance, 'cron', second='0')
        # scheduler.add_job(making_money_from_binance, 'cron', minute='0,10,20,30,40,50')
        scheduler.start()
    else: making_money_from_binance()

def run_bybit():
    if config_bybit.live_trade: print(colored("LIVE TRADE IS ENABLED\n", "green"))
    else: print(colored("THIS IS BACKTESTING\n", "red"))

    def making_money_from_bybit():
        for i in range(len(config_bybit.coin)):
            trade_bybit.lets_make_some_money(i)

    if config_bybit.enable_scheduler:
        scheduler = BlockingScheduler()
        scheduler.add_job(making_money_from_bybit, 'cron', second='0')
        # scheduler.add_job(making_money_from_bybit, 'cron', minute='0,10,20,30,40,50')
        scheduler.start()
    else: making_money_from_bybit()

# RUN THE SCRIPT !!!
try:
    if binance:
        print(colored("\nTHE BOT IS RUNNING...\n", "green"))
        run_binance()
    elif bybit:
        print(colored("\nTHE BOT IS RUNNING...\n", "green"))
        run_bybit()
    else:
        print(colored("\nMAKE SURE YOU READ THE README.md 100 TIMES BEFORE YOU USE THE PROGRAM !!!\n", "red"))
        sys.exit()

except (socket.timeout,
        BinanceAPIException,
        urllib3.exceptions.ProtocolError,
        urllib3.exceptions.ReadTimeoutError,
        requests.exceptions.ConnectionError,
        requests.exceptions.ConnectTimeout,
        requests.exceptions.ReadTimeout,
        ConnectionResetError, KeyError, OSError) as e: print(e)

except KeyboardInterrupt: print("\n\nAborted.\n")