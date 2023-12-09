from common_core import open_file

nums_list = '1234567890'
convert_list = [
    ('zero', 'z0o'),
    ('one', 'o1e'),
    ('two', 't2o'),
    ('three', 't3e'),
    ('four', 'f4r'),
    ('five', 'f5e'),
    ('six', 's6x'),
    ('seven', 's7n'),
    ('eight', 'e8t'),
    ('nine', 'n9e')
]


def replace_word_with_digit(line: str):
    for item in convert_list:
        line = line.replace(item[0], item[1])
    return line


def get_calibration_number(line_input: str, replace_words: bool = True):
    print(line_input)
    if replace_words:
        line_input = replace_word_with_digit(line_input)
    # first num
    for character in line_input:
        if character in nums_list:
            first_num = character
            break
    line_input = reversed(line_input)
    for character in line_input:
        if character in nums_list:
            last_num = character
            break
    output = int(first_num + last_num)
    print(output)
    return output


def main():
    filename = "input_files/puzzle_1.txt"
    # filename = "./sample_1.txt"
    data = open_file(filename)
    output = sum(get_calibration_number(x.strip('\n')) for x in data)
    print(output)


main()
