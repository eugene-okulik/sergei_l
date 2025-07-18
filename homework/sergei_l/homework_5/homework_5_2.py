program_result1 = 'результат операции: 42'
program_result2 = 'результат операции: 514'
program_result3 = 'результат работы программы: 9'

result_number1 = program_result1[-1:program_result1.index(':'):-1]
number_operation1 = int(result_number1[::-1]) + 10

result_number2 = program_result2[-1:program_result2.index(':'):-1]
number_operation2 = int(result_number2[::-1]) + 10

result_number3 = program_result3[-1:program_result3.index(':'):-1]
number_operation3 = int(result_number3[::-1]) + 10

print(f"Первый результат после прибавления: {number_operation1}")
print(f"Второй результат после прибавления: {number_operation2}")
print(f"Третий результат после прибавления: {number_operation3}")