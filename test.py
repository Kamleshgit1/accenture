x = int(input("Enter first number"))
op = input("Enter the operator sign")
y = int(input("Enter the second number"))
if op == "+":
    print(x+y)
elif op == "-":
    print(x-y)
elif op == "*":
    print(x*y)
elif op == "/":
    print(x/y)
else:
    print("you have enetered a wrong operator")
