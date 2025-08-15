import argparse
import os


parser = argparse.ArgumentParser()
parser.add_argument("file", help="Full path to log file(s)")
parser.add_argument("--text", help="Text to find")
args = parser.parse_args()


def read_file(path):
    with open(path) as log_file:
        for row in log_file:
            yield row


def file_path():
    path_list = []
    if os.path.isfile(args.file):
        path_list.append(args.file)
        return path_list
    elif os.path.isdir(args.file):
        file_list = os.listdir(args.file)
        for file in file_list:
            if args.file.endswith(os.path.sep):
                path_list.append(args.file + file)
            else:
                path_list.append(args.file + os.path.sep + file)
        return path_list


for line in file_path():
    print(f"----- In file: {line}")
    line_number = 1
    for row in read_file(line):
        words = row.split()
        for index, word in enumerate(words):
            if args.text == word:
                if index >= 5:
                    result = ' '.join(words[index - 5:index] + words[index:index + 6])
                else:
                    result = ' '.join(words[:index] + words[index:index + 6])
                print(f"On line {line_number}: {result}")
        line_number += 1
