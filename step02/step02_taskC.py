# Name: Cody M
# Date: 11/11/26
# Program: Variables and Input
# Desc: Pratice with variable types and inputs

# Task C: Paycheck Calculator

# Constants (roughly based on real stats)
FEDERAL_TAX_RATE = 0.10
STATE_TAX_RATE = 0.0275
SOCIAL_SECURITY_RATE = 0.062
MEDICARE_RATE = 0.0145
WEEKS_PER_YEAR = 52

# Inputs
name = input("Employee Name: ")
hourly_pay = float(input("Hourly Pay: "))
hours_worked = float(input("Hours worked this week: "))
print("\n")

# Calculations
gross_pay = hourly_pay * hours_worked

federal_tax = gross_pay * FEDERAL_TAX_RATE
state_tax = gross_pay * STATE_TAX_RATE
social_security_tax = gross_pay * SOCIAL_SECURITY_RATE
medicare_tax = gross_pay * MEDICARE_RATE
total_taken = federal_tax + state_tax + social_security_tax + medicare_tax

net_pay = gross_pay - total_taken
percent_kept = (net_pay / gross_pay) * 100
yearly_gross = gross_pay * WEEKS_PER_YEAR
yearly_net = net_pay * WEEKS_PER_YEAR

# Outputs
print("=" * 34)
print(" " * (11 - (len(name) // 2)),"PAY STUB: " + name) # Calculates spaces to always center the Paystub Name
print("=" * 34)

print(f"Hours worked:\t\t {hours_worked:.1f}")
print(f"Hourly rate:\t\t ${hourly_pay:.2f}")
print(f"Gross pay:\t\t ${gross_pay:.2f}")
print("-" * 34)

print(f"Federal tax ({FEDERAL_TAX_RATE * 100:.1f}%):\t ${federal_tax:.2f}")
print(f"State tax ({STATE_TAX_RATE * 100:.1f}%):\t ${state_tax:.2f}")
print(f"Social Security:\t ${social_security_tax:.2f}")
print(f"Medicare:\t\t ${medicare_tax:.2f}")
print(f"Total Deductions:\t ${total_taken:.2f}")
print("-" * 34)

print(f"Net Pay:\t\t ${net_pay:.2f}")
print("=" * 34)

print(f"You keep {percent_kept:.1f}% of what you earn.")
print(f"Yearly gross:\t\t ${yearly_gross:.2f}")
print(f"Yearly net:\t\t ${yearly_net:.2f}")


