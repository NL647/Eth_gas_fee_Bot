from web3 import Web3
import time
import os

# Replace with your Telegram bot and chat information
TELEGRAM_BOT_TOKEN = "xxxx"
TELEGRAM_CHAT_ID = "xxxx"
gas_alert = 20

# Connect to an Ethereum node (you can use Infura or run your own node)
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/xxxxxxxx'))

# Function to send a Telegram message using curl
def send_telegram_message(message):
    telegram_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    curl_command = (
        f'curl -s -X POST "{telegram_url}" '
        f'-d "chat_id={TELEGRAM_CHAT_ID}" '
        f'-d "text={message}"'
    )
    # Execute the curl command
    result = os.system(curl_command)
    return result

# Function to get and round the current gas price
def get_rounded_gas_price():
    gas_price = w3.eth.gas_price
    rounded_gas_price = round(gas_price / 1e9)
    return rounded_gas_price

# Function to check gas price and send Telegram message if conditions are met
def check_gas_price_and_notify():
    try:
        rounded_gas_price = get_rounded_gas_price()

        print(f"Current Gas Price: {rounded_gas_price} Gwei")

        if rounded_gas_price <= gas_alert:
            message = f"🚀 Gas Price Alert!\nCurrent Gas Price: {rounded_gas_price} Gwei"
            send_telegram_message(message)
            print("Telegram message sent!")

    except Exception as e:
        # Handle any exceptions that may occur during the process
        error_message = f"An error occurred: {str(e)}"
        print(error_message)
        send_telegram_message(error_message)

# Run the script every 120 seconds
while True:
    check_gas_price_and_notify()
    time.sleep(120)
