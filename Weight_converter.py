Weight = int(input("What is your weight: "))
unit = input("If it is in pounds type 'lbs'. If it is in kilos type 'kg': ")

if unit == "lbs":
    converted = Weight * 2.205
    print(f"You are {converted} kilos")
else:
    converted = Weight / 2.205
    print(f"You are {converted} pounds")
