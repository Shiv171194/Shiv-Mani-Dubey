print("💰 Welcome to Budget Helper 💰")

# Ask user for monthly income
income = float(input("Enter your monthly income: "))

# Ask for common expenses
rent = float(input("Enter rent amount: "))
groceries = float(input("Enter groceries expense: "))
travel = float(input("Enter travel expense: "))
other = float(input("Enter other expenses: "))

# Total expenses
total_expense = rent + groceries + travel + other

# Calculate balance
balance = income - total_expense

print("\n📊 Summary:")
print("Total Income:", income)
print("Total Expenses:", total_expense)
print("Remaining Balance:", balance)

# Give a suggestion
if balance > 0:
    print("✅ You're managing well! Maybe save some money this month.")
elif balance == 0:
    print("⚠️ You spent exactly what you earned. Be cautious!")
else:
    print("❌ You are overspending! Try to reduce your expenses.")
