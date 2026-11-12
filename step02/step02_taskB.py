# Name: Cody M
# Date: 11/11/26
# Program: Variables and Input
# Desc: Pratice with variable types and inputs

# Task B: Road Trip Calculator

# Constants
AVG_SPEED = 55

# Inputs
destination = input("Destination: ")
distance = float(input("Trip distance (miles): "))
gas_mileage = float(input("Car's miles per gallon: "))
gallon_price = float(input("Gas price per gallon: "))
travellers = int(input("Number of people splitting the cost: "))
print("\n")

# Calculations
gallons = distance / gas_mileage
gas_cost = gallons * gallon_price
cost_per_person = gas_cost / travellers
driving_time = ((distance / AVG_SPEED) * 60)
round_trip_gas = gas_cost * 2

# Outputs
print(f"--- Trip to {destination} ---")
print(f"Gallons of gas: {gallons:.1f}")
print(f"Gas cost: ${gas_cost:.2f}")
print(f"Cost per person: ${cost_per_person:.2f}")
print(f"Driving time: {int(driving_time / 60)}h {int(driving_time % 60)}m (at {AVG_SPEED}mph)")
print(f"Round trip gas: ${round_trip_gas:.2f}")
