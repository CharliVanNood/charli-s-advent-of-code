sum = 0

with open("data/day1.txt", "r") as f:
    inputs = f.readlines()
    for line in range(len(inputs)):
        line_ = inputs[line].replace("\n", "")
        line_ = line_.replace("one", "o1ne").replace("two", "tw2o").replace("three", "th3ree").replace("four", "fo4ur")
        line_ = line_.replace("five", "fi5ve").replace("six", "si6x").replace("seven", "se7ven").replace("eight", "ei8ght")
        line_ = line_.replace("nine", "ni9ne")
        firstCharacter = ""
        lastCharacter = ""

        Character = 0

        characters = []

        for character_ in range(len(line_)):
            character = line_[character_]
            try:
                int_ = int(character)
                characters.append(int_)
            except:
                continue
        
        firstCharacter = characters[0]
        lastCharacter = characters[len(characters) - 1]
        
        Character = int(str(firstCharacter) + str(lastCharacter))
        sum += Character
        print(Character)

print(sum)