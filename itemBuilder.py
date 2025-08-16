import random
from itemEntry import Prio, Status, ItemType, ItemEntry

class ItemBuilder():
    def __init__(self, setMonths : int = 3):
        self.numberOfMonths : int = setMonths

    #Generates x random item entries
    def buildXRandomItems(self, x : int, processCallback=None) -> list[ItemEntry]:
        outputItemList = []
        i = 0
        while i < x:
            #Randomly generate item entry status history
            randStatusDict = {}
            startMonth =  random.randint(1, self.numberOfMonths)
            endMonth = random.randint(startMonth+1, self.numberOfMonths+1)
            for i2 in range(startMonth, endMonth):
                randStatusDict[i2] = []
                numStatuses = random.randint(1,3)
                for i3 in range(0, numStatuses):
                    randStatusDict[i2].append(random.choice(list(Status))) #33 choices in original problem

            #Randomly generate item entry status history
            randArgs = {}
            randArgs["Team"] = random.randint(1,44) #44 choices in original problem
            randArgs["Prio"] = random.choice(list(Prio)) #3 choices in original problem
            randArgs["Type"] = random.choice(list(ItemType)) #146 choices in original problem

            nextItem = ItemEntry(randArgs["Team"], randArgs["Prio"], randArgs["Type"], randStatusDict, i)

            outputItemList.append(nextItem)
            i += 1
            if processCallback != None:
                processCallback.value += 1
        # for item in outputItemList:
        #     print("Produced Item: " + str(item))
        return outputItemList