import re
from collections import defaultdict

deck = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10,"J":11, "Q":12, "K":13, "A":14}


def check_five_of_a_kind(hand):
    values = [*hand[0]]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if sorted(value_counts.values()) == [1,5]:
        return hand[1]
    return 0


def check_full_house(hand):
    values = [*hand[0]]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if sorted(value_counts.values()) == [2,3]:
        return hand[1]
    return 0


def check_four_of_a_kind(hand):
    values = [*hand[0]]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if sorted(value_counts.values()) == [1,4]:
        return hand[1]
    return 0


def check_three_of_a_kind(hand):
    values = [*hand[0]]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if set(value_counts.values()) == set([3,1]):
        return hand[1]
    else:
        return 0


def check_two_pairs(hand):
    values = [*hand[0]]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if sorted(value_counts.values())==[1,2,2]:
        return hand[1]
    else:
        return 0


def check_one_pairs(hand):
    values = [*hand[0]]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if 2 in value_counts.values():
        return hand[1]
    else:
        return 0


def part1():
    f = open('day7.txt', 'r')
    x = f.read().splitlines()
    hands = []
    order = []
    count = 1
    res = 0
    sum = 0
    rank = []
    newrank = []
    value = 0
    for i in x:
        hands = (i.split())
        if res == 0:
            res = check_five_of_a_kind(hands)
            value = ' 5'
        if res == 0:
            res = check_four_of_a_kind(hands)
            value = ' 4'
        if res == 0:
            res = check_full_house(hands)
            value = ' 3'
        if res == 0:
            res = check_three_of_a_kind(hands)
            value = ' 2'
        if res == 0:
            res = check_two_pairs(hands)
            value = ' 1'
        if res == 0:
            res = check_one_pairs(hands)
            value = ' 0'
            
        order.append(res + value)

        res = 0
        
    for i in order:
        rank.append(i.split())
        
    rank=sorted(rank, key=lambda x: int(x[-1]))
    

    x = 0
    while x < len(rank):
        newrank.append(re.search(r"((\d+)[^,'])", str(rank[x])).group(1))
        x += 1
    for i in order:
         sum += int(newrank[count-1])*count
         count += 1
         print(sum)



print(part1())