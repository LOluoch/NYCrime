from csv import reader
from pyspark import SparkContext, SparkConf
import re

sc = SparkContext(appName="hw2")
sc.setLogLevel("ERROR")

# read input data from HDFS to create an RDD
data = sc.textFile("hdfs://group16-1:54310/hw1-input/NYPD_Complaint_Data_Current_YTD.csv")

# use csv reader to split each line of file into a list of elements.
# this will automatically split the csv data correctly.

splitdata = data.mapPartitions(lambda x: reader(x))
# use filter to select only those rows in which crime type is not blank

splitdata = splitdata.filter(lambda x: x[7])
# a
boro = splitdata.map(lambda x: (x[13],1))
print("Where is most of the crime happening in New York? And what is the total number of crimes reported in that location ? \n")
print(boro.reduceByKey(lambda x,y: x+y).sortBy(lambda x: x[1],ascending=False).take(1))
# b
july = splitdata.filter(lambda x: re.search('^(07[\/]*)', x[5]))
crimes = july.map(lambda x: (x[7],1))
print("What are the top 3 crimes that were reported in the month of July ? \n")
print(crimes.reduceByKey(lambda x,y: x+y).sortBy(lambda x: x[1],ascending=False).take(3))
