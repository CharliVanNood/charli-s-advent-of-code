#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;

int main()
{
	string data[256];

	string seeds[22];
	string seedToSoil[50][3];

	string currentRead = "seeds";

	string line;
	ifstream file("Z:/charli-s-advent-of-code/data/day5.txt");

	int line_ = 0;
	while (getline(file, line)) {
		data[line_] = line;
		line_ += 1;
	}
	file.close();

	int line__ = 0;
	for (int line_ = 0; line_ < sizeof(data) / sizeof(string); line_++) {
		string line = data[line_];
		if (line != "") {
			if (line.find(":") < 100) {
				line = line.replace(line.find(":"), 1, "");
			}

			string lineSplit[22];

			int split__ = 0;
			stringstream split_(line);
			string splitChar;
			while (split_ >> splitChar) {
				lineSplit[split__] = splitChar;
				split__++;
			}
			if (lineSplit[0] == "seeds") {
				cout << "seeds found" << endl;
				for (int seed = 1; seed < sizeof(lineSplit) / sizeof(string) - 1; seed++) {
					seeds[seed - 1] = lineSplit[seed];
				}
			}
			else if (
				lineSplit[0] == "seed-to-soil" || 
				lineSplit[0] == "soil-to-fertilizer" || 
				lineSplit[0] == "fertilizer-to-water" || 
				lineSplit[0] == "water-to-light" || 
				lineSplit[0] == "light-to-temperature" || 
				lineSplit[0] == "temperature-to-humidity" || 
				lineSplit[0] == "humidity-to-location"
				) {
				currentRead = lineSplit[0];
				line__ = 0;
			}

			if (currentRead == "seed-to-soil" && lineSplit[0] != currentRead) {
				cout << lineSplit[0] << endl;
				seedToSoil[line__][0] = lineSplit[0];
				seedToSoil[line__][1] = lineSplit[1];
				seedToSoil[line__][2] = lineSplit[2];
			}

			line__++;
		}
	}
}
