import time

dataFile = "data/day4.txt"

startTime = time.time()
sum = 0
cards = [1]

with open(dataFile, "r") as f:
    data = f.readlines()
    dataLength = len(data)
    for card__ in range(dataLength):
        card = data[card__].replace("\n", "").replace(" |", ":").split(":")

        sum += cards[card__]

        card_ = {"card": card__ + 1, "winning": [], "numbers": []}

        cardLength = len(card)
        for values_ in range(cardLength):
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

        numsWon = []

        for winning in card_["winning"]:
            if winning in card_["numbers"]:
                numsWon.append(winning)

        for x in range(len(numsWon)):
            if card__ + x + 1 >= len(cards):
                cards.append(cards[card__] + 1)
            else:
                cards[card__ + x + 1] += cards[card__]
        
        if len(numsWon) == 0:
            cards.append(1)
        
        cards[card__] = card_

print("completed in: " + str(round((time.time() - startTime) * 100000) / 100) + "ms")
print(sum)