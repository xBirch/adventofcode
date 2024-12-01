
def part1():
    current = 0
    result = 0
    for line in x:
        for l in line:
            t = ord(l)
            current += t
            current *= 17
            current %= 256
        result += current
        current = 0
    return result


def part2():
    current = 0
    result = 0
    for line in x:
        for l in line:
            t = ord(l)
            current += t
            current *= 17
            current %= 256
        result += current
        current = 0
    return result

f = open('day15.txt', 'r')
x = f.read().split(sep=',')

print('Part 1:', part1(), 'Part 2: ', part2())
