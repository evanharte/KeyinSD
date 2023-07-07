# Program description:
#       This program helps the Edsel Car Rental Company keep track of customer rentals
#       including calculating number of kilometers travelled, the cost of rental, HST, & total rental cost
# Written by: Evan Harte
# Date written: May 8, 2023

# Constant variables:
DAILY_COST = 55.00
MILEAGE_RATE = .24
HST_RATE = .15

# Get user input:
CustName = input("Enter customer name: ")
PhoneNum = input("Enter customer phone number: ")
NumDays = int(input("Enter number of days car was rented: "))
MileageBefore = float(input("Enter mileage when the car was rented: "))
MileageAfter = float(input("Enter mileage when the car was returned: "))

# Calculations / main part of program:
TotKilosTrav = MileageAfter - MileageBefore
MileageCost = TotKilosTrav * MILEAGE_RATE
CostOfRental = (DAILY_COST * NumDays) + MileageCost
HST = DAILY_COST * HST_RATE
TotRentalCost = CostOfRental + HST

# Print input values and calculations to the user:
print()
print("Customer name: ", CustName)
print("Phone number: ", PhoneNum)
print("Number of days car was rented: ", NumDays)
print("Mileage when the car was rented: {}km".format(MileageBefore))
print("Mileage when the car was returned: {}km".format(MileageAfter))

print()
print("Total kilometers travelled: {}km".format(TotKilosTrav))
print("Mileage cost: $", MileageCost)
print("Cost of rental: $", CostOfRental)
print("HST: $", HST)
print("Total rental cost: $", TotRentalCost)
