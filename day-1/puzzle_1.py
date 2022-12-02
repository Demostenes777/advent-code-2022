input = open("/home/alaitz/Development/advent-code-2022/day-1/input.txt", "r")

lines = input.readlines()
max = 0
sum = 0

for line in lines:
    if line == '\n':
        if sum > max:
            max = sum
        sum = 0
    else:
        sum = sum + int(str.replace(line, "\n", ""))
print(max)