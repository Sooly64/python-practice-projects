import time

# UX Constants
ERROR_MESSAGE = "Invalid Input, Please Try again!"
ANSWER_MESSAGE = "Your Answer is: "
LEAVE_MESSAGE = "Exiting..."
FIRST_NUMBER_MESSAGE = "Enter Your First Number: "
SECOND_NUMBER_MESSAGE = "Enter Your Second Number: "
OPERATION_MESSAGE = "Enter an Operation (*, /, -, +, **, %): "
CALCULATE_AGAIN_MESSAGE = "Do you want to calculate again? y/n: "
DIVIDE_BY_ZERO_ERROR_MESSAGE = "Can't divide by 0!"
LEAVE_MESSAGE_SPEED = 0.1

def get_number(message, error_message=ERROR_MESSAGE):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print(error_message)

def perform_operation(num1, num2, operation):
    if operation in ("*", "x"):
        return num1 * num2
    elif operation in ("/", "÷"):
        if num2 == 0:
            raise ZeroDivisionError(DIVIDE_BY_ZERO_ERROR_MESSAGE)
        return num1 / num2
    elif operation == "-":
        return num1 - num2
    elif operation == "+":
        return num1 + num2
    elif operation == "**":
        return num1 ** num2
    elif operation == "%":
        return num1 % num2
    else:
        raise ValueError(ERROR_MESSAGE)

def calculate():
    num1 = get_number(FIRST_NUMBER_MESSAGE)
    num2 = get_number(SECOND_NUMBER_MESSAGE)
    while True:
        operation = input(OPERATION_MESSAGE).lower()
        try:
            result = perform_operation(num1, num2, operation)
            print(f"{ANSWER_MESSAGE}{result}")
            break
        except ZeroDivisionError as e:
            print(e)
            num2 = get_number(SECOND_NUMBER_MESSAGE)
        except ValueError:
            print(ERROR_MESSAGE)

def exit_animation():
    print()
    for char in LEAVE_MESSAGE:
        print(char, end="", flush=True)
        time.sleep(LEAVE_MESSAGE_SPEED)
    print()

calculate()
time.sleep(1)
while True:
    command = input(CALCULATE_AGAIN_MESSAGE).lower()
    if command == "n":
        break
    elif command == "y":
        calculate()
        time.sleep(0.5)
    else:
        print(ERROR_MESSAGE)
exit_animation()
