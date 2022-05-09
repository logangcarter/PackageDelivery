import csv
import datetime
import trucks


# HashTable class using chaining.
class ChainingHashTable:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=10):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        self.size = 0
        for i in range(initial_capacity):
            self.table.append([])

    # Inserts a new item into the hash table.
    def insert(self, key, item):  # does both insert and update
        # get the bucket list where this item will go.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # update key if it is already in the bucket
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                kv[1] = item
                return True

        # if not, insert the item to the end of the bucket list.
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    def search(self, key):
        # get the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        # search for the key in the bucket list
        for kv in bucket_list:
            if kv[0] == key:
                return kv[1]  # value
        return None

    # Removes an item with matching key from the hash table.
    def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present.
        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])


packageHash = ChainingHashTable()


class Package:
    def __init__(self, id, address, city, state, zip, deadline, mass, note, truckId, status, deliveryTime):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.mass = mass
        self.note = note
        self.truckId = truckId
        self.status = status
        self.deliveryTime = deliveryTime


# csv file with package information
filename = "packageInfo.csv"
# creates a list of package information
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    rows = []
    for row in csvreader:
        rows.append(row)
# adds package information from list to
for row in rows:
    id = int(row[0])
    address = row[1]
    city = row[2]
    state = row[3]
    zip = row[4]
    deadline = row[5]
    mass = row[6]
    if len(row) == 8:
        note = row[7]
    else:
        note = None
    truckId = 0
    status = "at the hub"
    deliveryTime = None

    packageHash.insert(id, Package(id, address, city, state, zip, deadline, mass, note, truckId, status, deliveryTime))
    packageHash.size += 1


def setPackagesStatusByTime(time):
    # parses the time string into a usable timedelta to compare
    time = time.split(':')
    hour = int(time[0])
    minute = int(time[1])
    time = datetime.timedelta(hours=hour, minutes=minute)

    i = 1
    while i < packageHash.size + 1:
        truckId = packageHash.search(i).truckId
        leaveTime = trucks.getLeaveTime(truckId)
        if time >= leaveTime:
            packageHash.search(i).status = "en route"
        if time >= packageHash.search(i).deliveryTime:
            packageHash.search(i).status = "delivered"
        i += 1

    return time


def updateAddress(package, address, city, state, zip):
    package.address = address
    package.city = city
    package.state = state
    package.zip = zip
