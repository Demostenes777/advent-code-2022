input = open("/home/alaitz/Development/advent-code-2022/day-1/input.txt", "r")

lines = input.readlines()
sum = 0
sums = []

for line in lines:
    if line == '\n':
        sums.append(sum)
        sum = 0
    else:
        sum = sum + int(str.replace(line, "\n", ""))

total = sorted(sums)[-1] + sorted(sums)[-2] + sorted(sums)[-3]
print(total)