import csv
import json

def getData(fname):
    with open(fname, 'r') as csvFile:
        lines = csv.reader(csvFile)
        for row in lines:
            yield row
    
if __name__=="__main__":
    di = {}
    data = getData('airlines.csv')

    maxAirlineTravelled = [float('-inf'),'']
    minAirlineTravelled = [float('inf'),'']

    skipFirstLine = True
    for line in data:
        if skipFirstLine:
            skipFirstLine = False
            continue
        val = di.get(line[1])
        if not val:
            di[line[1]] = 1
        else:
            di[line[1]] = val+1
    for k, v in di.items():
        if v>maxAirlineTravelled[0]:
            maxAirlineTravelled[0] = v
            maxAirlineTravelled[1] = k
        if v<minAirlineTravelled[0]:
            minAirlineTravelled[0] = v
            minAirlineTravelled[1] = k
    with open('airlines.json', 'w') as jsonDumpFile:
        json.dump(di,jsonDumpFile, indent=4)
    with open('airlines.json', 'r') as jsonFile:
        print(jsonFile.read())
    print("Maximum Airline Travelled: ",maxAirlineTravelled)
    print("Minimum Airline Travelled: ",minAirlineTravelled)
            