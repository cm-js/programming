# Name: Cody M
# Date: 11/11/26
# Program: Variables and Input
# Desc: Pratice with variable types and inputs

# Task A: Pizza Party Planner

# Constants
SLICES_PER_PIZZA = 8
PIZZA_PRICE = 12.99
SLICE_PRICE = 2.25

# Inputs
host_name = input("Host name: ")
guest_num = int(input("Number of guests: "))
slices_per_person = int(input("Slices per person: "))
print("\n")

# Calculations
total_slices = guest_num * slices_per_person
whole_pizzas = total_slices // SLICES_PER_PIZZA
extra_slices = total_slices % SLICES_PER_PIZZA
total_cost = (whole_pizzas * PIZZA_PRICE) + (extra_slices * SLICE_PRICE)
cost_per_person = total_cost / guest_num

# Outputs
print(f"=== Pizza Plan for {host_name}'s Party ===")
print(f"Slices needed: {total_slices}")
print(f"Whole pizzas: {whole_pizzas}")
print(f"Extra slices: {extra_slices}")
print(f"Total cost: ${total_cost:.2f}")
print(f"Cost per person: ${cost_per_person:.2f}")
