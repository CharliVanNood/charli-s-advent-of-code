seeds = []
seedToSoil = []
seedToFertilizer = []

currentRead = "seeds"

with open("data/day5.txt", "r") as f:
    data = f.readlines()
    for line_ in range(len(data)):
        line = data[line_].replace("\n", "").replace(":", "").split(" ")
        if line[0] == "seeds":
            for seed in range(len(line) - 1):
                seeds.append(line[seed + 1])
        elif line[0] == "seed-to-soil":
            currentRead = "seed-to-soil"
        elif line[0] == "soil-to-fertilizer":
            currentRead = "soil-to-fertilizer"
        elif line[0] == "fertilizer-to-water":
            currentRead = "fertilizer-to-water"
        elif line[0] == "water-to-light":
            currentRead = "water-to-light"
        elif line[0] == "light-to-temperature":
            currentRead = "light-to-temperature"
        elif line[0] == "temperature-to-humidity":
            currentRead = "temperature-to-humidity"
        elif line[0] == "humidity-to-location":
            currentRead = "humidity-to-location"

        if currentRead == "seed-to-soil" and line[0] != "seed-to-soil" and line[0] != "":
            seedToSoil.append([int(line[0]), int(line[1]), int(line[2])])
        elif currentRead == "soil-to-fertilizer" and line[0] != "soil-to-fertilizer" and line[0] != "":
            seedToFertilizer.append([int(line[0]), int(line[1]), int(line[2])])

#for seed_ in range(len(seeds)):
for seed_ in range(1):
    seed = int(seeds[seed_])
    print(seed)

    seedToSoilResult = -1
    for seedToSoil__ in range(len(seedToSoil)):
        seedToSoil_ = seedToSoil[seedToSoil__]
        if seed >= seedToSoil_[1] and seed < seedToSoil_[1] + seedToSoil_[2]:
            offset = seedToSoil_[0] - seedToSoil_[1]
            result = seed + offset
            seedToSoilResult = result
    if seedToSoilResult == -1: seedToSoilResult = seed
    seed = seedToSoilResult
    print(seedToSoilResult)

    seedToFertilizerResult = -1
    for seedToFertilizer__ in range(len(seedToFertilizer)):
        seedToFertilizer_ = seedToFertilizer[seedToFertilizer__]
        if seed >= seedToFertilizer_[1] and seed < seedToFertilizer_[1] + seedToFertilizer_[2]:
            offset = seedToFertilizer_[0] - seedToFertilizer_[1]
            result = seed + offset
            seedToFertilizerResult = result
    if seedToFertilizerResult == -1: seedToFertilizerResult = seed
    seed = seedToFertilizerResult
    print(seedToFertilizerResult)
