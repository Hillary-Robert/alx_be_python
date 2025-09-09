userSalary = int(input("Enter your monthly income: "))
userExpenses = int(input("Enter your total monthly expenses: "))

userSavings = userSalary - userExpenses

rate = 5/100

projectedSavings = userSavings * 12 + (userSavings * 12 * rate)

print(f"Your monthly savings are ${userSavings}.")

print(f"Projected savings after one year, with interest, is: ${projectedSavings}.")