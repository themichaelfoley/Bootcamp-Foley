# Ethereum Account Functions

################################################################################

# Imports
import os
import requests
from dotenv import load_dotenv
load_dotenv()
from bip44 import Wallet
from web3 import Account
from web3 import middleware
from web3.gas_strategies.time_based import medium_gas_price_strategy
from web3 import Web3

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))
################################################################################

# Create a function called `generate_account` that automates the Ethereum
# account creation process
def generate_account():
    """Create a digital wallet and Ethereum account from a mnemonic seed phrase."""
    # Access the mnemonic phrase from the `.env` file
    mnemonic = os.getenv("MNEMONIC")

    # Create Wallet object instance
    wallet = Wallet(mnemonic)

    # Derive Ethereum private key
    private, public = wallet.derive_account("eth")

    # Convert private key into an Ethereum account
    account = Account.privateKeyToAccount(private)

    # Return the account from the function
    return account


# @TODO
# Create a function called `get_balance`, it should convert the wei balance of the account to ether, and returns the value of ether

def get_balance(address):

    wei_balance = w3.eth.get_balance(address)

    ether = w3.fromWei(wei_balance, "ether")

    return ether




# @TODO
# Create a function called `send_transaction` that creates a raw transaction, signs it, and sends it. Return the confirmation hash from the transaction.
def send_transaction(account, receiver, ether):
    
    w3.eth.setGasPriceStrategy(medium_gas_price_strategy)

    wei_value = w3.toWei(ether, "ether")

    raw_tx = {
        "to":receiver,
        "from":account.address,
        "value":wei_value
    }

    gas_estimate = w3.eth.estimateGas(raw_tx)

    #gas_price = w3.eth.generateGasPrice(raw_tx)

    raw_tx.update({
        "gas":gas_estimate,
        "gasPrice": 0,
        "nonce": w3.eth.getTransactionCount(account.address)
    })

    signed_tx = account.signTransaction(raw_tx)

    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)

    return tx_hash.hex()