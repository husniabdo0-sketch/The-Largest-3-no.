while True:
    try:
        number1 = float(input("Enter the first number: "))
        break
    except ValueError:
        print("Please enter a valid number, such as 4 or -2.5.")

while True:
    try:
        number2 = float(input("Enter the second number: "))
        break
    except ValueError:
        print("Please enter a valid number, such as 4 or -2.5.")

while True:
    try:
        number3 = float(input("Enter the third number: "))
        break
    except ValueError:
        print("Please enter a valid number, such as 4 or -2.5.")

if number1 == number2 == number3:
    print(f"All three numbers are equal: {number1:g}.")
elif number1 == number2 and number1 > number3:
    print(f"The largest number is {number1:g}; the first and second numbers are tied.")
elif number1 == number3 and number1 > number2:
    print(f"The largest number is {number1:g}; the first and third numbers are tied.")
elif number2 == number3 and number2 > number1:
    print(f"The largest number is {number2:g}; the second and third numbers are tied.")
elif number1 > number2 and number1 > number3:
    print(f"The largest number is {number1:g}; the third and fourth numbers are tied.")
elif number2 > number1 and number2 > number3:
    print(f"The largest number is {number2:g}.")
else:
    print(f"The largest number is {number3:g}.")