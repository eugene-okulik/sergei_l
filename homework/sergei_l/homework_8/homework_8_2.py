from sys import set_int_max_str_digits


def generator_fibonacci():
    a = 0
    b = 1
    # fibonacci_number = 0
    count = 1
    while True:
        if count == 1:
            yield a
            count += 1
        elif count == 2:
            yield b
            count += 1
        else:
            fibonacci_number = a + b
            yield fibonacci_number
            a = b
            b = fibonacci_number
            count += 1


def fibonacci_result(num=1):
    count = 1
    fibonacci_number = 0
    for number in generator_fibonacci():
        if count == num:
            fibonacci_number = number
            break
        count += 1
    return fibonacci_number


print(f"Пятое число Фибоначчи: {fibonacci_result(5)}")
print(f"Двухсотое число Фибоначчи: {fibonacci_result(200)}")
print(f"Тысячное число Фибоначчи: {fibonacci_result(1000)}")

set_int_max_str_digits(100000)
print(f"Стотысячное число Фибоначчи: {fibonacci_result(100000)}")
