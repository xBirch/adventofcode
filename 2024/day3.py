import csv
import re

with open('day3.txt', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ')
    y=0
    for row in spamreader:
        newnum=[]
        num = list(re.findall(r'mul(\(\d+,\d+)\)', str(row)))
        i=0
        while i < len(num):
            newnum.append(num[i].replace('(', ''))
            x = str(newnum[i]).split(',')
            y += int(x[0])*int(x[1])
            i += 1
    print(y)
