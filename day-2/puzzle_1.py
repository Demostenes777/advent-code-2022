input = open("/home/alaitz/Development/advent-code-2022/day-2/input.txt", "r")

lines = input.readlines()

points = 0

x = 1
y = 2
z = 3

lost = 0
draw = 3
win = 6

for line in lines:
    # A,X = Rock 
    # B,Y = Paper 
    # C,Z = Scissors 
    line = str.replace(line, "\n", "")
    if line == 'A X':
        points = points + draw + x
    elif line == 'A Y':
        points = points + win + y
    elif line == 'A Z':
        points = points + lost + z
    elif line == 'B X':
        points = points + lost + x
    elif line == 'B Y':
        points = points + draw + y
    elif line == 'B Z':
        points = points + win + z
    elif line == 'C X':
        points = points + win + x
    elif line == 'C Y':
        points = points + lost + y
    elif line == 'C Z':
        points = points + draw + z

print(points)
