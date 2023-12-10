from common_core import open_file

filename = "input_files/puzzle_4.txt"


# filename = "input_files/sample_4.txt"

def score_match(winning_cards, match_cards):
    output = 0
    for card in match_cards:
        if card in winning_cards:
            output += 1
    if output == 0:
        return 0
    return 2 ** (output - 1)


def find_bonus_cards(winning_cards, match_cards):
    output = 0
    for card in match_cards:
        if card in winning_cards:
            output += 1
    return output


def analyse_file(data):
    output = 0

    for match in data:
        match_details = match.split(':')
        # match_id = int(match_details[0].split(' ')[1])
        winning_cards = [int(x) for x in match_details[1].split('|')[0].split(' ') if x.isnumeric()]
        player_cards = [int(x) for x in match_details[1].split('|')[1].split(' ') if x.isnumeric()]
        output += score_match(winning_cards, player_cards)
        print(winning_cards, player_cards, score_match(winning_cards, player_cards))
    # extract the data from the game
    # pass data into calc
    # add to the output
    return output

def analyse_file_2(data):
    output = {}
    for match in data:
        match_details = match.split(':')
        match_id = int(match_details[0].split(' ')[-1])

        if str(match_id) in output:
            output[str(match_id)] += 1
        else:
            output[str(match_id)] = 1

        winning_cards = [int(x) for x in match_details[1].split('|')[0].split(' ') if x.isnumeric()]
        player_cards = [int(x) for x in match_details[1].split('|')[1].split(' ') if x.isnumeric()]
        bonus_cards = find_bonus_cards(winning_cards, player_cards)
        while bonus_cards != 0:
            if str(match_id+bonus_cards) in output:
                output[str(match_id+bonus_cards)] += output[str(match_id)]
            else:
                output[str(match_id+bonus_cards)] = output[str(match_id)]
            bonus_cards -= 1
    total = 0
    for value in output.values():
        total += value
    return total


def main_part_1():
    data = [x.strip('\n') for x in open_file(filename)]
    output = analyse_file(data)
    print(output)


def main_part_2():
    data = [x.strip('\n') for x in open_file(filename)]
    output = analyse_file_2(data)
    print(output)


# main_part_1()
main_part_2()
