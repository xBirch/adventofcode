import csv
import re
units = {
    'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9',
}
reg = re.compile(r'(?:(one|two|three|four|five|six|seven|eight|nine|[1-9]))')
reglast = re.compile(r'(?=(one|two|three|four|five|six|seven|eight|nine|[1-9]))')

with open('day1.txt', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ')
    result = 0
    count = 0
    for row in spamreader:
        x = reg.search(row[0]).group()
        y = reglast.findall(row[0])[-1]
        x = x.split()
        y = y.split()
        if any(char.isdigit() for char in x) == False:
            x = [units[word]for word in x]
        if any(char.isdigit() for char in y) == False:
            y = [units[word] for word in y]
        
        z = x+y
        sum = int(''.join(z))
        result += sum
        count += 1
        print(result,count, x+y)


