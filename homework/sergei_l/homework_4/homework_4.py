my_dict = {
    'tuple': ('a', 'b', 'c', 'd'), 
    'list': ['i', 'ii', 'iii', 'iv'], 
    'dict': {'a': 1, 'b': 2, 'c': 3, 'd': 4}, 
    'set': {'A1', 'B2', 'C3', 'D4'}
}

tuple_letters = my_dict['tuple']

list_lat_nums = my_dict['list']
list_lat_nums.append('v')
list_lat_nums.pop(1)

dict_nums = my_dict['dict']
dict_nums['e'] = 5
dict_nums.pop('d')

set_cells = my_dict['set']
set_cells.add('E5')
set_cells.pop()

print(f'Последнее значение кортежа внутри словаря: {tuple_letters[-1]}')
print(f'Измененные значения словаря: {my_dict}')

