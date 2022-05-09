import csv
import distances

# reads the distances csv file
filename = "distanceInfo.csv"
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)

    # creates a list of all addresses and a 2d array of distances
    allAddresses = next(csvreader)
    allDistances = []
    for row in csvreader:
        allDistances.append(row)


# uses the index of the address in allAddresses to find the distance in the 2d array allDistances
def findDistance(address1, address2):
    # find the index of the first address
    i = 0
    x = None
    for address in distances.allAddresses:
        if address1 in address:
            x = i
            break
        else:
            i += 1

    # find the index of the second address
    j = 0
    y = None
    for address in distances.allAddresses:
        if address2 in address:
            y = j
            break
        else:
            j += 1

    # use the indexes found to find the distance in the 2d array
    if allDistances[x][y] == '':
        return float(allDistances[y][x])
    else:
        return float(allDistances[x][y])
