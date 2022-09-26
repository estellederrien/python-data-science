
# Load CSV (using python) https://machinelearningmastery.com/load-machine-learning-data-python/
import csv
import numpy
filename = 'datasets\pima-indians-diabetes.data.csv'
raw_data = open(filename, 'rt')
reader = csv.reader(raw_data, delimiter=',', quoting=csv.QUOTE_NONE)
x = list(reader)
data = numpy.array(x).astype('float')
print(data.shape)