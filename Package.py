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





    def __str__(self):
       return str(self.packageID) + ", " + self.address + ", " + self.city + ", " +self.state + ", " + self.deadline +", " +str(self.weight) +", " + self.notes


    def getPackageID(self):
        return self.packageID

    def getAddress(self):
        return self.address

