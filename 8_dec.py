from common_core import open_file
from math import lcm

filename = "input_files/puzzle_8.txt"


def create_node_dict(data):
    output = {}
    for line in data:
        if '=' in line:
            root, branches = line.split('=')
            root = root.replace(' ', '')
            branches = [x.replace('(', '').replace(')', '').replace(' ', '') for x in branches.split(',')]
            output[root] = branches
    return output


def find_path(tree, sequence, start='AAA'):
    current = start
    i = 0
    while True:
        if current[-1] == 'Z':
            return i
        index = i % len(sequence)
        current = tree[current][sequence[index]]
        i += 1


def main():
    data = [x.strip('\n') for x in open_file(filename)]
    seq = [0 if char == 'L' else 1 for char in data[0]]
    tree = create_node_dict(data)
    starts = [x for x in tree.keys() if x[-1] == 'A']
    output = [find_path(tree, seq, x) for x in starts]
    final = lcm(*output)
    print(final)
    return output


print(main())
