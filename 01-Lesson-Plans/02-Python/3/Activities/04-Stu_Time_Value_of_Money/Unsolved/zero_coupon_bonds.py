# -*- coding: utf-8 -*-
"""
Zero-Coupon Bond Valuation.

This script will calculate the present value of zero-coupon bonds, compare the present value to the price of the bond, and determine the corresponding action (buy, not buy, neutral).
"""

# @TODO: Create a function to calculate present value

def calculate_present_value(future_value, discount_rate, compounding_periods, years):

    present_value = future_value/ (1 + (discount_rate/ compounding_periods))**(compounding_periods*5)
    return present_value


    














# Intialize the zero-coupon bond parameters, assume compounding period is equal to 1
price = 700
future_value = 1000
discount_rate = .1
compounding_periods = 1
years = 5

# @TODO: Call the calculate_present_value() function and assign to a variables
fair_market_price= calculate_present_value(future_value)

# @TODO: Determine if the bond is worth it
if fair_market_price > price:
    discount = fair_market_price - price
    print(f"The discount is {discount})
elif fair_market_price < price
    print