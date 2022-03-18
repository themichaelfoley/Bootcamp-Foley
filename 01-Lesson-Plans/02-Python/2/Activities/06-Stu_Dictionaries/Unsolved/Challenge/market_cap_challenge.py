# -*- coding: utf-8 -*-
"""
Student Activity: Market Capitalization.

This script showcases the use of Python Dicts to determine the
bank names associated with the corresponding market cap ranges.
"""

# Banks and Market Caps
#-----------------------
# JP Morgan Chase: 327
# Bank of America: 302
# Citigroup: 173
# Wells Fargo: 273
# Goldman Sachs: 87
# Morgan Stanley: 72
# U.S. Bancorp: 83
# TD Bank: 108
# PNC Financial Services: 67
# Capital One: 47
# FNB Corporation: 4
# First Hawaiian Bank: 3
# Ally Financial: 12
# Wachovia: 145
# Republic Bancorp: .97

# @TODO: Initialize a dictionary of banks and market caps (in billions)
banks = { 
    "JPM" : 327,
    "BoA" : 302,
    "Citi": 173,
    "Wells": 273,
    "Goldman": 87,
    "Morgan": 72,
    "USB": 83,
    "TD": 108,
    "PNC": 67,
    "Cap1": 47,
    "FNB": 4,
    "FHB": 3,
    "Ally": 12,
    "Wachovia": 145,
    "RepBank": .97,


}















# @TODO: Change the market cap for 'Citigroup'
banks["Citi"]= 200
print(banks)

# @TODO: Add a new bank and market cap pair
banks["FirstBank"]= 86
print(banks)

# @TODO: Remove a bank from the dictionary
del banks["Wells"]
print(banks)

# @TODO: Initialize metric variables
maxCap= max(banks)
minCap= min(banks)

print(f"Bank with Highest market capitalization is : {maxCap}")
print(f"Bank with Lowest market capitalization is : {minCap}")

# @TODO: Initialize minimum key-value pair
min(banks)


# @TODO: Initialize maximum key-value pair
max(banks)



# Mega Cap: Firms with a market capitalization over $300 billion.
# Large Cap: Firms with a market capitalization over 10 billion. ...
# Mid Cap: A market capitalization between $2 and $10 billion.
# Small Cap: A market capitalization between $300 million and $2 billion.

# @TODO: Initialize market cap lists





# @TODO: Iterate over key-value pairs of the dictionary




    # @TODO: Calculate sum of market caps and number of banks in the dictionary



    # @TODO: Logic to determine min value and associated key







    # @TODO: Logic to determine max value and associated key




    # @TODO: Group banks by categories of market caps










# @TODO: Calculate average market cap of banks in the dictionary


# @TODO: Print the metrics
