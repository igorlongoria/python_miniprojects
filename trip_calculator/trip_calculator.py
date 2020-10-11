# Trip Calculator

kilomters_to_drive = float(input("Please enter how many kilometers you are driving: "))
liter_per_kilometer = float(input("How many liters per kilometer does your car use: "))
price_per_liter = float(input("How much is the fuel per liter: "))
x = kilomters_to_drive
y = liter_per_kilometer
z = price_per_liter
total = x * y * z
print("Your total cost for the trip is: ", "$", total)