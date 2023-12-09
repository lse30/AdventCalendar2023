from common_core import open_file

filename = "input_files/puzzle_3.txt"
# filename = "input_files/sample_3.txt"
numbers = '0123456789'


def check_validity(data, row, start, end):
    new_grid = ''
    start = 0 if start == 0 else start - 1
    end = len(data[0]) if end == len(data[0]) else end + 1

    for row_offset in [-1, 0, 1]:
        if 0 < row + row_offset < len(data):
            new_grid += (data[row + row_offset][start:end])

    new_grid = new_grid.replace('.', '')
    for num in numbers:
        new_grid = new_grid.replace(num, '')
    return len(new_grid) > 0


def analyse_data(data):
    i = 0
    output = 0
    number = ''
    start_index = None
    end_index = None
    while i < len(data):

        for j in range(len(data[i])):
            if data[i][j].isnumeric():
                if not number:
                    start_index = j
                number += data[i][j]
                end_index = j
            else:
                if number:
                    if check_validity(data, i, start_index, end_index + 1):
                        output += int(number)
                    number = ''
        if number:
            if check_validity(data, i, start_index, end_index + 1):
                output += int(number)
            number = ''
        i += 1
    return output


def main_part_1():
    data = [x.strip('\n') for x in open_file(filename)]
    output = analyse_data(data)
    print(output)


class GearSchematic:

    def __init__(self, data):
        self.data = data
        self.gear_dict = {}

    def analyse_data_2(self):
        i = 0
        number = ''
        start_index = None
        end_index = None
        while i < len(self.data):
            for j in range(len(self.data[i])):
                if self.data[i][j].isnumeric():
                    if not number:
                        start_index = j
                    number += self.data[i][j]
                    end_index = j
                else:
                    if number:
                        self.check_for_gear(i, start_index, end_index + 1, number)
                        number = ''
            if number:
                self.check_for_gear(i, start_index, end_index + 1, number)
                number = ''

            i += 1

    def check_for_gear(self, row, start, end, number):
        start = 0 if start == 0 else start - 1
        end = len(self.data[0]) if end == len(self.data[0]) else end + 1

        for row_offset in [-1, 0, 1]:
            if 0 < row + row_offset < len(self.data):
                sample = (self.data[row + row_offset][start:end])

                if '*' in sample:
                    gear_index = sample.index('*')
                    self.add_to_gear_dict(f'{row + row_offset}-{start + gear_index}', int(number))

    def add_to_gear_dict(self, index, number):
        if index in self.gear_dict:
            self.gear_dict[index].append(number)
        else:
            self.gear_dict[index] = [number]

    def calc_gear_ratios(self):
        output = 0
        for values in self.gear_dict.values():
            if len(values) == 2:
                output += values[0] * values[1]
        return output


def main_part_2():
    data = [x.strip('\n') for x in open_file(filename)]
    output = GearSchematic(data)
    output.analyse_data_2()
    print(output.calc_gear_ratios())


# main_part_1()
main_part_2()
