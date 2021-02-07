# EthermineRPC
Discord Rich Presence for https://ethermine.org/ written in Python

![EthermineRPC Example](https://i.jaffasite.ga/2021/02/EthermineRPC.png)

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
pip install -r requirements.txt
```

## Configuration
Edit config.ini as follows:

| Key | Value |
| ------ | ------ |
| MinerAddress | Your Ethereum Miner Address |
| ClientID | Your RPC Client ID (Check Important Notes) |
| LargeImage | RPC Art Asset Name To Use (Check Important Notes) |
| LargeImageText | Large Image Asset Text |
| ShowDashButton | Option to Show or Hide the Dashboard Button - Can be 'True' or 'False' |
| RefreshTime | Refresh Time (in seconds) |

## Usage

```bash
python main.py
```

## Important Notes
You __NEED__ to create an application [here](https://discord.com/developers/applications/) and grab your client ID, then create an "Art Asset" that will be displayed next to your status.

I'd recommend you __keep the refresh time at or above 120 seconds__ as __Ethermine only update information every 2 minutes__

I use [api.ethermine.org](https://ethermine.org) and [min-api.cryptocompare.com](https://cryptocompare.com) to get information on your mining stats and current pricing for Ethereum in USD and BTC. __I am not associated with either of these sites and cannot be held responsible for their content or actions.__
