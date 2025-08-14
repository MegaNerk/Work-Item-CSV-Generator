import csv
import os

def create_csv(name : str, data : list[dict]):
    #Early exit for no data
    if len(data) < 1:
        return
    
    #Verify legal name
    counter = 1
    extension = ".csv"
    finalName = name + extension
    while os.path.exists(finalName):
        finalName = name + "(" + str(counter) + ")" + extension
        counter += 1

    #Build field names out of given data
    field_names = []
    for key in data[0]:
        field_names.append(str(key))

    #Create and populate CSV file
    with open(finalName, "x", newline = '') as new_csv:
        writer = csv.DictWriter(new_csv, field_names)
        writer.writeheader()
        writer.writerows(data)
        # for entry in data:
        #     writer.writerow(entry)
    pass