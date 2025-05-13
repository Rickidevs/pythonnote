import math

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def display_menu():
    print("\n===== ADVANCED CALCULATOR =====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (^)")
    print("6. Square Root (√)")
    print("7. Percentage (%)")
    print("8. Exit")

def calculate():
    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ")

        if choice == '8':
            print("Exiting calculator...")
            break

        if choice in ['6']: 
            num = get_number("Enter number: ")
            if choice == '6':
                if num >= 0:
                    print(f"√{num} = {math.sqrt(num):.2f}")
                else:
                    print("Cannot calculate square root of negative number")
        elif choice in ['1', '2', '3', '4', '5', '7']:
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")
            
            if choice == '1':
                print(f"{num1} + {num2} = {num1 + num2}")
            elif choice == '2':
                print(f"{num1} - {num2} = {num1 - num2}")
            elif choice == '3':
                print(f"{num1} * {num2} = {num1 * num2}")
            elif choice == '4':
                if num2 != 0:
                    print(f"{num1} / {num2} = {num1 / num2:.2f}")
                else:
                    print("Error: Division by zero!")
            elif choice == '5':
                print(f"{num1}^{num2} = {math.pow(num1, num2):.2f}")
            elif choice == '7':
                print(f"{num1}% of {num2} = {(num1/100) * num2}")
        else:
            print("Invalid choice. Please enter a number between 1-8.")

if __name__ == "__main__":
    calculate()