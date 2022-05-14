from Package import Package
from HashTable import HashTable
import datetime

import math



p1 = Package(1,'195 W Oakland Ave','Salt Lake City','UT',84115,'10:30 AM',21,'')
p2 = Package(2,'2530 S 500 E','Salt Lake City','UT',84106,'EOD',44,'')
p3 = Package(3,'233 Canyon Rd','Salt Lake City','UT',84103,'EOD',2,'Can only be on truck 2')
p4 = Package(4,'380 W 2880 S','Salt Lake City','UT',84115,'EOD',4,'')
p5 = Package(5,'410 S State St','Salt Lake City','UT',84111,'EOD',5,'')
p6 = Package(6,'3060 Lester St','West Valley City','UT',84119,'10:30 AM',88,'Delayed on flight---will not arrive to depot until 9:05 am')
p7 = Package(7,'1330 2100 S','Salt Lake City','UT',84103,'EOD',9,'')
p8 = Package(8,'300 State St','Salt Lake City','UT',84103,'EOD',9,'')
p9 = Package(9,'300 State St','Salt Lake City','UT',84103,'EOD',2,'Wrong address listed')
p10 = Package(10,'600 E 900 South','Salt Lake City','UT',84105,'EOD',1,'')
p11 = Package(11,'2600 Taylorsville Blvd','Salt Lake City','UT',84118,'EOD',1,'')
p12 = Package(12,'3575 W Valley Central Station bus Loop','West Valley City','UT',84119,'EOD',1,'')
p13 = Package(13,'2010 W 500 S','Salt Lake City','UT',84104,'10:30 AM',2,'')
p14 = Package(14,'4300 S 1300 E','Millcreek','UT',84117,'10:30 AM',88,'Must be delivered with 15, 19')
p15 = Package(15,'4580 S 2300 E','Holladay','UT',84117,'9:00 AM',4,'')
p16 = Package(16,'4580 S 2300 E','Holladay','UT',84117,'10:30 AM',88,'Must be delivered with 13, 19')
p17 = Package(17,'3148 S 1100 W','Salt Lake City','UT',84119,'EOD',2,'')
p18 = Package(18,'1488 4800 S','Salt Lake City','UT',84123,'EOD',6,'Can only be on truck 2')
p19 = Package(19,'177 W Price Ave','Salt Lake City','UT',84115,'EOD',37,'')
p20 = Package(20,'3595 Main St','Salt Lake City','UT',84115,'10:30 AM',37,'Must be delivered with 13, 15')
p21 = Package(21,'3595 Main St','Salt Lake City','UT',84115,'EOD',3,'')
p22 = Package(22,'6351 South 900 East','Murray','UT',84121,'EOD',2,'')
p23 = Package(23,'5100 South 2700 West','Salt Lake City','UT',84118,'EOD',5,'')
p24 = Package(24,'5025 State St','Murray','UT',84107,'EOD',7,'')
p25 = Package(25,'5383 South 900 East #104','Salt Lake City','UT',84117,'10:30 AM',7,'Delayed on flight---will not arrive to depot until 9:05 am')
p26 = Package(26,'5383 South 900 East #104','Salt Lake City','UT',84117,'EOD',25,'')
p27 = Package(27,'1060 Dalton Ave S','Salt Lake City','UT',84104,'EOD',5,'')
p28 = Package(28,'2835 Main St','Salt Lake City','UT',84115,'EOD',7,'Delayed on flight---will not arrive to depot until 9:05 am')
p29 = Package(29,'1330 2100 S','Salt Lake City','UT',84106,'10:30 AM',2,'')
p30 = Package(30,'300 State St','Salt Lake City','UT',84103,'10:30 AM',1,'')
p31 = Package(31,'3365 S 900 W','Salt Lake City','UT',84119,'10:30 AM',1,'')
p32 = Package(32,'3365 S 900 W','Salt Lake City','UT',84119,'EOD',1,'Delayed on flight---will not arrive to depot until 9:05 am')
p33 = Package(33,'2530 S 500 E','Salt Lake City','UT',84106,'EOD',1,'')
p34 = Package(34,'4580 S 2300 E','Holladay','UT',84117,'10:30 AM',2,'')
p35 = Package(35,'1060 Dalton Ave S','Salt Lake City','UT',84104,'EOD',88,'')
p36 = Package(36,'2300 Parkway Blvd','West Valley City','UT',84119,'EOD',88,'Can only be on truck 2')
p37 = Package(37,'410 S State St','Salt Lake City','UT',84111,'10:30 AM',2,'')
p38 = Package(38,'410 S State St','Salt Lake City','UT',84111,'EOD',9,'Can only be on truck 2')
p39 = Package(39,'2010 W 500 S','Salt Lake City','UT',84104,'EOD',9,'')
p40 = Package(40,'380 W 2880 S','Salt Lake City','UT',84115,'10:30 AM',45,'')

packageHashTable = HashTable()



packageHashTable.insert(1, p1)
packageHashTable.insert(2, p2)
packageHashTable.insert(3, p3)
packageHashTable.insert(4, p4)
packageHashTable.insert(5, p5)
packageHashTable.insert(6, p6)
packageHashTable.insert(7, p7)
packageHashTable.insert(8, p8)
packageHashTable.insert(9, p9)
packageHashTable.insert(10, p10)
packageHashTable.insert(11, p11)
packageHashTable.insert(12, p12)
packageHashTable.insert(13, p13)
packageHashTable.insert(14, p14)
packageHashTable.insert(15, p15)
packageHashTable.insert(16, p16)
packageHashTable.insert(17, p17)
packageHashTable.insert(18, p18)
packageHashTable.insert(19, p19)
packageHashTable.insert(20, p20)
packageHashTable.insert(21, p21)
packageHashTable.insert(22, p22)
packageHashTable.insert(23, p23)
packageHashTable.insert(24, p24)
packageHashTable.insert(25, p25)
packageHashTable.insert(26, p26)
packageHashTable.insert(27, p27)
packageHashTable.insert(28, p28)
packageHashTable.insert(29, p29)
packageHashTable.insert(30, p30)
packageHashTable.insert(31, p31)
packageHashTable.insert(32, p32)
packageHashTable.insert(33, p33)
packageHashTable.insert(34, p34)
packageHashTable.insert(35, p35)
packageHashTable.insert(36, p36)
packageHashTable.insert(37, p37)
packageHashTable.insert(38, p38)
packageHashTable.insert(39, p39)
packageHashTable.insert(40, p40)

#value = packageHashTable.search(25)
#print(value)




# I think both space complexity and time complexity is O(n^2) for this 2d array

distances2dArray = [
    [0, 7.2, 3.8, 11, 2.2, 3.5, 10.9, 8.6, 7.6, 2.8, 6.4, 3.2, 7.6, 5.2, 4.4, 3.7, 7.6, 2, 3.6, 6.5, 1.9, 3.4, 2.4, 6.4,
     2.4, 5, 3.6],
    [7.2, 0, 7.1, 6.4, 6, 4.8, 1.6, 2.8, 4.8, 6.3, 7.3, 5.3, 4.8, 3, 4.6, 4.5, 7.4, 6, 5, 4.8, 9.5, 10.9, 8.3, 6.9, 10,
     4.4, 13],
    [3.8, 7.1, 0, 9.2, 4.4, 2.8, 8.6, 6.3, 5.3, 1.6, 10.4, 3, 5.3, 6.5, 5.6, 5.8, 5.7, 4.1, 3.6, 4.3, 3.3, 5, 6.1, 9.7,
     6.1, 2.8, 7.4],
    [11, 6.4, 9.2, 0, 5.6, 6.9, 8.6, 4, 11.1, 7.3, 1, 6.4, 11.1, 3.9, 4.3, 4.4, 7.2, 5.3, 6, 10.6, 5.9, 7.4, 4.7, 0.6,
     6.4, 10.1, 10.1],
    [2.2, 6, 4.4, 5.6, 0, 1.9, 7.9, 5.1, 7.5, 2.6, 6.5, 1.5, 7.5, 3.2, 2.4, 2.7, 1.4, 0.5, 1.7, 6.5, 3.2, 5.2, 2.5, 6,
     4.2, 5.4, 5.5],
    [3.5, 4.8, 2.8, 6.9, 1.9, 0, 6.3, 4.3, 4.5, 1.5, 8.7, 0.8, 4.5, 3.9, 3, 3.8, 5.7, 1.9, 1.1, 3.5, 4.9, 6.9, 4.2, 9,
     5.9, 3.5, 7.2],
    [10.9, 1.6, 8.6, 8.6, 7.9, 6.3, 0, 4, 4.2, 8, 8.6, 6.9, 4.2, 4.2, 8, 5.8, 7.2, 7.7, 6.6, 3.2, 11.2, 12.7, 10, 8.2,
     11.7, 5.1, 14.2],
    [8.6, 2.8, 6.3, 4, 5.1, 4.3, 4, 0, 7.7, 9.3, 4.6, 4.8, 7.7, 1.6, 3.3, 3.4, 3.1, 5.1, 4.6, 6.7, 8.1, 10.4, 7.8, 4.2,
     9.5, 6.2, 10.7],
    [7.6, 4.8, 5.3, 11.1, 7.5, 4.5, 4.2, 7.7, 0, 4.8, 11.9, 4.7, 0.6, 7.6, 7.8, 6.6, 7.2, 5.9, 5.4, 1, 8.5, 10.3, 7.8,
     11.5, 9.5, 2.8, 14.1],
    [2.8, 6.3, 1.6, 7.3, 2.6, 1.5, 8, 9.3, 4.8, 0, 9.4, 1.1, 5.1, 4.6, 3.7, 4, 6.7, 2.3, 1.8, 4.1, 3.8, 5.8, 4.3, 7.8,
     4.8, 3.2, 6],
    [6.4, 7.3, 10.4, 1, 6.5, 8.7, 8.6, 4.6, 11.9, 9.4, 0, 7.3, 12, 4.9, 5.2, 5.4, 8.1, 6.2, 6.9, 11.5, 6.9, 8.3, 4.1,
     0.4, 4.9, 11, 6.8],
    [3.2, 5.3, 3, 6.4, 1.5, 0.8, 6.9, 4.8, 4.7, 1.1, 7.3, 0, 4.7, 3.5, 2.6, 2.9, 6.3, 1.2, 1, 3.7, 4.1, 6.2, 3.4, 6.9,
     5.2, 3.7, 6.4],
    [7.6, 4.8, 5.3, 11.1, 7.5, 4.5, 4.2, 7.7, 0.6, 5.1, 12, 4.7, 0, 7.3, 7.8, 6.6, 7.2, 5.9, 5.4, 1, 8.5, 10.3, 7.8,
     11.5, 9.5, 2.8, 14.1],
    [5.2, 3, 6.5, 3.9, 3.2, 3.9, 4.2, 1.6, 7.6, 4.6, 4.9, 3.5, 7.3, 0, 1.3, 1.5, 4, 3.2, 3, 6.9, 6.2, 8.2, 5.5, 4.4,
     7.2, 6.4, 10.5],
    [4.4, 4.6, 5.6, 4.3, 2.4, 3, 8, 3.3, 7.8, 3.7, 5.2, 2.6, 7.8, 1.3, 0, 0.6, 6.4, 2.4, 2.2, 6.8, 5.3, 7.4, 4.6, 4.8,
     6.3, 6.5, 8.8],
    [3.7, 4.5, 5.8, 4.4, 2.7, 3.8, 5.8, 3.4, 6.6, 4, 5.4, 2.9, 6.6, 1.5, 0.6, 0, 5.6, 1.6, 1.7, 6.4, 4.9, 6.9, 4.2, 5.6,
     5.9, 5.7, 8.4],
    [7.6, 7.4, 5.7, 7.2, 1.4, 5.7, 7.2, 3.1, 7.2, 6.7, 8.1, 6.3, 7.2, 4, 6.4, 5.6, 0, 7.1, 6.1, 7.2, 10.6, 12, 9.4, 7.5,
     11.1, 6.2, 13.6],
    [2, 6, 4.1, 5.3, 0.5, 1.9, 7.7, 5.1, 5.9, 2.3, 6.2, 1.2, 5.9, 3.2, 2.4, 1.6, 7.1, 0, 1.6, 4.9, 3, 5, 2.3, 5.5, 4,
     5.1, 5.2],
    [3.6, 5, 3.6, 6, 1.7, 1.1, 6.6, 4.6, 5.4, 1.8, 6.9, 1, 5.4, 3, 2.2, 1.7, 6.1, 1.6, 0, 4.4, 4.6, 6.6, 3.9, 6.5, 5.6,
     4.3, 6.9],
    [6.5, 4.8, 4.3, 10.6, 6.5, 3.5, 3.2, 6.7, 1, 4.1, 11.5, 3.7, 1, 6.9, 6.8, 6.4, 7.2, 4.9, 4.4, 0, 7.5, 9.3, 6.8,
     11.4, 8.5, 1.8, 13.1],
    [1.9, 9.5, 3.3, 5.9, 3.2, 4.9, 11.2, 8.1, 8.5, 3.8, 6.9, 4.1, 8.5, 6.2, 5.3, 4.9, 10.6, 3, 4.6, 7.5, 0, 2, 2.9, 6.4,
     2.8, 6, 4.1],
    [3.4, 10.9, 5, 7.4, 5.2, 6.9, 12.7, 10.4, 10.3, 5.8, 8.3, 6.2, 10.3, 8.2, 7.4, 6.9, 12, 5, 6.6, 9.3, 2, 0, 4.4, 7.9,
     3.4, 7.9, 4.7],
    [2.4, 8.3, 6.1, 4.7, 2.5, 4.2, 10, 7.8, 7.8, 4.3, 4.1, 3.4, 7.8, 5.5, 4.6, 4.2, 9.4, 2.3, 3.9, 6.8, 2.9, 4.4, 0,
     4.5, 1.7, 6.8, 3.1],
    [6.4, 6.9, 9.7, 0.6, 6, 9, 8.2, 4.2, 11.5, 7.8, 0.4, 6.9, 11.5, 4.4, 4.8, 5.6, 7.5, 5.5, 6.5, 11.4, 6.4, 7.9, 4.5,
     0, 5.4, 10.6, 7.8],
    [2.4, 10, 6.1, 6.4, 4.2, 5.9, 11.7, 9.5, 9.5, 4.8, 4.9, 5.2, 9.5, 7.2, 6.3, 5.9, 11.1, 4, 5.6, 8.5, 2.8, 3.4, 1.7,
     5.4, 0, 7, 1.3],
    [5, 4.4, 2.8, 10.1, 5.4, 3.5, 5.1, 6.2, 2.8, 3.2, 11, 3.7, 2.8, 6.4, 6.5, 5.7, 6.2, 5.1, 4.3, 1.8, 6, 7.9, 6.8,
     10.6, 7, 0, 8.3],
    [3.6, 13, 7.4, 10.1, 5.5, 7.2, 14.2, 10.7, 14.1, 6, 6.8, 6.4, 14.1, 10.5, 8.8, 8.4, 13.6, 5.2, 6.9, 13.1, 4.1, 4.7,
     3.1, 7.8, 1.3, 8.3, 0]
]

#print(len(distances2dArray))
#print(type(distances2dArray))


hub = '4001 South 700 East'
addressDictionary = {'4001 South 700 East': 0,
               '1060 Dalton Ave S': 1,
               '1330 2100 S': 2,
               '1488 4800 S': 3,
               '177 W Price Ave': 4,
               '195 W Oakland Ave': 5,
               '2010 W 500 S': 6,
               '2300 Parkway Blvd': 7,
               '233 Canyon Rd': 8,
               '2530 S 500 E': 9,
               '2600 Taylorsville Blvd': 10,
               '2835 Main St': 11,
               '300 State St': 12,
               '3060 Lester St': 13,
               '3148 S 1100 W': 14,
               '3365 S 900 W': 15,
               '3575 W Valley Central Station bus Loop': 16,
               '3595 Main St': 17,
               '380 W 2880 S': 18,
               '410 S State St': 19,
               '4300 S 1300 E': 20,
               '4580 S 2300 E': 21,
               '5025 State St': 22,
               '5100 South 2700 West': 23,
               '5383 South 900 East #104': 24,
               '600 E 900 South': 25,
               '6351 South 900 East': 26
                     }

# need distance lookup function that takes two addresses and looks up distance between those

def lookupDistance(address1,address2):

    row = addressDictionary[address1]
    column = addressDictionary[address2]
    distanceAtRowAndColumn = distances2dArray[row][column]
    return distanceAtRowAndColumn




#print(lookupDistance('2600 Taylorsville Blvd','4300 S 1300 E'))

#packages with high priority will be loaded onto truck 1

#truck1 = [p1.packageID,p13,p14,p15,p19,p16,p20,p29,p30,p31,p34,p37,p40]

#truck1 = [1,13,14,15,19,16,20,29,30,31,34,37,40]
truck1 = [1,13,14,15,19,16,20,29,30,31,34,37,40]
#truck1 = [p1.packageID,p13.packageID,p14.packageID,p15.packageID,p19.packageID,p16.packageID,p20.packageID,p29.packageID,p30.packageID,p31.packageID,p34.packageID,p37.packageID,p40.packageID]

truck2 = [p3,p18,p36,p38,p6,p7,p36,p38,p2,p4,p5,p8,p9,p10,p11,p25]
truck3 = [p39,p35,p33,p27,p26,p24,p23,p22,p21,p17,p12]


# truck3 = # rest of EOD packages to deliver

numPackagesTruck1 = len(truck1)
numPackagesTruck2 = len(truck2)
numPackagesTruck3 = len(truck3)
#print(len(truck1))
#print(len(truck2))
#print(len(truck3))

packagesLeft = 40 - (numPackagesTruck1 + numPackagesTruck2 + numPackagesTruck3)

#print(f"{'{:,.2f}'.format(packagesLeft)} packages left to deliver")

# TRUCK SPEED   -->> 18mph is equivalent to 0.3 miles / minute


#print(f"Packages on truck #1: {(truck1)}")


# Here I'm thinking... the 1st parameter of the lookupDistance function will change upon arriving at the next location.
# For example, original location w/ a loaded truck is the hub. Once the first package is delivered ...
# the function will take in the updated current address (the last package delivered + the next closest delivery address

Truck1StartLocation = hub

# for package in truck1:
#     listOfDistances = [lookupDistance(hub,package.address)]
#
#     #print(listOfDistances)
#
#     print(sorted(listOfDistances))


# numPackagesTruck1 = truck1.count()


# def dispatchTruck1():
#     for x in truck1:
#         print(x.getPackageID())
#         print(x.getAddress())
#      miles = lookupDistance(hub,x.address)
#     listOfMiles = []
#     listOfMiles.append(miles)
#     print(lookupDistance(hub,x.address))
#     print(f"miles: {'{:,.2f}'.format(miles)}")
#     print("\n")

# def deliverFirstPackage():
#     for x in truck1:
#         lookupDistance(hub,x.address)
#



def dispatchTruck1():
    for x in truck1:
        print(x.getPackageID())
        print(x.getAddress())
        miles = lookupDistance(hub,x.address)
        listOfMiles = []
        listOfMiles.append(miles)
        print(lookupDistance(hub,x.address))
        print(f"miles: {'{:,.2f}'.format(miles)}")

        minDistance = min(listOfMiles)
        #print(listOfMiles)
        print("\n")

#dispatchTruck1()




def sortTruck1():
    distanceList = []
    for packages in truck1:
        distanceFromHub = lookupDistance(hub,packages.address)
        distanceList.append(distanceFromHub)
        #print(distanceList)
        #sortedList = distanceList.sort()
        minDistance = min(distanceList)
        print(minDistance)



def findMinDistance(currentDistance, destination):
    for x in truck1:
        lookupDistance()





#sortTruck1()


def deliverPackages():
    numPackages = len(truck1)

    while numPackages > 0:
        print("There are packages left to deliver\n")
        print(f"This many: {'{:,.2f}'.format(numPackages)}")
        numPackages -=1

#deliverPackages()


#Don/t do list of miles (distances)

#loop through packages on the truck, and get the distance

# need a min value search
# create a variable called minDistance -> see if

def deliveryTruck1():
    currentAddress = hub
    minDistance = 10000000
    truckMiles = 0
    numPackagesTruck1 = len(truck1)

    while numPackagesTruck1 > 0:

        for packageID in truck1:
            package = packageHashTable.search(packageID)
            distance = lookupDistance(currentAddress,package.address)


            if distance < minDistance:
                minDistance = distance
                minPackage = package



        truckMiles += distance
        currentAddress = minPackage.address
        #print(packageID)


        #truck1.remove(packageID)

    # if numPackagesTruck1 == 0:
    #     distanceToHub = lookupDistance(currentAddress,hub)
    #     truckMiles += distanceToHub


    print(f"Total miles on truck 1: {'{:,.2f}'.format(truckMiles)}")
    print("All packages have been delievered")

        # deliver minPackage
        # update totMiles on truck1 w/ minDistance variable
        # currentAddress = delivery address of minPackage
        # remove packageID from truck list




            #print(lookupDistance(currentAddress,packageID.))
#deliveryTruck1()



