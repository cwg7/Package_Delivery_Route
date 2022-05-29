
#This is the Package Class
#The ability to create packages is generated here, as well as the ability of having access to various dynamic attributes of package objects
class Package:
    #This is the constructor

    def __init__(self, packageID, address,city, state, zip, deadline, weight, notes):
        self.packageID = packageID
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes

        self.delivery_time = None
        self.time_left_hub = None

        self.status = 'at hub'

    #function returns attribute data of package objects
    def __str__(self):
       return "   " + str(self.packageID) + "     " + self.address + ",  " + self.city + ", " +self.state + ", " + str(self.zip) +", " + self.deadline +", " +str(self.weight)  +" Kgs" + ", " + self.notes + ", " +str(self.delivery_time) + ", " + str(self.time_left_hub) + ", " + "Delivery status:  " + str(self.status)

    #function returns package id
    def getPackageID(self):
        return self.packageID

    #function returns delivery address of package
    def getAddress(self):
        return self.address


