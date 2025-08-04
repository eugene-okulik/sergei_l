import os
import datetime


base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
file_path = os.path.join(base_path, 'eugene_okulik', 'hw_13', 'data.txt')

date_list = []


def read_file():
    with open(file_path) as file:
        for line in file.readlines():
            yield line


for data_line in read_file():
    date_string = ', '.join(
        data_line.split()[1:3]
    )
    date_list.append(
        datetime.datetime.strptime(
            date_string.replace(',', ''), '%Y-%m-%d %H:%M:%S.%f'
        )
    )

task_1 = date_list[0] + datetime.timedelta(days=7)
task_2 = datetime.datetime.strftime(date_list[1], '%A')
task_3 = datetime.datetime.now().date() - date_list[2].date()

print(task_1)
print(task_2)
print(task_3)