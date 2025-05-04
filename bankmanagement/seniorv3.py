import random
import time
import getpass

class User:
    def __init__(self, first_name, last_name, age, is_student, password):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.is_student = is_student
        self.password = password
        self.customer_code = self._generate_customer_code()
        self.balance = 0.0

    def _generate_customer_code(self):
        return random.randint(1000, 9999)

    def verify_credentials(self, code, password):
        return self.customer_code == code and self.password == password

    def display_info(self):
        student_status = "Yes" if self.is_student else "No"
        print(f"""
✅ Login successful!

First Name : {self.first_name}
Last Name  : {self.last_name}
Age        : {self.age}
Student    : {student_status}
Balance    : {self.balance:.2f} AZN
""")

class BankSystem:
    def __init__(self):
        self.users = {}

    def run(self):
        self._welcome_message()
        while True:
            choice = self._get_choice()
            if choice == 1:
                user = self.register()
                if user:
                    self.login(user)
            elif choice == 2:
                print("Login system is only available for registered users in this demo.\n")
            else:
                print("Exiting...")
                break

    def _welcome_message(self):
        print("🏦 Welcome to the Advanced Python Bank System!\n")

    def _get_choice(self):
        print("Options:")
        print("1 - Register")
        print("2 - Login (not available)")
        print("3 - Exit")
        while True:
            try:
                choice = int(input("Select an option: "))
                if choice in [1, 2, 3]:
                    return choice
                else:
                    print("❗ Please enter 1, 2, or 3.")
            except ValueError:
                print("⚠️ Invalid input. Please enter a number.")

    def register(self):
        print("\n--- Registration ---")
        first_name = input("Enter your first name: ").strip()
        last_name = input("Enter your last name: ").strip()

        age = self._get_validated_input("Enter your age: ", int, lambda x: x > 0, "Age must be positive.")
        is_student_input = input("Are you a student? (yes/no): ").strip().lower()
        is_student = is_student_input == "yes"

        password = self._get_secure_password()
        user = User(first_name, last_name, age, is_student, password)
        self.users[user.customer_code] = user

        print(f"\n🎉 Registration complete! Your customer code is: {user.customer_code}")
        print("Please log in with your credentials.\n")
        return user

    def login(self, user):
        print("--- Login ---")
        attempts = 0
        while attempts < 3:
            try:
                code = int(input("Enter your customer code: "))
                password = getpass.getpass("Enter your password: ")
            except ValueError:
                print("⚠️ Invalid input. Please enter valid credentials.")
                continue

            if user.verify_credentials(code, password):
                user.display_info()
                return
            else:
                attempts += 1
                print(f"❌ Incorrect credentials. Attempts left: {3 - attempts}\n")

        print("⏳ Too many failed attempts. Please wait 3 minutes to try again.")
        time.sleep(180)

    def _get_validated_input(self, prompt, cast_type, condition, error_message):
        while True:
            try:
                value = cast_type(input(prompt).strip())
                if condition(value):
                    return value
                else:
                    print(f"❗ {error_message}")
            except ValueError:
                print("⚠️ Invalid input type.")

    def _get_secure_password(self):
        while True:
            password = getpass.getpass("Create a password (min 8 characters): ")
            if len(password) >= 8:
                return password
            else:
                print("❗ Password too short. Try again.")

if __name__ == "__main__":
    bank_app = BankSystem()
    bank_app.run()
