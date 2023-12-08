"""
Advent of Code 2023 - Day 7

Start: 8. Dec 2023 - 19:30
Finish: 8. Dec 2023 - 20:05
Notes:
    Idk why but I wanted to do sth with a custom score
"""
import math

strength = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
strength_part2 = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
hands = []


def read_data():
    with open("data", "r") as file:
        for line in file:
            line = line.replace("\n", "")
            cards = list(line.split(" ")[0])
            bid = int(line.split(" ")[1])
            hands.append((cards, bid))
            analyze_hand(cards)


def analyze_hand(cards):
    card_count = {}
    score = 0
    order_score = 0
    for index, card in enumerate(cards):
        order_score += (strength.index(card)+1) * math.pow(len(strength), len(cards)-index)
    score += order_score
    max_order_score = math.pow(len(strength), len(cards)+1)

    for card in cards:
        card_count[card] = card_count.get(card, 0) + 1
    for card in card_count:
        if card_count[card] == 5:
            score += 1000000000 * max_order_score
        elif card_count[card] == 4:
            score += 10000000 * max_order_score
        elif card_count[card] == 3:
            score += 100000 * max_order_score
        elif card_count[card] == 2:
            score += 1000 * max_order_score
        else:
            pass
    return score


def part1():
    print("⋆⁺₊❅⋆ ⁺₊❆⋆⋆⁺₊❅⋆ ⁺₊❆⋆")
    print("Solution Part 1")
    for i in range(len(hands)):
        hand = hands[i]
        score = analyze_hand(hand[0])
        hands[i] = (hand[0], hand[1], score)

    sorted_hands = sorted(hands, key=lambda x: x[2])
    total_winnings = 0
    for i in range(len(sorted_hands)):
        total_winnings += sorted_hands[i][1] * (i+1)
    print(total_winnings)


def analyze_hand_part2(cards):
    card_count = {}
    score = 0
    order_score = 0
    for index, card in enumerate(cards):
        order_score += (strength_part2.index(card)+1) * math.pow(len(strength), len(cards)-index)
    score += order_score
    max_order_score = math.pow(len(strength), len(cards)+1)
    for card in cards:
        card_count[card] = card_count.get(card, 0) + 1

    jokers = card_count.get("J", 0)

    if jokers != 5:
        card_count["J"] = 0
        max_cards = 0
        most_common = None
        for card in card_count:
                if card_count[card] > max_cards:
                    most_common = card
                    max_cards = card_count[card]
        card_count[most_common] += jokers

    for card in card_count:
        if card_count[card] == 5:
            score += 1000000000 * max_order_score
        elif card_count[card] == 4:
            score += 10000000 * max_order_score
        elif card_count[card] == 3:
            score += 100000 * max_order_score
        elif card_count[card] == 2:
            score += 1000 * max_order_score
        else:
            pass
    return score

def part2():
    print("⋆⁺₊❅⋆ ⁺₊❆⋆⋆⁺₊❅⋆ ⁺₊❆⋆")
    print("Solution Part 2")
    for i in range(len(hands)):
        hand = hands[i]
        score = analyze_hand_part2(hand[0])
        hands[i] = (hand[0], hand[1], score)

    sorted_hands = sorted(hands, key=lambda x: x[2])
    total_winnings = 0

    for i in range(len(sorted_hands)):
        total_winnings += sorted_hands[i][1] * (i+1)
    print(total_winnings)



def main():
    print("⋆⁺₊❅⋆₊☃️ 🎄 ☃️₊❅⁺₊❆⋆")
    print("Solution for Day 7")
    read_data()
    part1()
    part2()
    print("⋆⁺₊❅⋆ ⁺₊❆⋆⋆⁺₊❅⋆ ⁺₊❆⋆")


if __name__ == "__main__":
    main()

