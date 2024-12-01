
f = open('day9.txt', 'r')
x = f.read().splitlines()


def part1():
    ans=0
    for i in x:
        rows = []
        oldrow = [i.split()]
        row = i.split()
        while row[-1] != 0:
            c = 0
            for j in row:
                if c != 0:
                    rows.append(int(row[c]) - int(row[c-1]))
                c += 1
            oldrow.append(rows)
            row = rows
            rows = []

        rows = 0
        row = 0
        c = 0
        for step in oldrow[::-1]:

            if c % 2:
                row = step[-1]
                c += 1

            if row != 0:
                rows = rows + int(row)
            c += 1

        ans += rows
    return ans


def part2():
    ans = 0
    for i in x:
        rows = []
        oldrow = [i.split()]
        row = i.split()
        while row[-1] != 0:
            c = 0
            for j in row:
                if c != 0:
                    rows.append(int(row[c]) - int(row[c - 1]))
                c += 1
            oldrow.append(rows)
            row = rows
            rows = []

        rows = 0
        row = 0
        c = 0
        for step in oldrow[::-1]:

            if c % 2:
                row = step[0]
                c += 1

            if c != 0:
                rows = int(row) - rows
            c += 1

        ans += rows
    return ans


print('part1 :',part1())
print('part2 :',part2())
