from random import randrange


salary = int(input('Введите зарплату: '))
bonus = bool(randrange(0, 2))

if bonus:
    final_salary = salary + randrange(50, 1000, 50)
else:
    final_salary = salary

print(f"${final_salary}")
