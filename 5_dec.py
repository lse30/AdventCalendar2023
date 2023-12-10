from common_core import open_file

# filename = "input_files/puzzle_5.txt"
filename = "input_files/sample_5.txt"

TO_SOIL_ID = 'seed-to-soil map:'
TO_FERT_ID = 'soil-to-fertilizer map:'
TO_WATER_ID = 'fertilizer-to-water map:'
TO_LIGHT_ID = 'water-to-light map:'
TO_TEMP_ID = 'light-to-temperature map:'
TO_HUMIDITY_ID = 'temperature-to-humidity map:'
TO_LOCATION_ID = 'humidity-to-location map:'

class Alamanac:

    def __init__(self, data):
        self.data = data
        seeds = data[0].split(':')[-1].split(' ')
        self.seeds = [int(x) for x in seeds if x.isnumeric()]
        self.soil_map = self.find_mapping(TO_SOIL_ID)
        self.fert_map = self.find_mapping(TO_FERT_ID)
        self.water_map = self.find_mapping(TO_WATER_ID)
        self.light_map = self.find_mapping(TO_LIGHT_ID)
        self.temp_map = self.find_mapping(TO_TEMP_ID)
        self.humidity_map = self.find_mapping(TO_HUMIDITY_ID)
        self.location_map = self.find_mapping(TO_LOCATION_ID)

    def find_mapping(self, map_id):
        i = 0
        output = []
        while self.data[i] != map_id:
            i += 1
        i += 1
        while self.data[i] != '' or i <= len(self.data):
            info = [int(x) for x in self.data[i].split(' ')]
            output.append(info)
            i += 1
        print(self.data[i])
        return output



def main_part_1():
    data = [x.strip('\n') for x in open_file(filename)]
    mapping = Alamanac(data)
    print(mapping.seeds)

#
# def main_part_2():
#     data = [x.strip('\n') for x in open_file(filename)]
#     output = analyse_file_2(data)
#     print(output)


main_part_1()
# main_part_2()