# Cats Mini Project

#In this part of the activity you will import the functions from your wallet.py file and create an interface using streamlit

#In this portion of the activity we will create an interface and check our balance in ether to determine if we are able to purchase a cat.

# Imports
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
import pandas as pd



# @TODO: # From crypto_wallet.py import w3, generate_account, get_balance
from crypto_wallet import *


################################################################################
# Cat Information

# Database of cats including their name, digital address, rating and in Ether.
# A single Ether is currently valued at $3,900

cat_database = {
    "Jennifurr": ["Jennifurr", 22],
    "Cheddar": ["Cheddar", 151],
    "Meowise": ["Meowise", 31],
}

# Create a list of the the cats by first names
kitties = list(cat_database.keys())
#kitties = ["Jennifurr", "Cheddar", "Meowise"] # dont hard code!

# Create a get_cats function to display the purchase information from the cats
def get_cats():
    st.write(pd.DataFrame(cat_database.values(), columns=["names", "prices"]))

################################################################################
# Streamlit Code

# @TODO Create Streamlit application headings using `st.markdown` to explain this app is for buying kitties
st.write("This is an app for buying cats!")

# @TODO: Call the `generate_account` function and save it as a variable  called `account`.
account = generate_account()

# @TODO: Call the `get_balance` function and save it as the variable `ether`
ether = get_balance(account.address)

# Disply the balance of ether in the account
st.sidebar.markdown("## Your Balance of Ether")
st.sidebar.markdown(ether)
st.sidebar.markdown("---------")


# @TODO: Create a select box to chose a Cat using `st.sidebar.selectbox`
cat = st.sidebar.selectbox("Select a cat!", kitties)
cat_price = cat_database[cat][1]

# @TODO: Create a header using ` st.sidebar.markdown()` to display cat name and price.
st.sidebar.markdown(f"""
        Kitty: {cat}
        Ether: {cat_price}
""")

# Identify the cat for purchase by name
#cat = cat_database[cat][0]

#@TODO: Create a variable called cat_price to retrive the cat price


#@TODO: create an if else statement to check if the selected cat can be purchased

if (ether >= cat_price):
  st.sidebar.write("If you buy", cat, "for", cat_price, "eth, your account balance will be", ether-cat_price, ".")
  get_cats()
else:
  st.sidebar.write("With a balance of", ether, "ether, you can't buy", cat, "for", cat_price, "eth." )
  get_cats()