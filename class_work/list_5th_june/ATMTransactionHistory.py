# List of customer transactions
transactions = [5000, -2000, 3000, -1000, -500, 7000]

# Calculate current balance

balance = 0

for i in transactions:
    balance = balance + i

print("Current Balance:", balance)

# Count total deposits and withdrawals

deposit_count = 0
withdrawal_count = 0

for i in transactions:
    if i > 0:
        deposit_count += 1
    else:
        withdrawal_count += 1

print("Total Deposits:", deposit_count)
print("Total Withdrawals:", withdrawal_count)

# Find the largest deposit and largest withdrawal

for i in transactions:

    if i > largest_deposit:
        largest_deposit = i

    # Withdrawal means negative value
    if i < largest_withdrawal:
        largest_withdrawal = i

print("Largest Deposit:", largest_deposit)
print("Largest Withdrawal:", largest_withdrawal)

# Create separate lists for deposits and withdrawals

deposits = []
withdrawals = []

for i in transactions:
    if i > 0:
        deposits.append(i)
    else:
        withdrawals.append(i)

print("Deposits List:", deposits)
print("Withdrawals List:", withdrawals)