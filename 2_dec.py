from common_core import open_file

filename = "input_files/puzzle_2.txt"
# filename = "./sample_2.txt"


class GameDie:
    def __init__(self):
        self.red = 0
        self.green = 0
        self.blue = 0

    def game_power(self):
        return self.red * self.green * self.blue

    def update_die(self, y):
        self.red = max(self.red, y[0])
        self.green = max(self.green, y[1])
        self.blue = max(self.blue, y[2])


def is_illegal_hand(rules, dice_list):
    for rule in rules:
        count = 0
        for dice in dice_list:
            if rule[1] in dice:
                count += int(dice.replace(' ', '').replace(rule[1], ''))
        if count > rule[0]:
            print(rule, count)
            return True
    return False


def analyse_game(rules, line):
    id = int(line.split(' ')[1][:-1])
    hands = line.split(': ')[-1].split(';')
    for hand in hands:
        dice = hand.split(',')
        if is_illegal_hand(rules, dice):
            return 0
    return id


def main_part_1():
    # 12 red cubes, 13 green cubes, and 14 blue cubes
    criteria = [(12, 'red'), (13, 'green'), (14, 'blue')]

    data = open_file(filename)
    output = sum(analyse_game(criteria, x.strip('\n')) for x in data)
    print(output)


def find_minimums(dice_list):
    output = []
    for colour in ['red', 'green', 'blue']:
        count = 0
        for dice in dice_list:
            if colour in dice:
                count += int(dice.replace(' ', '').replace(colour, ''))
        output.append(count)
    return output


def find_fewest_cubes(game):
    game_data = GameDie()
    hands = game.split(': ')[-1].split(';')
    for hand in hands:
        dice = hand.split(',')
        game_data.update_die(find_minimums(dice))

    return game_data.game_power()


def main_part_2():
    data = open_file(filename)
    output = sum(find_fewest_cubes(x.strip('\n')) for x in data)
    print(output)


# main_part_1()
main_part_2()
