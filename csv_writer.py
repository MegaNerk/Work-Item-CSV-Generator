import csv
import os

def create_csv(name : str, data : list[dict], dirPth = "", countCallback = None, totalCallback = None):
    totalRows = len(data)

    #Early exit for no data
    if totalRows < 1:
        return
    
    if totalCallback != None:
        totalCallback.value = totalRows

    #Verify filepath exists
    if dirPth != "":
        if not os.path.exists(dirPth):
            os.makedirs(dirPth)
    
    #Verify legal name
    counter = 1
    extension = ".csv"
    finalName = name + extension
    finalFilePath = os.path.join(dirPth, finalName)
    while os.path.exists(finalFilePath):
        finalName = name + "(" + str(counter) + ")" + extension
        finalFilePath = os.path.join(dirPth, finalName)
        counter += 1

    #Build field names out of given data
    field_names = []
    for key in data[0]:
        field_names.append(str(key))

    #Create and populate CSV file
    with open(finalFilePath, "x", newline = '') as new_csv:
        writer = csv.DictWriter(new_csv, field_names)
        writer.writeheader()
        #writer.writerows(data)
        for entry in data:
            writer.writerow(entry)
            if countCallback != None:
                countCallback.value += 1