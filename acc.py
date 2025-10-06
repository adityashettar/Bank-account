deposit_amount = float(input("Enter the deposit amount: "))
deposit_amount = float(input("Enter the deposit amount: "))
initial_balance = float(input("Enter the initial balance: "))
deposit_amount = float(input("Enter the deposit amount: "))
updated_balance = initial_balance + deposit_amount
print("Updated balance after deposit:", updated_balance)

# Ask the user for the withdrawal amount
withdraw_amount = float(input("Enter the withdrawal amount: "))

# Calculate the new balance after withdrawal
new_balance = updated_balance - withdraw_amount
print("Balance after withdrawal:", new_balance)