import re


def check(s, seed):
    loc = 0
    c = 0
    count = 0
    while c != 1:
        source = int(src.search(s[count]).group())
        destination = int(dest.search(s[count]).group())
        ranges = int(rang.search(s[count]).group())
        test = range(source, source + ranges)
        if int(seed) in test:
            loc = int(seed) - source + destination
        else:
            if loc == 0:
                loc = seed
        count += 1
        if count >= len(s):
            c += 1
            count = 0
    return loc


c = 0
f = open('day5.txt', 'r')
x = f.read().splitlines()
reg = re.compile(r'(\d.+)')
src = re.compile(r'[^\d](\d+)')
dest = re.compile(r'(^\d+)')
rang = re.compile(r'(\d+$)')
seed = [reg.search(x[0]).group(1)]
seed = seed[0].split()
sts = []
stf = []
ftw = []
wtl = []
ltt = []
tth = []
htl = []
for i in x:
    if 2 < c < 27:
        sts.append(i)
    if 29 < c < 60:
        stf.append(i)
    if 62 < c < 72:
        ftw.append(i)
    if 73 < c < 101:
        wtl.append(i)
    if 102 < c < 114:
        ltt.append(i)
    if 116 < c < 129:
        tth.append(i)
    if 130 < c < 139:
        htl.append(i)
    c += 1
c = 0
ans = 0
seeds = []
start = ''
i = 0
for s in seed:
    if i == 1:
        seeds = ([*range(int(start), int(s)+int(start))])
        i = 0
        while c != len(seeds):
            soil = check(sts, seeds[c])
            fertilizer = check(stf, soil)
            water = check(ftw, fertilizer)
            light = check(wtl, water)
            temp = check(ltt, light)
            humid = check(tth, temp)
            loc = check(htl, humid)
            c += 1
            print(c)
            if loc < ans or ans == 0:
                ans = loc

    else:
        start = s
        i += 1

print(ans)

'''    if 2 < c < 5:
        sts.append(i)
    if 6 < c < 10:
        stf.append(i)
    if 11 < c < 16:
        ftw.append(i)
    if 17 < c < 20:
        wtl.append(i)
    if 21 < c < 25:
        ltt.append(i)
    if 26 < c < 29:
        tth.append(i)
    if 30 < c < 33:
        htl.append(i)'''