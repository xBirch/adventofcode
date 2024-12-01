

def part1():
    ans=1
    f = open('day6.txt', 'r')
    f = f.read().splitlines()
    time = f[0].split(' ', 1)
    time.remove('Time:')
    time = [int(i) for i in time[0].split() if i.isdigit()]
    dist = f[1].split(' ', 1)
    dist.remove('Distance:')
    dist = [int(i) for i in dist[0].split() if i.isdigit()]
    e = 0
    for i  in time:
        loop=0
        sec = i
        j = sec
        y = dist[e]
        while sec > 0:
            speed = 1*sec
            newtime= j-sec
            res = newtime * speed
            if res > y:
                loop += 1
            sec-=1
        e += 1
        ans *= loop
    return ans


def part2():
    ans=0
    f = open('day6.txt', 'r')
    f = f.read().splitlines()
    time = f[0].split(' ', 1)
    time.remove('Time:')
    time = [int(i) for i in time[0].split() if i.isdigit()]
    time = int(''.join(map(str, time)))
    dist = f[1].split(' ', 1)
    dist.remove('Distance:')
    dist = [int(i) for i in dist[0].split() if i.isdigit()]
    dist = int(''.join(map(str, dist)))
    sec = time
    j = sec
    y = dist
    while sec > 0:
        speed = 1*sec
        newtime= j-sec
        res = newtime * speed
        if res > y:
            ans += 1
        sec-=1
 
    return ans

print('part1: ', part1() , 'part2: ', part2())