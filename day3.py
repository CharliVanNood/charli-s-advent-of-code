sum = 0
grid = []

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
        symbolFound = True
    if inGrid(x - 1, y) and isNum(grid[y][x - 1]) == False and grid[y][x - 1] != ".":
        symbolFound = True
    if inGrid(x, y + 1) and isNum(grid[y + 1][x]) == False and grid[y + 1][x] != ".":
        symbolFound = True
    if inGrid(x, y - 1) and isNum(grid[y - 1][x]) == False and grid[y - 1][x] != ".":
        symbolFound = True
    if inGrid(x + 1, y + 1) and isNum(grid[y + 1][x + 1]) == False and grid[y + 1][x + 1] != ".":
        symbolFound = True
    if inGrid(x + 1, y - 1) and isNum(grid[y - 1][x + 1]) == False and grid[y - 1][x + 1] != ".":
        symbolFound = True
    if inGrid(x - 1, y + 1) and isNum(grid[y + 1][x - 1]) == False and grid[y + 1][x - 1] != ".":
        symbolFound = True
    if inGrid(x - 1, y - 1) and isNum(grid[y - 1][x - 1]) == False and grid[y - 1][x - 1] != ".":
        symbolFound = True
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
    numFound = False
    for x_ in range(len(y)):
        if x_ == 0: numFound = False
        x = y[x_]
        if isNum(x):
            foundSymbol = getSurrounding(x_, y_)
            if foundSymbol == True and numFound == False:
                numFound = True
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
                sum += int(fullNum)
        else:
            numFound = False

print(sum)
