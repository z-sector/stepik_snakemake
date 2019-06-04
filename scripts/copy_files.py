import argparse
import re


def parse_args():
    parser = argparse.ArgumentParser(description='Word counting utility!')
    parser.add_argument('input', type=argparse.FileType('r'), help='Input path file for count.')
    parser.add_argument('output', type=argparse.FileType('w'), help='Output path file after count.')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    file_input = args.input
    file_output = args.output
    with file_output:
        lines = "".join(file_input.readlines()).lower()
        lines = re.sub(r'\s+', '', lines)
        ch_list = sorted(set(lines))
        for char in ch_list:
            record = char + ': ' + str(lines.count(char)) + '\n'
            file_output.write(record)
