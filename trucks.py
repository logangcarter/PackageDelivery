import packages
import distances
import datetime


class Truck:
    def __init__(self, truckId, inventory, mileage, route, leaveTime):
        self.truckId = truckId
        self.inventory = inventory
        self.mileage = mileage
        self.route = route
        self.leaveTime = leaveTime


# packages manually loaded onto trucks
# packages that must be delivered early
truck1 = Truck(1, [1, 4, 7, 8, 13, 14, 15, 16, 19, 20, 29, 30, 34, 37, 39, 40], 0, [], datetime.timedelta(hours=8))
# packages that are delayed
truck2 = Truck(2, [3, 5, 6, 18, 25, 26, 28, 31, 32, 36, 38], 0, [], datetime.timedelta(hours=9, minutes=5))
# wrong address and other packages
truck3 = Truck(3, [2, 9, 10, 11, 12, 17, 19, 21, 22, 23, 24, 27, 33, 35], 0, [],
               datetime.timedelta(hours=10, minutes=20))


# brute force searches all package addresses to find the next closest one
def findNearestNeighbor(address, truck):
    shortestDistance = 1000000
    nextPackage = None
    for package in truck.inventory:
        distance = distances.findDistance(address, packages.packageHash.search(package).address)
        # return a package if it is at the same address
        if distance == 0:
            return package, distance
        # hold the information for the package and address with the shortest distance
        elif distance < shortestDistance:
            shortestDistance = distance
            nextPackage = package
    # if there are no packages at the same address, return the closest neighbor and its distance
    return nextPackage, shortestDistance


# sorts the packages from the trucks unsorted inventory into a sorted route using the nearestNeighbor function
def findTruckRoute(truck):
    address1 = "4001 South 700 East"
    while len(truck.inventory) > 0:
        nextPackage, distance = findNearestNeighbor(address1, truck)
        packages.packageHash.search(nextPackage).truckId = truck.truckId
        truck.route.append(nextPackage)
        truck.inventory.remove(nextPackage)
        address1 = packages.packageHash.search(nextPackage).address


def getLeaveTime(truckId):
    if truckId == 1:
        return truck1.leaveTime
    if truckId == 2:
        return truck2.leaveTime
    if truckId == 3:
        return truck3.leaveTime
