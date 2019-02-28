'''
Usage:
python3 main.py data/example.in out.txt
'''

import sys


def parse_input(file):
    nums = []
    with open(file, 'r') as f:
        for i, line in enumerate(f):
            # TODO parsing
            nums.append(line.rstrip('\n').split(' '))

    return nums

def write_out(file, data):
    with open(file, 'w') as f:
        for line in data:
            for val in line:
                f.write('{} '.format(val))
            f.write('\n')


if __name__ == '__main__':
    nums = parse_input(sys.argv[1])
    write_out(sys.argv[2] if len(sys.argv) > 2 else 'out.txt', nums)
