class Package:
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


    def __str__(self):
       return "   " + str(self.packageID) + "     " + self.address + ",  " + self.city + ", " +self.state + ", " + str(self.zip) +", " + self.deadline +", " +str(self.weight)  +" Kgs" + ", " + self.notes + ", " +str(self.delivery_time) + ", " + str(self.time_left_hub) + ", " + str(self.status)

    def getPackageID(self):
        return self.packageID

    def getAddress(self):
        return self.address


