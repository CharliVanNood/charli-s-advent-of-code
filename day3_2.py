sum = 0
grid = []
gears = []
gearsSorted = {}

def isNum(input_):
    try:
        num = int(input_)
        return True
    except:
        return False

def inGrid(x, y):
    if x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid):
        return True
    return False

def getSurrounding(x, y):
    symbolFound = False
    if inGrid(x + 1, y) and isNum(grid[y][x + 1]) == False and grid[y][x + 1] != ".":
        symbolFound = [grid[y][x + 1], x + 1, y]
    if inGrid(x - 1, y) and isNum(grid[y][x - 1]) == False and grid[y][x - 1] != ".":
        symbolFound = [grid[y][x - 1], x - 1, y]
    if inGrid(x, y + 1) and isNum(grid[y + 1][x]) == False and grid[y + 1][x] != ".":
        symbolFound = [grid[y + 1][x], x, y + 1]
    if inGrid(x, y - 1) and isNum(grid[y - 1][x]) == False and grid[y - 1][x] != ".":
        symbolFound = [grid[y - 1][x], x, y - 1]
    if inGrid(x + 1, y + 1) and isNum(grid[y + 1][x + 1]) == False and grid[y + 1][x + 1] != ".":
        symbolFound = [grid[y + 1][x + 1], x + 1, y + 1]
    if inGrid(x + 1, y - 1) and isNum(grid[y - 1][x + 1]) == False and grid[y - 1][x + 1] != ".":
        symbolFound = [grid[y - 1][x + 1], x + 1, y - 1]
    if inGrid(x - 1, y + 1) and isNum(grid[y + 1][x - 1]) == False and grid[y + 1][x - 1] != ".":
        symbolFound = [grid[y + 1][x - 1], x - 1, y + 1]
    if inGrid(x - 1, y - 1) and isNum(grid[y - 1][x - 1]) == False and grid[y - 1][x - 1] != ".":
        symbolFound = [grid[y - 1][x - 1], x - 1, y - 1]
    return symbolFound

with open("data/day3.txt", "r") as f:
    lines = f.readlines()
    for line_ in range(len(lines)):
        grid.append([])
        line = lines[line_].replace("\n", "")
        for character_ in range(len(line)):
            character = line[character_]
            grid[line_].append(character)

for y_ in range(len(grid)):
    y = grid[y_]
    for x_ in range(len(y)):
        x = y[x_]
        if isNum(x):
            foundSymbol = getSurrounding(x_, y_)
            if foundSymbol != False:
                fullNum = ""
                
                if inGrid(x_ - 2, y_) and isNum(grid[y_][x_ - 2]) and inGrid(x_ - 1, y_) and isNum(grid[y_][x_ - 1]):
                    fullNum = fullNum + grid[y_][x_ - 2]

                if inGrid(x_ - 1, y_) and isNum(grid[y_][x_ - 1]):
                    fullNum = fullNum + grid[y_][x_ - 1]

                if inGrid(x_, y_) and isNum(grid[y_][x_]):
                    fullNum = fullNum + grid[y_][x_]

                if inGrid(x_ + 1, y_) and isNum(grid[y_][x_ + 1]):
                    fullNum = fullNum + grid[y_][x_ + 1]

                if inGrid(x_ + 2, y_) and isNum(grid[y_][x_ + 2]) and inGrid(x_ + 1, y_) and isNum(grid[y_][x_ + 1]):
                    fullNum = fullNum + grid[y_][x_ + 2]

                if foundSymbol[0] == "*":
                    gears.append([foundSymbol[1], foundSymbol[2], x_, y_, fullNum])

for gear in gears:
    try:
        gear_ = gearsSorted[str(gear[0]) + "x" + str(gear[1])]
        gearsSorted[str(gear[0]) + "x" + str(gear[1])].append([gear[2], gear[3], gear[4]])
    except:
        gearsSorted[str(gear[0]) + "x" + str(gear[1])] = []
        gearsSorted[str(gear[0]) + "x" + str(gear[1])].append([gear[2], gear[3], gear[4]])

for gear in gearsSorted:
    numsFound = []

    for num in gearsSorted[gear]:
        if num[2] not in numsFound:
            numsFound.append(num[2])
    
    if len(numsFound) == 2:
        sum += int(numsFound[0]) * int(numsFound[1])

print(sum)
