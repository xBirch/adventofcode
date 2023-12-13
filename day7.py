from collections import Counter

deck = {"J": '1', "2": '2', "3": '3', "4": '4', "5": '5', "6": '6', "7": '7', "8": '8', "9": '9', "T": '10', "Q": '12',
        "K": '13', "A": '14'}

def check_hand(hand):
    values = [*hand[0]]
    joker = values.count('J')
    values = [c for c in values if c != 'J']
    counts = sorted(Counter(values).values(), reverse=True)
    if not counts:
        counts = [0]
    if counts[0] + joker == 5:
        hand.append(6)
        return hand
    if counts[0] + joker == 4:
        hand.append(5)
        return hand
    if counts[0] + joker == 3 and counts[1] == 2:
        hand.append(4)
        return hand
    if counts[0] + joker == 3:
        hand.append(3)
        return hand
    if counts[0] == 2 and (joker or counts[1] == 2):
        hand.append(2)
        return hand
    if counts[0] == 2 or joker:
        hand.append(1)
        return hand
    hand.append(0)
    return hand



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
        res = check_hand(hands)
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

print(sum)
