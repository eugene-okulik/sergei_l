def wich_operation(func):

    def wrapper(first_num, second_num):
        if first_num == second_num:
            operation = "+"
        elif first_num < 0 or second_num < 0:
            operation = "*"
        elif first_num > second_num:
            operation = "-"
        elif first_num < second_num:
            operation = "/"
        return func(first_num, second_num, operation)

    return wrapper


@wich_operation
def calc(first_num, second_num, operation):
    if operation == "+":
        result = first_num + second_num
    elif operation == "-":
        result = second_num - first_num
    elif operation == "*":
        result = first_num * second_num
    elif operation == "/":
        result = first_num / second_num
    else:
        result = "Operation is incorrect"
    return print(result)


first_number = int(input("Enter a first number: "))
second_number = int(input("Enter a second number: "))

calc(first_number, second_number)
