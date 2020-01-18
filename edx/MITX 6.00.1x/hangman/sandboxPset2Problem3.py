balance = 20000
annualInterestRate = 0.18
monthly_interest_rate = (annualInterestRate) / 12.0
low = balance / 12
high = (balance * (1 + monthly_interest_rate)**12) / 12
minimum_fixed_payment = (low + high) / 2

while True:
    due = balance
    for period in range(12):
        unpaid_balance = due - minimum_fixed_payment
        due = unpaid_balance + (unpaid_balance * monthly_interest_rate)
    if (due < 0) and (due > -0.01):
        break
    else:
        if due > 0:
            low = minimum_fixed_payment
        else:
            high = minimum_fixed_payment
    minimum_fixed_payment = (low + high)/2
print('Lowest Payment: ', round(minimum_fixed_payment, 2))
