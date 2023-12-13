from common_core import open_file

filename = "input_files/puzzle_6.txt"
# filename = "input_files/sample_6.txt"


def create_file_race_stats(data):
    times = data.pop(0)
    distance = data.pop(0)
    times = [int(x.replace(' ', '')) for x in times.split(':')[-1].split(' ') if x.replace(' ', '').isnumeric()]
    distance = [int(x.replace(' ', '')) for x in distance.split(':')[-1].split(' ') if x.replace(' ', '').isnumeric()]
    return list(zip(times, distance))


def find_winning_strategies(ratio):
    output = 0
    for i in range(ratio[0]+1):
        boat_distance = (i * 1) * (ratio[0] - i)
        if boat_distance > ratio[1]:
            output += 1
    return output


def get_prod(a_list):
    result = 1
    for a in a_list:
        result *= a
    return result

def main():
    # data = [x.strip('\n') for x in open_file(filename)]
    # print(data)
    # races = create_file_race_stats(data)
    # output = []
    # for race in races:
    #     output.append(find_winning_strategies(race))
    # return get_prod(output)
    return find_winning_strategies((46807866, 214117714021024))




print(main())
# main_part_2()
