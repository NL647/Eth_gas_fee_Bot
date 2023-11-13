# Eth_gas_fee_Bot
A Python3 Telegram bot to alert you when gas fee are low on Ethereum Network.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Web3.\
[Web3](https://pypi.org/project/web3/)

```bash
pip install web3
```

## Usage
You will need an [Infura](https://www.infura.io/) api key. \
Set up variables in the main.py script
```bash
TELEGRAM_BOT_TOKEN = "xxxxxx"
TELEGRAM_CHAT_ID = "xxxxx"
gas_alert = 20
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/xxxxxx'))
```

```bash
python3 main.py
```
Or using screen to run it the background .

```bash
sudo apt install screen
screen -dmS bot_gas python3 main.py
```
