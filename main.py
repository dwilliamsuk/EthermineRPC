# EthermineRPC Made by Dan https://github.com/TheJaffaMeme
print("EthermineRPC Made by Dan https://github.com/TheJaffaMeme")

import requests
from pypresence import Presence
import time
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

MinerID = str(config['ETHERMINE']['MinerAddress'])
client_id = int(config['DISCORDRPC']['ClientID'])
large_image = str(config['DISCORDRPC']['LargeImage'])
large_text = str(config['DISCORDRPC']['LargeImageText'])
refreshtime = int(config['GENERAL']['RefreshTime'])
RPC = Presence(client_id)

RPC.connect()

def getstats(ID):
    url = "https://api.ethermine.org/miner/" + ID + "/dashboard"
    response = requests.request("GET", url)
    return(response.json())

def lateststats(stats):
    if stats['status'] == "ERROR":
        print("Error! " + stats['error'])
        quit()
    latest = stats['data']['currentStatistics']
    monies = stats['data']['currentStatistics']['unpaid']
    workers = stats['data']['currentStatistics']['activeWorkers']
    url = "https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=BTC,USD"
    response = requests.request("GET", url)
    pricing = response.json()
    BTC = pricing['BTC']
    USD = pricing['USD']
    return [latest, monies, workers, BTC, USD]

def updateRPC():
    stats = lateststats(getstats(MinerID))
    eth = stats[1] / 1000000000000000000
    eth = round(eth, 5)
    btc = round(eth * stats[3], 5)
    usd = eth * stats[4]
    details = str(eth)+ ' ETH'
    state = '${:.2f}'.format(usd)+ ' USD'
    RPC.update(state=state, details=details, start=time.time(), end=str(int(time.time()+refreshtime)), buttons=[{"label": "Ethermine Dashboard", "url": "https://ethermine.org/miners/" +MinerID+ "/dashboard"}], large_image=large_image, large_text=large_text)
    return

try:
    while True:
        updateRPC()
        print("Updated RPC, Sleeping for " +str(refreshtime)+ " seconds")
        time.sleep(refreshtime)
except KeyboardInterrupt:
    print("Shutting Down...")
    quit()
