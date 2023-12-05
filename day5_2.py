import time

startTime = time.time()

seeds = []
ranges = []

seedToSoil = []
seedToFertilizer = []
fertilizerToWater = []
waterToLight = []
lightToTemperature = []
temperatureToHumidity = []
humidityToLocation = []

locations = []

currentRead = "seeds"

def convertTo(seeds, range_, array_):
    seedRanges = []

    print(seeds)

    seedsOffset = seeds

    while seedsOffset < seeds + range_:
        for array___ in range(len(array_)):
            array__ = array_[array___]

            # seeds + range_

            # lowest  value is 3037945983
            # highest value is 3781894260
            
            arrayMin = array__[1]
            arrayMax = arrayMin + array__[2]

            if seedsOffset >= arrayMin and seedsOffset < arrayMax:
                seedRanges.append([seedsOffset, arrayMax])
            
            if seedsOffset > arrayMin and seedsOffset < arrayMax:
                seedsOffset = arrayMax
            #elif seedsOffset > arrayMin and seedsOffset < arrayMax:
            #    seedsOffset = seeds + range_

            print(seedsOffset)

            #if seeds + range_ > arrayMax and seedsOffset > arrayMin:
            #    seedsOffset = arrayMax
            #elif seedsOffset > arrayMin:
            #    seedsOffset = arrayMin
            #else:
            #    seedsOffset = seeds + range_

    print(seedRanges)

    #array_Result = -1
    #for array___ in range(len(array_)):
    #    array__ = array_[array___]
    #    if seeds >= array__[1] and seeds < array__[1] + array__[2]:
    #        offset = array__[0] - array__[1]
    #        result = seeds + offset
    #        array_Result = result
    #if array_Result == -1: array_Result = seeds
    #return array_Result

with open("data/day5.txt", "r") as f:
    data = f.readlines()
    for line_ in range(len(data)):
        line = data[line_].replace("\n", "").replace(":", "").split(" ")
        if line[0] == "seeds":
            for seed in range(int((len(line) - 1) / 2)):
                seeds.append(int(line[(seed * 2) + 1]))
                ranges.append(int(line[(seed * 2) + 2]))
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
    range_ = int(ranges[seed_])

    seed = convertTo(seed, range_, seedToSoil)
    seed = convertTo(seed, range_, seedToFertilizer)
    seed = convertTo(seed, range_, fertilizerToWater)
    seed = convertTo(seed, range_, waterToLight)
    seed = convertTo(seed, range_, lightToTemperature)
    seed = convertTo(seed, range_, temperatureToHumidity)
    seed = convertTo(seed, range_, humidityToLocation)

    locations.append(seed)

print("completed in: " + str(round((time.time() - startTime) * 100000) / 100) + "ms")
print(min(locations))
