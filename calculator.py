print("Welcome to my calculator")

def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def pakape(a, pakape):
    ret_val = a
    for i in range(1, pakape):
        ret_val = ret_val * a
    return ret_val
def main():
    operation = input(
        """
        Select operation: 
        + add
        - substract
        * multiply
        / divide
        ** power
        """    
        )

    number_1 = int(input("Enter first number: "))
    number_2 = int(input("Enter second number: "))

    if operation == "+":
        result = add(number_1, number_2)
        print(f"{number_1} + {number_2} = {result}")
    elif operation == "-":
        result = substract(number_1, number_2)
        print(f"{number_1} - {number_2} = {result}")
    elif operation == "**":
        result = pakape(number_1, number_2)
        print(f"{number_1} power {number_2} = {result}")
    elif operation == "*":
        result = multiply(number_1, number_2)
        print(f"{number_1} x {number_2} = {result}")
    elif operation == "/":
        result = divide(number_1, number_2)
        print(f"{number_1} / {number_2} = {result}")
    else:
        print("Operation not defined")

def repeat():
    answer = input("do you want to continue? y/n: ")
    if answer =="y":
        main()
        repeat()
    else:
        print("bye bye")

main()
repeat()