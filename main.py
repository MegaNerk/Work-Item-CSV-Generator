from retriever import Retriever
import csv_writer
import time

numItemsToGen = 1000000

start_time = time.perf_counter()
retriever = Retriever()
retriever.generateDataSet(numItemsToGen)
end_time = time.perf_counter()
print("Generated " + str(numItemsToGen) + " in " + str(end_time - start_time) + " seconds")

start_time = time.perf_counter()
dataset = retriever.producePowerBICSVData()
end_time = time.perf_counter()
print("Built PowerBI Data for " + str(numItemsToGen) + " items in " + str(end_time - start_time) + " seconds")

start_time = time.perf_counter()
csv_writer.create_csv("PowerBI CSV", dataset)
end_time = time.perf_counter()
print("Populated CSV in " + str(end_time - start_time) + " seconds")