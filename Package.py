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



        #If I add this attribute, I need to update my package objects that I'm inserting to the hashtable

        #self.delivery_status = delivery_status

# Need to add timestamp attribute which returns time at delivery


    def __str__(self):
       return "   " + str(self.packageID) + "     " + self.address + ",  " + self.city + ", " +self.state + ", " + str(self.zip) +", " + self.deadline +", " +str(self.weight)  +" Kgs" + ", " + self.notes + ", " +str(self.delivery_time) + ", " + str(self.time_left_hub) + ", " + str(self.status)

    # def __str__(self):
    #     return "%s, %s, %s, %s, %s, %s, %s, %s"  (
    #         str(self.packageID), self.address, self.city, self.state, self.deadline,self.weight,str(self.notes),str(self.delivery_time),str(self.time_left_hub))

    def getPackageID(self):
        return self.packageID

    def getAddress(self):
        return self.address


