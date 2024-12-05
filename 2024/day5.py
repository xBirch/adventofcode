import csv

def part1():
    with open('day5.txt', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ')
        instr = []
        update = []
        for row in spamreader:
            if '|' in str(row):
                instr.append(str(row))
            if ',' in str(row):
                update.append(row)
        for row in update:
            row = str(row).split(',')
            for n in row:
                for r in instr:
                    r.replace("[", '')
                    rr = str(r).split('|')
                    if str(n[0]) in rr[0]:
                        print(n, rr)

part1()
