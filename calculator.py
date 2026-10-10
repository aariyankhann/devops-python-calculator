
def calculate():
    print("=== Simple Python Calculator ===")
    print("Operations: +, -, *, /")

    try:
        first = float(input("Enter the first number: "))
        operator = input("Choose an operation (+, -, *, /): ").strip()
        second = float(input("Enter the second number: "))

        if operator == "+":
            result = first + second
        elif operator == "-":
            result = first - second
        elif operator == "*":
            result = first * second
        elif operator == "/":
            if second == 0:
                print("Error: Cannot divide by zero.")
                return
            result = first / second
        else:
            print("Error: Invalid operation.")
            return

        print(f"Result: {result:g}")

    except ValueError:
        print("Error: Please enter valid numbers.")


if __name__ == "__main__":
    calculate()
