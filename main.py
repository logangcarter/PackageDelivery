# Logan Carter / 000990702
import packages
import trucks
import drivers


# creates the schedule for the first truck
drivers.createSchedule(drivers.driver1, trucks.truck1, drivers.driver1.schedule[-1][4])
# creates the schedule for the second truck
drivers.createSchedule(drivers.driver2, trucks.truck2, drivers.driver2.schedule[-1][4])
# updates address for package with wrong address
packages.updateAddress(packages.packageHash.search(9), "410 S State St", "Salt Lake City", "UT", "84111")
# creates the schedule for the third truck and adds it to driver1's schedule
drivers.createSchedule(drivers.driver1, trucks.truck3, drivers.driver1.schedule[-1][4])

totalMileage = drivers.driver1.schedule[-1][3] + drivers.driver2.schedule[-1][3]
# INTERFACE
print("Thank you for using WGUPS Package Management System.")
print("The mileage for today's route is as follows:")
print("Total Mileage:", totalMileage)
print("Truck 1:", trucks.truck1.mileage)
print("Truck 2:", trucks.truck2.mileage)
print("Truck 3:", trucks.truck3.mileage)
print()
time = input("What time would you like to check the status of the packages at? (Please enter military time in form HH:MM)\n")
# set the packages status based on the time inputted
compareTime = packages.setPackagesStatusByTime(time)
print("Package status check at:", time)

# if package's scheduled delivery time has not passed do not print the delivery time, only the status
i = 1
while i < packages.packageHash.size + 1:
    if compareTime >= packages.packageHash.search(i).deliveryTime:
        print("ID:", packages.packageHash.search(i).id,
              "| Address:", packages.packageHash.search(i).address,
              "| City:", packages.packageHash.search(i).city,
              "| Zip:", packages.packageHash.search(i).zip,
              "| Weight:", packages.packageHash.search(i).mass,
              "| Status:", packages.packageHash.search(i).status,
              "| Delivery Time:", packages.packageHash.search(i).deliveryTime,
              "| Deadline:", packages.packageHash.search(i).deadline)
    else:
        print("ID:", packages.packageHash.search(i).id,
              "| Address:", packages.packageHash.search(i).address,
              "| City:", packages.packageHash.search(i).city,
              "| Zip:", packages.packageHash.search(i).zip,
              "| Weight:", packages.packageHash.search(i).mass,
              "| Status:", packages.packageHash.search(i).status,
              "| Deadline:", packages.packageHash.search(i).deadline)
    i += 1
