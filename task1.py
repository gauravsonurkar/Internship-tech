def add(num1, num2):
    return num1 + num2


def substract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: Division by zero is not allowed"


print("Select the operation ")
print("1. Addition ")
print("2. Substraction ")
print("3. Multiplication ")
print("4. Division ")

choice = input("Enter the choice (1/2/3/4) : ")

num1 = float(input("Enter the first number : "))
num2 = float(input("Enter the secound number : "))


if choice == "1":
    print(num1, "+", num2, "=", add(num1, num2))

elif choice == "2":
    print(num1, "-", num2, "=", substract(num1, num2))
elif choice == "3":
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == "4":
    print(num1, "/", num2, "=", divide(num1, num2))

else:
    print("Invalid Input ")
