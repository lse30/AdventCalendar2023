from common_core import open_file

filename = "input_files/puzzle_7.txt"
# filename = "input_files/sample_7.txt"

convert_dict = {
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    'T': 'A',
    'J': 'B',
    'Q': 'C',
    'K': 'D',
    'A': 'E',
}

convert_dict_2 = {
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    'T': 'A',
    'J': '1',
    'Q': 'C',
    'K': 'D',
    'A': 'E',
}

v = {
    '6': 'Five of a kind',
    '5': 'Four of a kind',
    '4': 'Full house',
    '3': 'Three of a kind',
    '2': 'Two pair',
    '1': 'One pair',
    '0': 'High card'
}


class Hand:

    def __init__(self, cards, bid):
        self.bid = int(bid)
        self.cards = list(cards)
        self.hand_class = self.analyse_hand_jokers()
        self.score = self.score_hand_2()

    def analyse_hand(self):
        """
        returns a score based on the type of hand
        class 6: Five of a kind
        class 5: Four of a kind
        class 4: Full house
        class 3: Three of a kind
        class 2: Two pair
        class 1: One pair
        class 0: High card
        """
        card_set_len = len(set(self.cards))
        if card_set_len == 1:
            # 5 of a kind
            return 6
        if card_set_len == 2:
            a = self.cards.count(self.cards[0])
            if a == 1 or a == 4:
                # 4 of a kind
                return 5
            # full house
            return 4
        if card_set_len == 3:
            counts = [self.cards.count(x) for x in self.cards]
            if 3 in counts:
                # 3 of a kind
                return 3
            # 2 pair
            return 2
        if card_set_len == 4:
            # 1 pair
            return 1
        if card_set_len == 5:
            # high card
            return 0
        raise Exception("Something went wrong!")

    def analyse_hand_jokers(self):
        if 'J' not in self.cards:
            return self.analyse_hand()

        new_cards = [x for x in self.cards if x != 'J']
        card_set_len = len(set(new_cards))
        output = 0
        if card_set_len == 1 or card_set_len == 0:
            # 5 of a kind
            output = 6
        elif card_set_len == 2:
            if len(new_cards) == 4 and new_cards.count(new_cards[0]) == 2:
                # full house
                output = 4
            else:
                output = 5
        elif card_set_len == 3:
            # 3 of a kind
            output = 3
        elif card_set_len == 4:
            # 1 pair
            output = 1
        # print(new_cards, v[str(output)])
        return output

    def score_hand(self):
        values = f'0x{self.hand_class + 1}' + ''.join([convert_dict[x] for x in self.cards])
        values = int(values, 16)
        return values

    def score_hand_2(self):
        values = f'0x{self.hand_class + 1}' + ''.join([convert_dict_2[x] for x in self.cards])
        values = int(values, 16)
        return values


def parse_file(filename):
    data = [x.strip('\n') for x in open_file(filename)]
    output = []
    for line in data:
        cards, bid = line.split(' ')
        output.append((cards, bid))
    return output


def score_match(games):
    games.sort(key=lambda x: x.score)
    rank = 1
    output = 0
    for game in games:
        output += (game.bid * rank)
        rank += 1
    return output


def main():
    hands = parse_file(filename)
    games = [Hand(x[0], x[1]) for x in hands]
    return score_match(games)


print(main())
