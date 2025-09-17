num1 = float(input("Please enter the first number:"))
num2 = float(input("Please enter the second number:"))
num3 = float(input("Please enter the third number:"))

def sum():
    return num1 + num2 + num3

def roundedsum():
    total = sum()
    return "{:.2f}".format(total)
print("The total of the three numbers is:", roundedsum())