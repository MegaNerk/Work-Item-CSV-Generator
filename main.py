from retriever import Retriever

from multiprocessing import Process
from multiprocessing import Pipe

from appJar import gui
import csv_writer
import time
import os

def main_run(button = None):
    main_window.stop()
    if button == "Confirm":

        #Clean number entry
        numItemsToGen = main_window.getEntry("How many work items?")
        if numItemsToGen is None:
            numItemsToGen = 1
        numItemsToGen = int(numItemsToGen)

        #Clean directory entry
        csvDir = main_window.getEntry("CSV Output Path")
        if csvDir is None:
            csvDir = ""

        con1, con2 = Pipe()
        countProcess = Process(target=beginCount, args=(con2,numItemsToGen,csvDir))
        countProcess.start()
        createBarWindow(con1)

#region Count Process
def beginCount(connection, numItemsToGen, csvDir):
    #Run primary logic
    start_time = time.perf_counter()
    retriever = Retriever()
    retriever.generateDataSet(numItemsToGen)
    end_time = time.perf_counter()
    print(f"Generated {numItemsToGen} work items in {end_time - start_time} seconds")

    start_time = time.perf_counter()
    dataset = retriever.producePowerBICSVData(connection)
    end_time = time.perf_counter()
    print(f"Built PowerBI Data for {numItemsToGen} work items in {end_time - start_time} seconds")

    start_time = time.perf_counter()
    csv_writer.create_csv("PowerBI CSV", dataset, csvDir)
    end_time = time.perf_counter()
    print(f"Populated CSV in {end_time - start_time} seconds")
#endregion

#region Main Process
def recordCount(connection):
    while True:
        if connection.poll():
            counted, total = connection.recv()
            print(str(counted))
            if counted == total:
                break
    print("We seem to have finished counting!")

def createBarWindow(connection):
    barWindow = gui("Progress", "600x50")
    barWindow.addMeter("Counted Items")
    barWindow.setMeterFill("Counted Items", "blue")
    barWindow.setMeter("Counted Items", 0, "Count progress...")
    barWindow.after(1, lambda: updateBar(barWindow,connection))
    barWindow.go()

def updateBar(window,connection):
    pollingRate = 1 #Polling rate in ms
    counted, total = None, None
    while connection.poll():
        counted, total = connection.recv()
    if counted != None:
        window.setMeter("Counted Items", (counted/total)*100, f"{counted}/{total}")
    if counted == None or counted < total:
        window.after(pollingRate, lambda: updateBar(window,connection))
    
#endregion

if __name__ == "__main__":
    main_window = gui("Work Item Filter", "600x150")
    main_window.addLabel("Set Up Work Item Filter")
    main_window.setLabelBg("Set Up Work Item Filter", "lightblue")

    main_window.addLabelNumericEntry("How many work items?")
    main_window.setEntryDefault("How many work items?", 100)

    main_window.addLabelDirectoryEntry("CSV Output Path")
    main_window.setEntryDefault("CSV Output Path", os.getcwd())

    main_window.addButtons(["Confirm", "Close"], main_run)

    main_window.go()