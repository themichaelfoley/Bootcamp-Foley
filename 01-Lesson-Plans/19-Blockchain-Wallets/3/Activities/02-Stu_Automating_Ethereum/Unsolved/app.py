# Streamlit Application

# Imports
import streamlit as st
from web3 import Web3

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))

# @TODO
# Update the imports for the functions coming from ethereum.py
from ethereum import generate_account


################################################################################
# Streamlit Code

# Streamlit application headings
st.markdown("# Automating Ethereum with Streamlit!")

#######################################

# Generate the Ethereum account
account = generate_account()

#######################################

# The Ethereum Account Address
st.text("\n")
st.text("\n")
st.markdown("## Ethereum Account Address:")

# Write the Ethereum account address to the Streamlit page
st.write(account.address)

#######################################

# Display the Etheremum Account balance
st.text("\n")
st.text("\n")
st.markdown("## Ethereum Account Balance:")

# @TODO
# Call the `get_balance` function and write the account balance to the screen
#wei_balance = w3.fromWei(w3.eth.getBalance('0x756D8FCf4d1b8e97405C2C926d50D12FAb061bcD'))
wei_balance = w3.eth.get_balance("0x756D8FCf4d1b8e97405C2C926d50D12FAb061bcD")
eth_balance = w3.fromWei(wei_balance, "ether")
st.write(eth_balance)
#print(eth_balance)
#######################################

# An Ethereum Transaction
st.text("\n")
st.text("\n")
st.markdown("## An Ethereum Transaction:")


# @TODO
# Create inputs for the receiver address and ether amount
receiver = st.text_input()#"0x53A54d758d77251Bc834e6D25f1AF39A0db2D8f1"



# @TODO
# Create a button that calls the `send_transaction` function and returns the transaction hash
