# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# takes an input and prints "Hi, {input}"
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# returns num1 plus num2
def add(num1, num2):
    return num1 + num2

# returns num1 subtracted by num2
def subtract(num1, num2):
    return num1 - num2

# returns num1 multiplied by num2
def multiply(num1, num2):
    return num1 * num2

# returns num1 divided by num2
def divide(num1, num2):
    return num1 / num2

# takes 3 parameters, the first number, an operation symbol,
# and the second number and performs that operation.
def perform_operation(num1, operator, num2):
    if operator == "+":
        return add(num1, num2)
    elif operator == "-":
        return subtract(num1, num2)
    elif operator == "*":
        return multiply(num1, num2)
    elif operator == "/":
        return divide(num1, num2)
    else:
        #if they didn't enter a valid operator
        #inform the user.
        return str(operator) + " is not a valid operator"

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Welcome to the calculator, enter 'exit' to exit. ")

    while True:
        num1 = input("Please enter a number: ")
        if num1 == "exit":
            break
        operator = input("Please enter an operator (+, -, *, /): ")
        if operator == "exit":
            break
        num2 = input("Please enter another number: ")
        if operator == "exit":
            break

        #try to to cast the number input to a float
        #will throw an error if the numbers are strings.
        try:
            output = perform_operation(float(num1), operator, float(num2))
            print(str(num1) + " " + str(operator) + " " + str(num2) + " = " + str(output))
        except ValueError:
            #print the operator that was incorrect when it was entered
            #wrong.
            print(output)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
