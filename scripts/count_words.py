import _io
import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Word counting utility!')
    parser.add_argument('input', type=argparse.FileType('r'), help='Input path file for count.')
    parser.add_argument('output', type=argparse.FileType('w'), help='Output path file after count.')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    file_input: _io.TextIOWrapper = args.input
    file_output: _io.TextIOWrapper = args.output
    with file_input:
        count = 0
        for line in file_input:
            count += len(line.split())
        with file_output:
            file_output.write(f'{count}')
