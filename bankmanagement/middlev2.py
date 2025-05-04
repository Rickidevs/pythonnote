import random
import time

def get_input(prompt, required_type=str, condition=lambda x: True, error_message="Invalid input."):
    while True:
        try:
            value = required_type(input(prompt).strip())
            if condition(value):
                return value
            else:
                print(error_message)
        except ValueError:
            print(error_message)

def register_user():
    user = {}
    print("\n--- Registration ---")
    user["first_name"] = get_input("Enter your first name: ")
    user["last_name"] = get_input("Enter your last name: ")
    user["age"] = get_input("Enter your age: ", int, lambda x: x > 0, "Age must be a positive number.")
    student_input = get_input("Are you a student? (yes/no): ", str, lambda x: x.lower() in ["yes", "no"])
    user["is_student"] = student_input.lower() == "yes"
    
    user["password"] = get_input("Enter a password (min 8 characters): ", str, lambda x: len(x) >= 8, "Password too short.")
    user["customer_code"] = random.randint(1000, 9999)
    
    print(f"\n✅ Welcome, {user['first_name']} {user['last_name']}!")
    print(f"Your customer code is: {user['customer_code']}")
    print("Please log in again to access your account.\n")
    return user

def login_user(user):
    print("\n--- Login ---")
    attempts = 0
    while attempts < 3:
        code = get_input("Enter customer code: ", str)
        password = get_input("Enter password: ")
        
        if code.isdigit() and int(code) == user["customer_code"] and password == user["password"]:
            print(f"""
✅ Login successful!

First Name: {user['first_name']}
Last Name: {user['last_name']}
Age: {user['age']}
Student: {"Yes" if user['is_student'] else "No"}
Balance: 0 AZN
""")
            return
        else:
            attempts += 1
            print(f"❌ Incorrect credentials. Attempts remaining: {3 - attempts}")
    
    print("⚠️ Too many failed attempts. Please try again after 3 minutes.")
    time.sleep(180)

def main():
    print("🏦 Welcome to our Bank System\n")
    choice = get_input("1 - Register\n2 - Login (not implemented)\nChoose an option: ", int, lambda x: x in [1, 2], "Please enter 1 or 2.")
    
    if choice == 1:
        user = register_user()
        login_user(user)
    else:
        print("Login functionality is not available yet.")

if __name__ == "__main__":
    main()
