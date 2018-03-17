import csv
import numpy as np
import matplotlib.pyplot as plt
import sys

#%%  Load csv files into dictionary in list
def Load_csv(filename):
    dic = {}
    dic_list = []
    with open(filename, 'r') as csvfile:
        reader = csvreader(csvfile)
        data = np.array(list(reader))
        for i in range(1,data.shape[0]-1):
            unique, counts = np.unique(data[1:,i], return_counts=True)
            dic = dict(zip(unique,counts))
            dic['Question'] = data[0,i]
            dic_list.append(dic)
    return dic_list

#%% Save the pie chart into image file
def plot_csv(data_list):
    for i in range(len(data_list)):
        fig = plt.figure()
        labels = []
        sizes = []
        for j in data_list[i]:
            if j not 'Question' and j:
                labels.append(j)
                sizes.append(data_list[i][j])
        plt.pie(sizes, labels=labels, autopct='%1.1f%%')
        plt.title(data_list[i]['Question'])
        plt.axis('equal')
        plt.savefig('Question' + str(i+1) + '.png')

#%% Main part
if len(sys.argv) <= 1:
    exit("Require a filename")
else:
    plot_csv(Load_csv(sys.argv[1]))
