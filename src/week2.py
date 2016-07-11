import re

hand = open('regex_sum_298004.txt')
sum = 0
for line in hand:
    line = line.rstrip()
    x = re.findall('[0-9]+', line)
    if len(x) > 0:
        for item in x:
            sum += int(item)

print(sum)
