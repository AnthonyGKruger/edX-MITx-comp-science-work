#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 07:59:30 2018

@author: anthony
"""

balance = float(input('what is the balance of your credit cards that you need to pay?   '))
years = int(input('\nHow many years would you like to take to pay off the debt?   ')) * 12
annualInterestRate = 0.2
monthly_unpaid_balance = 0
monthly_interest_rate = annualInterestRate / years
low_bal = balance / years
high_bal = (balance * (1 + monthly_interest_rate) ** years) / years
min_month_payment = (low_bal + high_bal) / 2.0
while True:
    rem_balance = balance
    for i in range(years):
        monthly_unpaid_balance = rem_balance - min_month_payment
        rem_balance = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)
    if (rem_balance <= 0) and (rem_balance >= -0.01):
        break
    else:
        if rem_balance > 0:
            low_bal = min_month_payment
        else:
            high_bal = min_month_payment
    min_month_payment = (low_bal + high_bal) / 2.0
print('/nLowest Payment: ', round(min_month_payment,2))
