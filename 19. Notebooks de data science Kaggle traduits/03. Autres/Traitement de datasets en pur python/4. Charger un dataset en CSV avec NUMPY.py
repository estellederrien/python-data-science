
# Load CSV from URL using NumPy
from numpy import loadtxt
from urllib.request import urlopen

# Ouvrir un fichier sur internet
# url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv'
# raw_data = urlopen(url)

url = 'datasets\pima-indians-diabetes.data.csv'
raw_data = open(url)

dataset = loadtxt(raw_data, delimiter=",")
print(dataset.shape)