unit=input("Please write a measurement unit: ")
temp = int(input("What`s the temperature? "))

if unit == "fahrenheit":
    if temp <= 32:
        print("It`s freezing out!")
    else:
        print("It`s not freezing out.")
else:
    print(f"I am not very good with {unit}")