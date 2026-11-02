# Menu-Driven Calculator
# Language: Python 3

# 1. Functions for arithmetic operations

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b


def power(a, b):
    return a ** b


def modulus(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a % b


# 2. Main calculator program

def main():
    while True:
        print("===== MENU-DRIVEN CALCULATOR =====")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Modulus")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        # Validate menu choice
        if choice not in ("1", "2", "3", "4", "5", "6", "7"):
            print("Invalid choice. Select 1 to 7.")
            continue

        # Exit option
        if choice == "7":
            print("Thank you for using the calculator. Exiting...")
            break

        # Take numbers and perform the selected operation
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == "1":
                result = add(a, b)
                symbol = "+"

            elif choice == "2":
                result = subtract(a, b)
                symbol = "-"

            elif choice == "3":
                result = multiply(a, b)
                symbol = "*"

            elif choice == "4":
                result = divide(a, b)
                symbol = "/"

            elif choice == "5":
                result = power(a, b)
                symbol = "^"

            elif choice == "6":
                result = modulus(a, b)
                symbol = "%"

            # Display result rounded to 2 decimal places
            print(f"{a:g} {symbol} {b:g} = {result:.2f}")

        except ValueError:
            print("Invalid number. Enter numeric values only.")

        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")

        except OverflowError:
            print("Error: Result is too large to display.")

        except (TypeError, ArithmeticError):
            print("Error: Unable to perform this calculation.")


# 3. Start the program
if __name__ == "__main__":
    main()
