from common_core import open_file

# filename = "input_files/puzzle_5.txt"
filename = "input_files/sample_5.txt"

A_TO_B_IDENTIFIERS = [
    'seed-to-soil map:',
    'soil-to-fertilizer map:',
    'fertilizer-to-water map:',
    'water-to-light map:',
    'light-to-temperature map:',
    'temperature-to-humidity map:',
    'humidity-to-location map:'
]


class MapRule:
    def __init__(self, rule):
        if len(rule) == 3:
            self.upper_left = rule[1]
            self.upper_right = rule[1] + rule[2] - 1
            self.lower_left = rule[0]
            self.lower_right = rule[0] + rule[2] - 1
        elif len(rule) == 4:
            pass

    def update_rule(self):
        pass

    def __str__(self):
        return f"{self.upper_left} - {self.upper_right}" \
               f"\n{self.lower_left} - {self.lower_right}"


class Alamanac:

    def __init__(self, data, part_two=False):
        self.data = data
        if part_two:
            self.seeds = []
            seeds_line = [int(x) for x in data[0].split(':')[-1].split(' ') if x.isnumeric()]
            while seeds_line:
                seed_origin = seeds_line.pop(0)
                seed_range = seeds_line.pop(0)
                self.seeds += [seed_origin + x for x in range(seed_range)]

        else:
            self.seeds = [int(x) for x in data[0].split(':')[-1].split(' ') if x.isnumeric()]

        self.maps = [self.find_mapping(x) for x in A_TO_B_IDENTIFIERS]

    def find_mapping(self, map_id):
        i = 0
        output = []
        while self.data[i] != map_id:
            i += 1
        i += 1
        while i < len(self.data) and self.data[i] != '':
            info = [int(x) for x in self.data[i].split(' ')]
            output.append(info)
            i += 1
        return output

    def get_next_map_number(self, mapper, current):
        for input_line in mapper:
            if input_line[1] <= current <= input_line[1] + input_line[2]:
                next_map = input_line[0] + current - input_line[1]
                return next_map
        return current

    def create_seed_to_location_path(self, seed):
        current_path = [seed]
        for mapper in self.maps:
            a = self.get_next_map_number(mapper, current_path[-1])
            current_path.append(a)
        print("Seed {}, soil {}, fertilizer {}, water {}, light {}, temperature {}, humidity {}, location {}".format(
            current_path[0],
            current_path[1],
            current_path[2],
            current_path[3],
            current_path[4],
            current_path[5],
            current_path[6],
            current_path[7],
        ))
        return current_path[-1]

    def merge_maps(self):
        bottom_map = self.maps.pop(-1)
        to_merge_map = self.maps.pop(-1)
        to_merge_rules = [MapRule(x) for x in to_merge_map]
        bottom_rules = [MapRule(x) for x in bottom_map]
        new_rules = []
        for u_rule in to_merge_rules:
            for l_rule in bottom_rules:
                new_rules += merge_rules(u_rule, l_rule)
        for r in new_rules:
            print(r)

        # print(new_rules)


def merge_rules(a, b):
    a_left = a.lower_left
    a_right = a.lower_right
    b_left = b.upper_left
    b_right = b.upper_right
    # print(a_left, a_right, b_left, b_right)

    # case A - rules are non conflicting
    if a_right < b_left or b_right < a_left:
        print("The rules are non conflicting!")
        return [a, b]

    # case B
    if a_left > b_left and a_right < b_right:
        print("a is completely contained in b!")
        return []

    # case C
    if a_left < b_left and a_right > b_right:
        print("b is completely contained in a!")
        return []

    # case D
    if a_right > b_left:
        print("a overlaps on the left!")
        x = MapRule([a.lower_left, a.upper_left, b.upper_left - a.lower_left])
        y = MapRule([b.lower_left, a.upper_left + (b.upper_left - a.lower_left), a.lower_right - b.upper_left + 1])
        z = MapRule(
            [b.lower_left + b.upper_right - a.lower_right + 1, a.lower_right + 1, b.upper_right - a.lower_right])
        return [x, y, z]

    # case E
    if a_left < b_right:
        print("a overlaps on the right!")
        return []


def main():
    data = [x.strip('\n') for x in open_file(filename)]
    seed_converter = Alamanac(data)
    output = []
    seed_converter.merge_maps()
    # for seed in seed_converter.seeds:
    #     output.append(seed_converter.create_seed_to_location_path(seed))

    # print(min(output))


main()
# main_part_2()
