import re

f = open('day8.txt', 'r')
x = f.read().split()

reg = re.compile(r'(\w+)')
inst = ''
col = []
right = []
left = []
c = 0
y = 0
count = 0
for i in x:
    if c == 0:
        inst = [*i]
    else:
        if y == 0:
            col.append(i)
        if y == 2:
            left.append(reg.search(i).group())
        y += 1
        if y == 4:
            right.append(reg.search(i).group())
            y = 0
    c = 1
c = 0
ans = col[0]
x = col.index('AAA')
while ans != 'ZZZ':
    if inst[c] == 'L':
        ans = left[x]
    if inst[c] == 'R':
        ans = right[x]
    x = col.index(ans)
    c += 1
    if c == len(inst):
        c = 0
    count += 1


print(ans, count)