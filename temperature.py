temp = float(input("What is the temperature? "))
unit = input("Is this temeprature in celsius or farenheit? (C or F): ")

if unit == "C":
    temp = round((round * temp) / 5 + 32, 1)
    print(f"The temperature in farenheit is: {temp}° F")

elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in celsius is: {temp}° C")
