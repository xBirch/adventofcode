f = open('day4.txt', 'r')
res = 0
newcard = 0
lastcard = []
cop = 0
num = []
x = f.read().splitlines()
count = 0
c = 0
scratch = []
winning = []


for i in x:
    card = i.split()
    for j in card:
        if count < 7 and count > 1:
            scratch.append(j)
        if count > 7:
            winning.append(j)
        count += 1
    num.append(set(scratch).intersection(winning))
    lastcard.append(len(num[c]))
    count = 0
    scratch.clear()
    winning.clear()
    if len(num[c]) == 10:
        res += 512
    elif len(num[c]) == 9:
        res += 256
    elif len(num[c]) == 8:
        res += 128
    elif len(num[c]) == 7:
        res += 64
    elif len(num[c]) == 6:
        res += 32
    elif len(num[c]) == 5:
        res += 16
    elif len(num[c]) == 4:
        res += 8
    elif len(num[c]) == 3:
        res += 4
    elif len(num[c]) == 2:
        res += 2
    elif len(num[c]) == 1:
        res += 1
    c += 1

print('part1 :', res, ' part2 :', newcard)