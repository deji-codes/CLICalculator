def show_help():
    print("""
Simple CLI Calculator
---------------------
Enter calculations in the following steps when prompted:
- First number
- Operator (+, -, *, /)
- Second number

Commands:
- help  : Show this help message
- quit  : Exit the calculator

Bonus:
- You can press ENTER on the first number to reuse the previous result.
""")


def get_number(prompt, previous_result=None):
    while True:
        user_input = input(prompt).strip()

        # Allow reuse of previous result
        if user_input == "" and previous_result is not None:
            return previous_result

        try:
            return float(user_input)
        except ValueError:
            print("Invalid number. Please enter a valid numeric value.")


def get_operator():
    while True:
        operator = input("Enter operator (+, -, *, /): ").strip()

        if operator in ["+", "-", "*", "/"]:
            return operator
        elif operator.lower() == "help":
            show_help()
        else:
            print("Unsupported operator.")


def calculate(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return num1 / num2


def main():
    print("Welcome to the Simple CLI Calculator!")
    print("Type 'help' for instructions or 'quit' to exit.\n")

    previous_result = None

    while True:
        command = input("Press ENTER to calculate or type 'quit': ").strip().lower()
        if command == "quit":
            print("Goodbye!")
            break
        elif command == "help":
            show_help()
            continue

        try:
            num1 = get_number(
                "Enter first number: ",
                previous_result=previous_result
            )

            operator = get_operator()

            num2 = get_number("Enter second number: ")

            result = calculate(num1, operator, num2)
            print(f"Result: {result}\n")

            previous_result = result

        except ZeroDivisionError as e:
            print(f" Error: {e}\n")
        except Exception:
            print(" Something went wrong. Please try again.\n")


if __name__ == "__main__":
    main()
