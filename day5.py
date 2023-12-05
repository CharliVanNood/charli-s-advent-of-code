import time

startTime = time.time()

seeds = []
seedToSoil = []
seedToFertilizer = []
fertilizerToWater = []
waterToLight = []
lightToTemperature = []
temperatureToHumidity = []
humidityToLocation = []

locations = []

currentRead = "seeds"

def convertTo(seeds, array_):
    array_Result = -1
    for array___ in range(len(array_)):
        array__ = array_[array___]
        if seeds >= array__[1] and seeds < array__[1] + array__[2]:
            offset = array__[0] - array__[1]
            result = seeds + offset
            array_Result = result
    if array_Result == -1: array_Result = seeds
    return array_Result

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
        elif currentRead == "fertilizer-to-water" and line[0] != "fertilizer-to-water" and line[0] != "":
            fertilizerToWater.append([int(line[0]), int(line[1]), int(line[2])])
        elif currentRead == "water-to-light" and line[0] != "water-to-light" and line[0] != "":
            waterToLight.append([int(line[0]), int(line[1]), int(line[2])])
        elif currentRead == "light-to-temperature" and line[0] != "light-to-temperature" and line[0] != "":
            lightToTemperature.append([int(line[0]), int(line[1]), int(line[2])])
        elif currentRead == "temperature-to-humidity" and line[0] != "temperature-to-humidity" and line[0] != "":
            temperatureToHumidity.append([int(line[0]), int(line[1]), int(line[2])])
        elif currentRead == "humidity-to-location" and line[0] != "humidity-to-location" and line[0] != "":
            humidityToLocation.append([int(line[0]), int(line[1]), int(line[2])])

for seed_ in range(len(seeds)):
    seed = int(seeds[seed_])
    seed = convertTo(seed, seedToSoil)
    seed = convertTo(seed, seedToFertilizer)
    seed = convertTo(seed, fertilizerToWater)
    seed = convertTo(seed, waterToLight)
    seed = convertTo(seed, lightToTemperature)
    seed = convertTo(seed, temperatureToHumidity)
    seed = convertTo(seed, humidityToLocation)

    locations.append(seed)

print("completed in: " + str(round((time.time() - startTime) * 100000) / 100) + "ms")
print(min(locations))
