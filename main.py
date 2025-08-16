from retriever import Retriever

from multiprocessing import Process
from multiprocessing import Pipe
from multiprocessing import Value

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

        built = Value('i', 0, lock=False)
        counted = Value('i', 0, lock=False)
        countProcess = Process(target=beginCount, args=(built,counted,numItemsToGen,csvDir))
        countProcess.start()
        createBarWindow(built, counted, numItemsToGen)

#region Count Process
def beginCount(built,count, numItemsToGen, csvDir):
    #Run primary logic
    start_time = time.perf_counter()
    retriever = Retriever()
    retriever.generateDataSet(numItemsToGen,built)
    end_time = time.perf_counter()
    print(f"Generated {numItemsToGen} work items in {end_time - start_time} seconds")

    start_time = time.perf_counter()
    dataset = retriever.producePowerBICSVData(count)
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

def createBarWindow(built, counted, total):
    barWindow = gui("Progress", "600x50")
    
    barWindow.addMeter("Built Items")
    barWindow.setMeterFill("Built Items", "orange")
    barWindow.setMeter("Built Items", 0, "Build Progress...")

    barWindow.addMeter("Counted Items")
    barWindow.setMeterFill("Counted Items", "blue")
    barWindow.setMeter("Counted Items", 0, "Count Progress...")
    barWindow.after(1, lambda: updateBar(barWindow,total,built, counted))
    barWindow.go()

def updateBar(window,total,built,count):
    pollingRate = 1 #Polling rate in ms

    curBuilt = built.value
    window.setMeter("Built Items", (curBuilt/total)*100, f"{curBuilt}/{total} items built")

    curCount = count.value
    window.setMeter("Counted Items", (curCount/total)*100, f"{curCount}/{total} items processed")
    if curCount != total:
         window.after(pollingRate, lambda: updateBar(window,total,built,count))
    
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