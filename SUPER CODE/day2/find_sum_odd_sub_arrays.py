'''

### WeCare Insurance company wants to calculate premium of vehicles.
Vehicles are of two types - "Two Wheeler", "Four Wheeler"
Each vehicle is identified by `vehicle id, type, cost and premium amount`
Premium amount is 2% of the vehicle cost for two wheelers and 6% of vehicle cost for four wheelers

Calculate the premium amount and display the vehicle details.
Write a Python Program to implement the class chosen with its attributes and methods

Consider all instance variables to be private and methods to be public
Include getter and setter methods for all instance variables
Display appropriate error, if the vehicle type is not correct

'''

class WeCare:
    def __init__(self):
        self.__id = None
        self.__type = None
        self.__cost = None
        self.__premium = None
     
    #Setter Function
    def setID(self,ID):
        self.__id = ID
    def setType(self,Type):
        self.__type= Type
    def setCost(self,Cost):
        self.__cost = Cost
    def setPremium(self,prem):
        self.__premium = prem
        
    def calculatepremium(self):
        if self.__type=='Two Wheeler':
            pre = (self.__cost*0.02)
        elif self.__type=='Four Wheeler':
            pre = (self.__cost*0.06)
        else:
            pre=-1
        self.setPremium(pre)
    
    #Getter Function
    def getID(self):
        return self.__id
    def getType(self):
        return self.__type
    def getCost(self):
        return self.__cost
    def getPremium(self):
        return self.__premium
        
    def display(self):
        if self.__premium != -1:
            print("ID: {}, Type: {}, Cost: {}, Premium:{}".format(self.getID(),self.getType(),self.getCost(),self.getPremium()))
        else:
            print("Invalid Vehicle Details")

            ob= WeCare()
ob.setID(101)
ob.setType("Two Wheeler")
ob.setCost(10000)
id(ob)
ob.calculatepremium()
ob.display()