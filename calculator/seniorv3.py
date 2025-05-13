import math
import sys
from datetime import datetime
from enum import Enum, auto

class Operation(Enum):
    ADD = auto()
    SUBTRACT = auto()
    MULTIPLY = auto()
    DIVIDE = auto()
    POWER = auto()
    SQRT = auto()
    SIN = auto()
    COS = auto()
    TAN = auto()
    LOG = auto()
    LN = auto()
    FACTORIAL = auto()
    MODULO = auto()
    PERCENTAGE = auto()
    EXIT = auto()

class Calculator:
    def __init__(self):
        self.history = []
        self.start_time = datetime.now()
        self.session_id = self.start_time.strftime("%Y%m%d%H%M%S")
        
    def display_menu(self):
        print("\n" + "="*50)
        print(f"SCIENTIFIC CALCULATOR (Session: {self.session_id})".center(50))
        print("="*50)
        print(f"{'Operation':<20}{'Key':<10}{'Description':<20}")
        print("-"*50)
        print(f"{'Addition':<20}{'1':<10}{'a + b':<20}")
        print(f"{'Subtraction':<20}{'2':<10}{'a - b':<20}")
        print(f"{'Multiplication':<20}{'3':<10}{'a × b':<20}")
        print(f"{'Division':<20}{'4':<10}{'a ÷ b':<20}")
        print(f"{'Power':<20}{'5':<10}{'a^b':<20}")
        print(f"{'Square Root':<20}{'6':<10}{'√a':<20}")
        print(f"{'Trigonometric':<20}{'7':<10}{'sin/cos/tan':<20}")
        print(f"{'Logarithm':<20}{'8':<10}{'log10/ln':<20}")
        print(f"{'Factorial':<20}{'9':<10}{'a!':<20}")
        print(f"{'Modulo':<20}{'10':<10}{'a % b':<20}")
        print(f"{'Percentage':<20}{'11':<10}{'a% of b':<20}")
        print(f"{'History':<20}{'12':<10}{'View history':<20}")
        print(f"{'Exit':<20}{'0':<10}{'Quit program':<20}")
        print("="*50)

    def get_float_input(self, prompt):
        while True:
            try:
                value = input(prompt)
                if value.lower() == 'pi':
                    return math.pi
                if value.lower() == 'e':
                    return math.e
                return float(value)
            except ValueError:
                print("Invalid input. Please enter a number or 'pi'/'e'.")

    def get_operation_choice(self):
        while True:
            try:
                choice = int(input("\nEnter operation number (0-12): "))
                if 0 <= choice <= 12:
                    return choice
                print("Please enter a number between 0 and 12.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def perform_operation(self, operation, a=None, b=None):
        result = None
        operation_name = ""
        
        try:
            if operation == Operation.ADD:
                result = a + b
                operation_name = f"{a} + {b}"
            elif operation == Operation.SUBTRACT:
                result = a - b
                operation_name = f"{a} - {b}"
            elif operation == Operation.MULTIPLY:
                result = a * b
                operation_name = f"{a} × {b}"
            elif operation == Operation.DIVIDE:
                if b == 0:
                    raise ZeroDivisionError("Division by zero")
                result = a / b
                operation_name = f"{a} ÷ {b}"
            elif operation == Operation.POWER:
                result = math.pow(a, b)
                operation_name = f"{a}^{b}"
            elif operation == Operation.SQRT:
                if a < 0:
                    raise ValueError("Square root of negative number")
                result = math.sqrt(a)
                operation_name = f"√{a}"
            elif operation == Operation.SIN:
                result = math.sin(math.radians(a))
                operation_name = f"sin({a}°)"
            elif operation == Operation.COS:
                result = math.cos(math.radians(a))
                operation_name = f"cos({a}°)"
            elif operation == Operation.TAN:
                result = math.tan(math.radians(a))
                operation_name = f"tan({a}°)"
            elif operation == Operation.LOG:
                if a <= 0:
                    raise ValueError("Log of non-positive number")
                result = math.log10(a)
                operation_name = f"log10({a})"
            elif operation == Operation.LN:
                if a <= 0:
                    raise ValueError("Ln of non-positive number")
                result = math.log(a)
                operation_name = f"ln({a})"
            elif operation == Operation.FACTORIAL:
                if a < 0:
                    raise ValueError("Factorial of negative number")
                result = math.factorial(int(a))
                operation_name = f"{int(a)}!"
            elif operation == Operation.MODULO:
                result = a % b
                operation_name = f"{a} mod {b}"
            elif operation == Operation.PERCENTAGE:
                result = (a / 100) * b
                operation_name = f"{a}% of {b}"
            
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.history.append((timestamp, operation_name, result))
            
            return result
        
        except Exception as e:
            print(f"Error: {str(e)}")
            return None

    def show_history(self):
        if not self.history:
            print("\nNo history available.")
            return
            
        print("\n" + "="*70)
        print("CALCULATION HISTORY".center(70))
        print("="*70)
        print(f"{'Timestamp':<20}{'Operation':<25}{'Result':<25}")
        print("-"*70)
        for entry in self.history[-10:]: 
            print(f"{entry[0]:<20}{entry[1]:<25}{str(entry[2]):<25}")
        print("="*70)

    def run(self):
        print("\n" + "="*50)
        print("PROFESSIONAL SCIENTIFIC CALCULATOR".center(50))
        print("="*50)
        print(f"Session started at: {self.start_time}")
        
        while True:
            self.display_menu()
            choice = self.get_operation_choice()
            
            if choice == 0:
                duration = datetime.now() - self.start_time
                print(f"\nSession duration: {duration}")
                print("Thank you for using the Professional Scientific Calculator!")
                sys.exit(0)
            elif choice == 12:
                self.show_history()
                continue
            
            operation_map = {
                1: Operation.ADD,
                2: Operation.SUBTRACT,
                3: Operation.MULTIPLY,
                4: Operation.DIVIDE,
                5: Operation.POWER,
                6: Operation.SQRT,
                7: None,
                8: None,  
                9: Operation.FACTORIAL,
                10: Operation.MODULO,
                11: Operation.PERCENTAGE
            }
            
            operation = operation_map.get(choice)
            
            if choice == 7: 
                trig_choice = input("Choose (1) sin, (2) cos, (3) tan: ")
                angle = self.get_float_input("Enter angle in degrees: ")
                if trig_choice == '1':
                    result = self.perform_operation(Operation.SIN, angle)
                elif trig_choice == '2':
                    result = self.perform_operation(Operation.COS, angle)
                elif trig_choice == '3':
                    result = self.perform_operation(Operation.TAN, angle)
                else:
                    print("Invalid trigonometric function choice")
                    continue
                    
            elif choice == 8:
                log_choice = input("Choose (1) log10, (2) natural log: ")
                num = self.get_float_input("Enter number: ")
                if log_choice == '1':
                    result = self.perform_operation(Operation.LOG, num)
                elif log_choice == '2':
                    result = self.perform_operation(Operation.LN, num)
                else:
                    print("Invalid logarithmic function choice")
                    continue
                    
            elif operation in [Operation.SQRT, Operation.FACTORIAL]:
                num = self.get_float_input("Enter number: ")
                result = self.perform_operation(operation, num)
                
            else:
                num1 = self.get_float_input("Enter first number: ")
                num2 = self.get_float_input("Enter second number: ")
                result = self.perform_operation(operation, num1, num2)
            
            if result is not None:
                print(f"\nResult: {result:.10g}")
if __name__ == "__main__":
    try:
        calc = Calculator()
        calc.run()
    except KeyboardInterrupt:
        print("\n\nCalculator session terminated by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\nAn unexpected error occurred: {str(e)}")
        sys.exit(1)