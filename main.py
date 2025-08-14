from retriever import Retriever
import csv_writer
import time

numItemsToGen = 100000

start_time = time.perf_counter()
retriever = Retriever()
retriever.generateDataSet(numItemsToGen)
end_time = time.perf_counter()
print(f"Generated {numItemsToGen} work items in {end_time - start_time} seconds")

start_time = time.perf_counter()
dataset = retriever.producePowerBICSVData()
end_time = time.perf_counter()
print(f"Built PowerBI Data for {numItemsToGen} work items in {end_time - start_time} seconds")

start_time = time.perf_counter()
csv_writer.create_csv("PowerBI CSV", dataset)
end_time = time.perf_counter()
print(f"Populated CSV in {end_time - start_time} seconds")