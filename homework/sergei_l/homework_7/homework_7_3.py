string1 = 'результат операции: 42'
string2 = 'результат операции: 54'
string3 = 'результат работы программы: 209'
string4 = 'результат: 2'


def result_calc(string):
    return int(string.split()[-1]) + 10


print(result_calc(string1))
print(result_calc(string2))
print(result_calc(string3))
print(result_calc(string4))
