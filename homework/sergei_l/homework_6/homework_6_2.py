result = []

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        result.append('FuzzBuzz')
    elif num % 3 == 0:
        result.append('Fuzz')
    elif num % 5 == 0:
        result.append('Buzz')
    else:
        result.append(num)

print(result)
