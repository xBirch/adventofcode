import csv
import re

def part1():
    with open('day1.txt', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ')
        p1=[]
        p2=[]
        p3=0
        for row in spamreader:
            p1.append(str(re.search(r'^\D*(\d+)', str(row)).group(1)))
            p2.append(str(re.search(r'(\d+)\D+$', str(row)).group(1)))

        p1.sort()
        p2.sort()
        x=0
        for number1 in p1:
            p3 += abs(int(p2[x])-int(str(number1)))
            x+=1
        print(p3)

def part2():
    with open('day1.txt', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ')
        p1 = []
        p2 = []
        p3 = 0
        for row in spamreader:
            p1.append(str(re.search(r'^\D*(\d+)', str(row)).group(1)))
            p2.append(str(re.search(r'(\d+)\D+$', str(row)).group(1)))
        p = 0
        x = 0
        for number1 in p1:
            for number2 in p2:
                if number1 in number2:
                    p += 1
            p3 += int(p1[x]) * p
            x += 1
            p = 0
        print(p3)

part1()
part2()