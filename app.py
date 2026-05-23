print("===== Simple Calculator =====")
print("1. Addition")
print("2. Multiplication")
print("3. Exit")

choice = input("Enter choice: ")

if choice == "1":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result:", a + b)

elif choice == "2":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result:", a * b)

elif choice == "3":
    print("Goodbye!")
