sum = 0

with open("data/day2.txt", "r") as f:
    games = f.readlines()
    for game_ in range(len(games)):
        gamePossible = True
        gameData = {
            "game": 0,
            "red": 0,
            "green": 0,
            "blue": 0
        }

        game = games[game_].replace("\n", "").split(";")
        for value__ in range(len(game)):
            game__ = game[value__].replace(":", ",").split(",")
            for value_ in range(len(game__)):
                value = game__[value_].replace("Game ", "").split(" ")

                if len(value) == 1:
                    gameData["game"] = value[0]
                else:
                    gameData[value[2]] = int(value[1])

            if int(gameData["red"]) > 12 or int(gameData["green"]) > 13 or int(gameData["blue"]) > 14:
                gamePossible = False
        
        if gamePossible:
            sum += int(gameData["game"])

print(sum)