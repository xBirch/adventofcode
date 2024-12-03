import csv
import re

def part1():
    with open('day3.txt', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ')
        y=0
        for row in spamreader:
            newnum=[]
            reg = re.compile('mul(\(\d+.\d+)\)')
            num = re.findall(reg, str(row))
            i=0
            while i < len(num):
                newnum.append(num[i].replace('(', ''))
                x = str(newnum[i]).split(',')
                y += int(x[0])*int(x[1])
                i += 1
        print(y)

def part2():
    with open('day3.txt', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ')
        y=0
        dis=0
        for row in spamreader:
            newnum=[]
            reg = re.compile("(mul\(\d+,\d+\)|don't\(\)|do\(\))")
            num = re.findall(reg, str(row))
            i=0
            while i < len(num):
                newnum.append(num[i].replace('(', ''))
                newnum[i] = newnum[i].replace(')', '')
                newnum[i]=newnum[i].replace('m', '')
                newnum[i]=newnum[i].replace('u', '')
                newnum[i]=newnum[i].replace('l', '')
                if newnum[i] == 'do':
                    dis = 0
                    i += 1
                elif newnum[i] == "don't" or dis == 1:
                    dis = 1
                    i += 1
                else:
                    x = str(newnum[i]).split(',')
                    y += int(x[0]) * int(x[1])
                    i += 1
        print(y)

part1()
part2()
