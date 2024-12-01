import re

f = open('day3.txt').read()
sch = [re.findall("\\d|.", line) for line in f.splitlines()]   

def adjfind(n, c, schematic):
    adj = [(0, 1), (0, -1), (1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1)]
    for d, cha in adj:
        if 0 <= d + n < len(schematic) and 0 <= cha+c < len(schematic):
            if schematic[d+n][cha+c] != "." and not schematic[d+n][cha+c].isdigit():
                return True
    return False

num_pos = []
for i in range(len(sch)):
    num = []
    for j in range(len(sch[i])):
        if not sch[i][j].isdigit() and num:
            num_pos.append(num)
            num = []
        if sch[i][j].isdigit():
            num.append((i, j))
    if num:
        num_pos.append(num)

ans = 0
for num in num_pos:
    if any(adjfind(n, c, sch) for n,c in num):
        ans += int("".join(sch[n][c] for n,c in num))

print(ans)