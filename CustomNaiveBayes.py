import numpy as np
import pandas as pd
from math import log
import matplotlib.pyplot as plt
from math import exp, sqrt, pi, log
from scipy.stats import norm
import statistics

def calculate_probability(x,mean,sd):
    exponent = exp(-0.5*((x-mean)/sd)**2)
    return ((1/(sd*sqrt(2*pi)))*exponent)

read = pd.read_csv("Crop_recommendation.csv")

N = float(input("N : "))
P = float(input("P : "))
K = float(input("K : "))
temp = float(input("temp : "))
humidity = float(input("humidity : "))
ph = float(input("Ph : "))
rainfall = float(input("rainfall : "))

data={}
for i in read['label'].unique():
    for col in read.columns[0:len(read.columns)-1]:
        list = []
        for k in range(len(read)):
            if read['label'][k] == i:
                list.append(read[col][k])
        if(col=='N'):
            input = N
        elif (col == 'P'):
            input=P
        elif (col=='K'):
            input = K
        elif (col == 'temperature'):
            input = temp
        elif (col == 'humidity'):
            input = humidity
        elif (col == 'ph'):
            input = ph
        elif (col == 'rainfall'):
            input = rainfall
            
        x_axis = np.asarray(list)
        mean = statistics.mean(x_axis)
        sd = statistics.stdev(x_axis)
        value = calculate_probability(input, mean, sd)
        data[str(i)+str(col)] = value


probabilityofanycrop= 21/(21*100)

Score = {}
score = log(probabilityofanycrop)

for i in read['label'].unique():
    for col in read.columns[0:len(read.columns)-1]:
        try:
            value+=log(data[str(i)+str(col)])
        except:
            value+=log(1)
    Score[i] = value
    value = log(probabilityofanycrop)


maximum = Score['rice']
for keys in Score:
    maximum = max(maximum,Score[keys])
for keys in Score:
    if Score[keys]==maximum :
        print()
        print("Suitable crop is : ",keys)
        