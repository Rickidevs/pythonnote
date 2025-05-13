print("*** Simple Calculator ***")
print("Operations:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Please select operation (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print(f"Result: {num1} + {num2} = {num1 + num2}")
elif choice == '2':
    print(f"Result: {num1} - {num2} = {num1 - num2}")
elif choice == '3':
    print(f"Result: {num1} * {num2} = {num1 * num2}")
elif choice == '4':
    if num2 != 0:
        print(f"Result: {num1} / {num2} = {num1 / num2}")
    else:
        print("Error! Division by zero is not allowed.")
else:
    print("Invalid input! Please select 1, 2, 3 or 4.")