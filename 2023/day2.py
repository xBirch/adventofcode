import csv
import re


reg = re.compile(r'(\d+.)([(blue)|(red)|(green)])')
regid = re.compile(r'([(Game)])(.\d+)')
red = True
blue = True
green = True
redm = 0
bluem = 0
greenm = 0
count = 0
with open('day2.txt', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\n')
    sum = 0
    min = 0
    i = 0
    for row in spamreader:
        games = reg.findall(row[0])
        id = regid.findall(row[0])
        trash, idnum = id[0]
        for num in games:
            n, t=games[i]
            if 'r' in t:
                    if int(n) > 12:
                        red = False
                    if int(n) > redm:
                         redm = int(n)
            if 'b' in t:
                    if int(n) > 14:
                        blue = False
                    if int(n) > bluem:
                         bluem = int(n)
            if 'g' in t:
                    if int(n) > 13:
                        green = False
                    if int(n) > greenm:
                         greenm = int(n)
            i += 1   
            if len(games)== i:
                i = 0
              
        if red and blue and green == True:
            sum += int(idnum)
        else:
            red = True
            blue = True
            green = True
        min += (redm * bluem * greenm) 
        redm = 0
        bluem = 0
        greenm = 0
    print(sum)
    print(min)