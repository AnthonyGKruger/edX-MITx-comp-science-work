
balance = 735
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
month = 0
due = balance
minimum_fixed_payment = 10

while True:
    due = balance
    for period in range(12):
        unpaid_balance = due - minimum_fixed_payment
        interest = (annualInterestRate/12) * unpaid_balance
        due = unpaid_balance + interest
    if unpaid_balance > 0:
        minimum_fixed_payment += 10
    elif unpaid_balance <= 0:
        print('Lowest payment: ', minimum_fixed_payment)
        break

