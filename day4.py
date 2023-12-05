sum = 0

with open("data/day4.txt", "r") as f:
    data = f.readlines()
    for card_ in range(len(data)):
        card = data[card_].replace("\n", "").replace(" |", ":").split(":")

        card_ = {"card": 0, "winning": [], "numbers": []}
        numsWon = []

        for values_ in range(len(card)):
            values = card[values_].split(" ")
            values__ = []
            if values[0] != "Card":
                for num in values:
                    if num != "":
                        values__.append(num)
                if len(values__) == 10:
                    card_["winning"] = values__
                else:
                    card_["numbers"] = values__
            else:
                card_["card"] = values[1]

        for winning in card_["winning"]:
            if winning in card_["numbers"]:
                numsWon.append(winning)

        print(numsWon)
        points = 0
        if len(numsWon) > 0:
            points = 1
            for x_ in range(len(numsWon) - 1):
                points *= 2
        print(points)
        sum += points

print(sum)