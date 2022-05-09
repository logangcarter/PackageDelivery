import packages
import distances
import datetime
import trucks


class Driver:
    def __init__(self, schedule):
        self.schedule = schedule


# creates the first driver and tells it to leave at 8:00am
driver1 = Driver([])
driver1.schedule.append(["hub", "4001 South 700 East", 0.0, 0.0, datetime.timedelta(hours=8)])
# creates the second driver and tells it to leave at 9:05 (when the last packages arrive at the depot)
driver2 = Driver([])
driver2.schedule.append(["hub", "4001 South 700 East", 0.0, 0.0, datetime.timedelta(hours=9, minutes=5)])


# used within the createSchedule function
def updatePackageInfo(address1, address2, driver, package, startTime, totalMileage, truckMileage):
    MPH = 18
    distance = distances.findDistance(address1, address2)
    totalMileage += distance
    truckMileage += distance
    deliveryTime = startTime + datetime.timedelta(minutes=(distance / MPH * 60))
    packages.packageHash.search(package).deliveryTime = deliveryTime
    startTime = deliveryTime
    driver.schedule.append([package, address2, distance, round(totalMileage, 2), deliveryTime])
    return startTime, totalMileage, truckMileage


# chooses the different packages to find the route between, then calls the updatePackageInfo function
def createSchedule(driver, truck, startTime):
    trucks.findTruckRoute(truck)
    hub = "4001 South 700 East"
    i = 0
    startMileage = driver.schedule[-1][3]
    totalMileage = driver.schedule[-1][3]
    truckMileage = 0

    # from the hub to the first package
    firstPackage = truck.route[i]
    address2 = packages.packageHash.search(firstPackage).address
    startTime, totalMileage, truckMileage = \
        updatePackageInfo(hub, address2, driver, firstPackage, startTime, totalMileage, truckMileage)

    # from package to package
    while i < (len(truck.route) - 1):
        package1 = truck.route[i]
        package2 = truck.route[i + 1]
        address1 = packages.packageHash.search(package1).address
        address2 = packages.packageHash.search(package2).address
        startTime, totalMileage, truckMileage = \
            updatePackageInfo(address1, address2, driver, package2, startTime, totalMileage, truckMileage)
        i += 1

    # from the last package to the hub
    lastPackage = truck.route[-1]
    lastAddress = packages.packageHash.search(lastPackage).address
    updatePackageInfo(hub, lastAddress, driver, lastPackage, startTime, totalMileage, truckMileage)
    truck.mileage = driver.schedule[-1][3] - startMileage
