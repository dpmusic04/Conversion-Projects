weight = float(input("What is your weight? "))
unit = input("Kilogram or pounds? (K or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."

elif unit == "L":
    weight = weight * 2.205
    unit = "Kgs."

else:
    print(f"{unit} is not valid")

    print(f"Your weight is: {weight} {unit}")
