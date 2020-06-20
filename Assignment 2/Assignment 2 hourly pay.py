hours = int(input("Enter the hours worked:"))

pay = int(input("Enter the hourly pay:"))

grossPay = hours * pay

print("Gross Pay: $",grossPay)

fedTax = .25 * grossPay

stateTax = .15 * grossPay

print("Fed Tax Deducted: $", fedTax)

print("State Tax Deducted: $", stateTax)

tax = fedTax+stateTax

print("Total Deduction: $",tax)

netPay = grossPay-tax

print("Net Pay: $",netPay)
