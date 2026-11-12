# Name: Cody M
# Date: 11/11/26
# Program: Working with variables
# Desc: Pratice with variable types and inputs

# Variable: a stored value with a name able to be used throughout a program
# Int: a whole number
# Float: any number with decimal value
# String: a line of plain text, ignoring any possible data types
# Bool: a yes or no switch, used to check if something is true or false
# Operator: A math operation used to modify variables

# Variable introduction
room = "Room 112:"
seats = 24
print(room)
print(seats)
print("\n", "=" * 30, "\n")

# Variable modification
count = 5
print("Initial count: " + str(count))
count = count + 1
print(count)
print("\n", "=" * 30, "\n")

# Variable types
print(type("Cody"))
print(type(3))
print(type(2.75))
print(type(True))
print(type("3"))
print("\n", "=" * 30, "\n")

# Inputs
first_name = input("First name: ")
print("Hello, " + first_name + "!")

# Var to string
age_text = input("Age: ")
age = int(age_text)
age_next_year = age + 1
print("Next year you will be", age_next_year)
print("\n", "=" * 30, "\n")

# Operators
minutes = 135
hours = minutes // 60
leftover = minutes % 60
print(hours, "hours and", leftover, "minutes")
print("\n", "=" * 30, "\n")

print("Value list: 80, 90, 85")
average = (80 + 90 + 85) / 3
print("Average: " + str(average))

wrong_average = 80 + 90 + 85 / 3
print("Wrong average: " + str(wrong_average))
print("\n", "=" * 30, "\n")

# Division
price = 8.99
print(int(price))
print(round(price))
print(round(price, 2))
print("\n", "=" * 30, "\n")

# Constants
SALES_TAX_RATE = 0.0675
SHIPPING_COST = 4.99

order_amount = 40.00
tax = order_amount * SALES_TAX_RATE
total = order_amount + tax + SHIPPING_COST
print(f"Total: ${total:.2f}")
print("\n", "=" * 30, "\n")

# F-Strings
player = "Casey"
points = 42
cost = 3.5

print(f"{player} scored {points} points.")
print(f"Cost: ${cost}")
print(f"Cost: ${cost:.2f}")
