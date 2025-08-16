from itemEntry import Prio, Status, ItemType, ItemEntry
from functools import lru_cache
from datetime import datetime

class ItemSet():
    def __init__(self, setItems : list[ItemEntry]):
        self.workItems : list[ItemEntry] = setItems

    #region Section takes arguments and returns a filtered list of items from within the set
    def getFilteredList(self, args : dict, month : int):
        outputList = []
        for item in self.workItems:
            if self.validate(item, args, month):
                outputList.append(item)
        return outputList

    def validate(self, item : ItemEntry, validArgs : dict, month : int) -> bool:
        if month not in item.statuses.keys():
            return False

        if len(validArgs["Teams"]) > 0 and item.team not in validArgs["Teams"]:
            return False
        if len(validArgs["Prios"]) > 0 and item.priority not in validArgs["Prios"]:
            return False
        if len(validArgs["ItemTypes"]) > 0 and item.itemType not in validArgs["ItemTypes"]:
            return False

        if len(validArgs["Statuses"]) > 0:
            index : int = len(item.statuses[month])-1
            if item.statuses[month][index] not in validArgs["Statuses"]:
                return False
            
        return True
    #endregion

    #region PowerBI Systems
    #Formats set data as counts of identical item entries for each month in the given range
    def createPowerBIData(self, monthRange : range, processCallback) -> list[dict]:
        workingData : dict = {}
        data : list[dict] = []
        monthSet = set(monthRange)
        total = len(self.workItems)

        for item in self.workItems:
            for month in item.statuses:
                if month in monthSet:
                    curTag = item.produce_content_tag(month)
                    curItemData = item.get_data(month)
                    if curTag not in workingData:
                        workingData[curTag] = curItemData
                        workingData[curTag]["Count"] = 1
                    else:
                        workingData[curTag]["Count"] += 1
            processCallback.value += 1
        data = list(workingData.values())
        data.sort(key= lambda x: self.parseDateStr(x["Month"]))
        return data
    
    @lru_cache(maxsize=None)
    def parseDateStr(self, date_string : str):
        return datetime.strptime(date_string, "%m/%d/%Y")
    #endregion