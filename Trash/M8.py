def arithmetic(x, y, operation):
    if operation == "+":
        print(x + y)
    elif operation == "-":
        print(x - y)
    elif operation == "*":
        print(x * y)
    elif operation == "/":
        print(x / y)
    else:
        print("Неизвестная операция")


x = float(input())
y = float(input())
operation = (input())

arithmetic(x, y, operation)
