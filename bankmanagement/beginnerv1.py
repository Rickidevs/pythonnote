import random
import time

login_attempts = 0

print("Welcome to our Bank!\n")

try:
    choice = int(input("For registration - 1\nFor login - 2\nChoose: "))

    if choice == 1:
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        age = int(input("Enter your age: "))
        is_student = input("Are you a student? (yes/no): ").strip().lower() == "yes"

        password = input("Enter your password (minimum 8 characters): ")
        while len(password) < 8:
            password = input("Password too short. Please enter again: ")

        customer_code = random.randint(1000, 9999)
        print(f"\nDear {first_name} {last_name}, welcome!")
        print(f"Your customer code is: {customer_code}")
        print("Please log in again to access your account.\n")

        while True:
            if login_attempts >= 3:
                print("❌ Maximum login attempts exceeded. Please try again after 3 minutes.")
                time.sleep(180)
                login_attempts = 0
                continue

            entered_code = input("Enter your customer code: ")
            entered_password = input("Enter your password: ")

            if entered_code.isdigit() and int(entered_code) == customer_code and entered_password == password:
                print(f"""
✅ Login successful!

First Name: {first_name}
Last Name: {last_name}
Age: {age}
Student: {"Yes" if is_student else "No"}
Balance: 0 AZN
""")
                break
            else:
                login_attempts += 1
                print("Incorrect customer code or password. Please try again.\n")

    elif choice == 2:
        print("Login functionality has not been implemented yet.")
    else:
        print("❗ Invalid selection.")
except ValueError:
    print("⚠️ Please enter only numeric values.")
