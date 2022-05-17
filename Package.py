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

        #If I add this attribute, I need to update my package objects that I'm inserting to the hashtable

        #self.delivery_status = delivery_status

        self.delivery_time = None



# Need to add timestamp attribute which returns time at delivery


    def __str__(self):
       return str(self.packageID) + ", " + self.address + ", " + self.city + ", " +self.state + ", " + self.deadline +", " +str(self.weight) +", " + self.notes

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (
            self.package_ID, self.address, self.city, self.state, self.deadline,self.weight,self.notes,self.delivery_status)

    def getPackageID(self):
        return self.packageID

    def getAddress(self):
        return self.address

