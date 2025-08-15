import csv
import os

def create_csv(name : str, data : list[dict], dirPth = ""):
    #Early exit for no data
    if len(data) < 1:
        return
    
    #If path does not exist, make it
    #If file 


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
        writer.writerows(data)
        # for entry in data:
        #     writer.writerow(entry)
    pass