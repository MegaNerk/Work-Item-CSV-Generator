from itemSet import ItemSet
from itemBuilder import ItemBuilder

#Holds an item set, which it can parse to create usable data
class Retriever():
    def __init__(self):
        self.validationArgs = {
        "Teams" : [],
        "Prios" : [],
        "ItemTypes" : [],
        "Statuses" : []
        }

        self.activeItemSet : ItemSet = None
        self.numMonths : int = 33

    #Getter for the currently active item set
    def getItemSet(self):
        return self.activeItemSet

    def displayFiltered(self, args : dict = None):
        if args == None:
            args = self.validationArgs

        for curMonth in range(1, self.numMonths+1):
            filteredList = self.activeItemSet.getFilteredList(args, curMonth)
            for item in filteredList:
                print("Filtered Result For Month " + str(curMonth) + ": " + str(item))
    
    #Generates a new random dataset and replaces the old
    def generateDataSet(self, x : int = 1, processCallback = None):
        myItemBuilder = ItemBuilder(self.numMonths)
        newItems = myItemBuilder.buildXRandomItems(x, processCallback)
        self.activeItemSet = ItemSet(newItems)
    
    def producePowerBICSVData(self, processCallback) -> list[dict]:
        return self.activeItemSet.createPowerBIData(range(1,self.numMonths+1), processCallback)