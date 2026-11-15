print("Simple Calculator")
try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("1. Add  2. Subtract  3. Multiply  4. Divide")
    choice = input("Choose operation (1-4): ")
    if choice == "1":
        print(f"Answer: {a + b:g}")
    elif choice == "2":
        print(f"Answer: {a - b:g}")
    elif choice == "3":
        print(f"Answer: {a * b:g}")
    elif choice == "4":
        if b == 0:
            print("Cannot divide by zero.")
        else:
            print(f"Answer: {a / b:g}")
    else:
        print("Invalid operation.")
except ValueError:
    print("Please enter valid numbers.")
