import csv
import matplotlib
matplotlib.use('AGG')
import matplotlib.pyplot as plt

y_data1 = []
y_data2 = []
y_data3 = []
with open('q1.2.1.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
                y_data1.append(row[0])

with open('q1.2.2.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
                y_data2.append(row[0])

with open('q1.2.3.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
                y_data3.append(row[0])

y_data_result1=[]
y_data_result2=[]
y_data_result3=[]
for i in y_data1 :
        y_data_result1.append(i * (44100/1024)) # Sampling Rate / FFT Size
for i in y_data2 :
        y_data_result2.append(i * (44100/1024)) # Sampling Rate / FFT Size
for i in y_data3 :
        y_data_result3.append(i * (44100/1024)) # Sampling Rate / FFT Size


plt.figure()
plt.plot(range(0, len(y_data1)), y_data_result1)
plt.savefig('q1_2_1.png')

plt.figure()
plt.plot(range(0, len(y_data2)), y_data_result2)
plt.savefig('q1_2_2.png')

plt.figure()
plt.plot(range(0, len(y_data3)), y_data_result3)
plt.savefig('q1_2_3.png')
