import time

history = []

# UX Constants
ERROR_MESSAGE = "Invalid Input, Please Try again!"
ANSWER_MESSAGE = "Your Answer is: "
LEAVE_MESSAGE = "Exiting..."
FIRST_NUMBER_MESSAGE = "Enter Your First Number: "
SECOND_NUMBER_MESSAGE = "Enter Your Second Number: "
OPERATION_MESSAGE = "Enter an Operation (*, /, -, +, **, %): "
COMMAND_MESSAGE = "Do you want to calculate again or view history? y/n/h: "
DIVIDE_BY_ZERO_ERROR_MESSAGE = "Can't divide by 0!"
LEAVE_MESSAGE_SPEED = 2 / len(LEAVE_MESSAGE)
HISTORY_DISPLAY_SPEED = 2

# Getters
def get_number(message, error_message=ERROR_MESSAGE):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print(error_message)
def get_valid_operation(valid_operations):
    while True:
        operation = input(OPERATION_MESSAGE).lower()
        if operation in valid_operations:
            return operation
        print(ERROR_MESSAGE)

# Helper Method for Calculate
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

# Asks for Values and Calculates and Prints out answer, appends equation to history
def calculate():
    num1 = get_number(FIRST_NUMBER_MESSAGE)
    valid_operations = ("+", "-", "**", "*", "x", "%", "/", "÷")
    operation = get_valid_operation(valid_operations)
    while True:
        num2 = get_number(SECOND_NUMBER_MESSAGE)
        try:
            result = perform_operation(num1, num2, operation)
            print(f"{ANSWER_MESSAGE}{result:.0f}")
            history.append(f"{num1:.0f} {operation} {num2:.0f} = {result:.0f}")
            break
        except ZeroDivisionError:
            print(DIVIDE_BY_ZERO_ERROR_MESSAGE)

# Animated Exit With customized Exit Message and dynamic speed
def exit_animation():
    time.sleep(LEAVE_MESSAGE_SPEED)
    print()
    for char in LEAVE_MESSAGE:
        print(char, end="", flush=True)
        time.sleep(LEAVE_MESSAGE_SPEED)
    print()
    time.sleep(LEAVE_MESSAGE_SPEED)
    print()

# Main Control Flow
calculate()
time.sleep(1)
while True:
    command = input(COMMAND_MESSAGE).strip().lower()
    if command == "n":
        break
    elif command == "y":
        calculate()
        time.sleep(0.5)
    elif command == "h":
        CURRENT_HISTORY_DISPLAY_SPEED = HISTORY_DISPLAY_SPEED / len(history)
        time.sleep(CURRENT_HISTORY_DISPLAY_SPEED)
        for equation in history:
            print(equation)
            time.sleep(CURRENT_HISTORY_DISPLAY_SPEED)
    else:
        print(ERROR_MESSAGE)
exit_animation()
