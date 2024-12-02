import csv

with open('day2.txt', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ')
    last=0
    unsafe=0
    skip=1
    p=0
    lastx=0
    for row in spamreader:
        for number in row:
            if skip != 1:
                x=int(number) - last
                if x not in range(1,4):
                    if x not in range(-3, 0):
                        unsafe=1
                if lastx < 0 < x:
                    unsafe = 1
                elif lastx > 0 > x:
                    unsafe = 1
                lastx=x
            else:
                skip=0
            last=int(number)
            if unsafe == 1:
                break
        if unsafe == 0:
            p+=1
        unsafe=0
        lastx = 0
        skip=1
    print(p)
