Employee = input("Please Enter Your Name: ")
Salary = float(input("Please Enter Your Salary: "))
Grosery_Bill = float(input("Please Enter Your Grosery Bill: "))
Ke_Bill = float(input("Please Enter Your KE Bill: "))
Gas_Bill = float(input("Please Enter Your Gas Bill: "))
Internet_Bill = float(input("Please Enter Your Internet Bill: "))
Water_Bill = float(input("Please Enter Your Water Bill: "))
Jamedar_Bill = float(input("Please Enter Your Jamedar Bill: "))
Super_Card_Bill = float(input("Please Enter Your Super Card Bill: "))
Transport_Bill = float(input("Please Enter Your Transport Bill: "))

Own_House = input("Do you live in you own house?")

if Own_House.lower() == "no":
    rent = float(input("Please Enter Your Rent: "))

else:
    rent = 0



print("Expense Calculator")


Married = input(" Are you Married? ")

if Married.lower() == "yes":
    child = int(input("How many child do you have? "))
    if child > 0:
        child_expense = float(input("Enter Your Child Expense: "))
    else:
        child_expense = 0

Total_Expenses = Grosery_Bill + Ke_Bill + Gas_Bill + Internet_Bill + Water_Bill + Jamedar_Bill + Super_Card_Bill + Transport_Bill + rent + child_expense


Savings = Salary - Total_Expenses

if Salary > Total_Expenses:
    print(f"{Employee}Your Savings Are: {Savings} Your Should take savings plans kindly visit HBL")
elif Salary == Total_Expenses:
    print("Please you should take measure steps to increase your income and contact Dhoolu Bhoolu")
else: print("Please Decrease Your Expenses")

print(f"Your Salary is: {Salary}")
print(f"Your Total Expense is: {Total_Expenses}")
print(f"Your Total Savings is: {Savings}")
