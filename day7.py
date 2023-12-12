import re
from collections import defaultdict
import operator

deck = {"J": '1', "2": '2', "3": '3', "4": '4', "5": '5', "6": '6', "7": '7', "8": '8', "9": '9', "T": '10', "Q": '12',
        "K": '13', "A": '14'}


def check_five_of_a_kind(hand):
    values = [*hand[0]]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    if sorted(value_counts.values()) == [5]:
        hand.append(7)
        return hand
    return 0





def check_four_of_a_kind(hand):
    values = [*hand[0]]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    if sorted(value_counts.values()) == [1, 4]:
        hand.append(6)
        return hand
    return 0


def check_full_house(hand):
    values = [*hand[0]]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    if sorted(value_counts.values()) == [2, 3]:
        hand.append(5)
        return hand
    return 0


def check_three_of_a_kind(hand):
    values = [*hand[0]]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    if set(value_counts.values()) == set([3, 1]):
        hand.append(4)
        return hand
    else:
        return 0


def check_two_pairs(hand):
    values = [*hand[0]]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    if sorted(value_counts.values()) == [1, 2, 2]:
        hand.append(3)
        return hand
    else:
        return 0


def check_one_pairs(hand):
    values = [*hand[0]]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    if 2 in value_counts.values():
        hand.append(2)
        return hand
    else:
        return 0


def part1():
    f = open('day7.txt', 'r')
    x = f.read().splitlines()
    order = []
    res = 0
    sum = 0
    rank = 1
    newres = []

    for i in x:
        hands = (i.split())
        if res == 0:
            res = check_five_of_a_kind(hands)

        if res == 0:
            res = check_four_of_a_kind(hands)

        if res == 0:
            res = check_full_house(hands)

        if res == 0:
            res = check_three_of_a_kind(hands)

        if res == 0:
            res = check_two_pairs(hands)

        if res == 0:
            res = check_one_pairs(hands)

        if res == 0:
            hands.append(1)
            res = hands

        for s in res[0]:
            newres.append(deck.get(s))
        newres.append(res[1])
        newres.append(res[2])
        order.append(newres)
        newres = []
        res = 0
    order = sorted(order, key=lambda j: (int(j[6]), int(j[0]), int(j[1]), int(j[2]), int(j[3]), int(j[4])))
    for i in order:
        sum += int(i[5]) * rank
        rank += 1

    return sum


print(part1())
